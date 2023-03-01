from typing import List, Optional, Callable, Union, Any, Tuple, Dict

import os
import pandas as pd
import json
import numpy as np
from sklearn.preprocessing import MinMaxScaler

import faiss
import tensorflow_hub as hub

import torch
from torchvision.transforms import Compose, Lambda
from torchvision.transforms._transforms_video import (
    CenterCropVideo,
    NormalizeVideo,
)
from pytorchvideo.data.encoded_video import EncodedVideo
from pytorchvideo.transforms import (
    ApplyTransformToKey,
    ShortSideScale,
    UniformTemporalSubsample
)

from moviepy.editor import VideoFileClip

from img2vec_pytorch import Img2Vec
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

from utils import *
from base import Recommendation


class Metadata(Recommendation):
    """
    Using text, images and videos to identify interest sub-categories
    """
    
    device = "cpu" # set to cuda to load on GPU

    @property
    def processed_file_names(self) -> Union[str, List[str], Tuple]:
        """The name of the files in the processed_path folder that
        must be present in order to skip training."""
        return ['multimodal_adventures.p',
                'multimodal_img_faiss.index',
                'multimodal_text_faiss.index',
                'kinetics_id_to_classname.p']


    def init_processed_paths(self):
        """
        initiate the file paths for processed data
        """
        self.processed_path_adventures = os.path.join(self.processed_dir, 'multimodal_adventures.p')
        self.processed_path_img_faiss_index = os.path.join(self.processed_dir, 'multimodal_img_faiss.index')
        self.processed_path_text_faiss_index = os.path.join(self.processed_dir, 'multimodal_text_faiss.index')
        self.processed_path_model_use_v5 = os.path.join(self.processed_dir, 'models/pretrained/use_v5')
        self.processed_path_model_torch_model_zoo = os.path.join(self.processed_dir, 'models/pretrained/torch_model_zoo')
        self.processed_path_kinetics_id_to_classname = os.path.join(self.processed_dir, 'kinetics_id_to_classname.p')

        os.environ['TORCH_HOME'] = self.processed_path_model_torch_model_zoo


    def process(self):
        """
        load the raw data, process it and save into processed data folder
        """
        # load the interests table
        adventures = pd.read_csv(self.raw_path_adventures)
        sights = pd.read_csv(self.raw_path_sights)

        # load the text vectorisation model
        embed = hub.KerasLayer(self.processed_path_model_use_v5)
        
        # process and save the interests table
        adventures = adventures[['id', 'name', 'icon', 'parent_id']]
        sights = sights[['id', 'name', 'icon', 'parent_id']]
        adventures = adventures.append(sights, ignore_index=True)
        adventures['save_path'] = adventures['icon'].apply(get_img_path, basepath=self.raw_path_images_adventures)
        save_pickle(adventures, self.processed_path_adventures)

        # convert text to vectors and save
        embeddings = embed(adventures['name'].tolist()).numpy()
        index_flat_text = IndexFlatL2(512, adventures, embeddings)
        index_flat_text.build()
        faiss.write_index(index_flat_text.index, self.processed_path_text_faiss_index)

        # convert image to vectors and save
        BUFFERSIZE = 100
        img_paths = adventures.save_path.tolist()
        img2vec = Img2Vec(cuda=False)
        img_vecs = None
        for i in range(0, len(img_paths), BUFFERSIZE):
            max_range = (i+BUFFERSIZE) if (i+BUFFERSIZE) <= len(img_paths) else len(img_paths)
            _img_paths = img_paths[i:i+BUFFERSIZE]
            _vectors = img2vec.get_vec([Image.open(ipath).convert('RGB') for ipath in _img_paths])
            if img_vecs is None:
                img_vecs = _vectors
            else:
                img_vecs = np.vstack((img_vecs, _vectors))
                
        index_flat_img = IndexFlatL2(512, adventures, img_vecs)
        index_flat_img.build()
        faiss.write_index(index_flat_img.index, self.processed_path_img_faiss_index)
        
        with open(self.raw_path_kinetics_classnames , "r") as f:
            kinetics_classnames = json.load(f)

        # Create an id to label name mapping
        kinetics_id_to_classname = {}
        for k, v in kinetics_classnames.items():
            kinetics_id_to_classname[v] = str(k).replace('"', "")

        kinetics_id_to_classname = pd.DataFrame(kinetics_id_to_classname.items(), columns=['id','label']).sort_values(by='id')
        kinetics_id_to_classname.set_index('id', inplace=True)
        kinetics_id_to_classname.to_pickle(self.processed_path_kinetics_id_to_classname)


    def load(self):
        """
        load the processed data from processed data folder into memory
        """
        self.adventures = load_pickle(self.processed_path_adventures)
        self.embed = hub.KerasLayer(self.processed_path_model_use_v5)
        img2vec = Img2Vec(cuda=False)
        self.img_embed = lambda x: img2vec.get_vec(x)
        text_index = faiss.read_index(self.processed_path_text_faiss_index)
        self.index_flat_text = IndexFlatL2(512, self.adventures, index=text_index)
        self.index_flat_text.build()
        img_index = faiss.read_index(self.processed_path_img_faiss_index)
        self.index_flat_img = IndexFlatL2(512, self.adventures, index=img_index)
        self.index_flat_img.build()
        
        self.kinetics_id_to_classname = pd.read_pickle(self.processed_path_kinetics_id_to_classname)

        device = self.device
        model_name = "x3d_xs"
        mean = [0.45, 0.45, 0.45]
        std = [0.225, 0.225, 0.225]
        frames_per_second = 30
        model_transform_params  = {
            "x3d_xs": {
                "side_size": 182,
                "crop_size": 182,
                "num_frames": 4,
                "sampling_rate": 12,
            }
        }
    
        self.model = torch.hub.load("facebookresearch/pytorchvideo:main",
                                    model=model_name,
                                    pretrained=True)
        # set to eval mode and move to desired device
        self.model = self.model.to(device)
        self.model = self.model.eval()

        transform_params = model_transform_params[model_name]

        self.transform =  ApplyTransformToKey(
            key="video",
            transform=Compose(
                [
                    UniformTemporalSubsample(transform_params["num_frames"]),
                    Lambda(lambda x: x/255.0),
                    NormalizeVideo(mean, std),
                    ShortSideScale(size=transform_params["side_size"]),
                    CenterCropVideo(
                        crop_size=(transform_params["crop_size"], transform_params["crop_size"])
                    )
                ]
            ),
        )

        # duration of the input clip is specific to the model
        self.clip_duration = (transform_params["num_frames"] * transform_params["sampling_rate"])/frames_per_second


    def classify_video(self,
                       video_path,
                       topk = 5,
                       headstart = 0,
                       limit = 60,
                       verbose = True,
                       ):
        
        pred_class_names_all = []

        
        clip_length = VideoFileClip(video_path).duration # in seconds
        clip_length = clip_length - headstart
        clip_length = clip_length if clip_length < limit else limit

        segments = int(clip_length // self.clip_duration)

        for i in range(0, segments):

            start_sec = headstart + i * self.clip_duration

            # Select the duration of the clip to load by specifying the start and end duration
            # The start_sec should correspond to where the action occurs in the video
            end_sec = start_sec + self.clip_duration

            if verbose:
                print('Analysing {:.2f}s-{:.2f}s clip segment | Segment {}/{}'\
                    .format(start_sec, end_sec, i+1, segments))

            # Initialize an EncodedVideo helper class
            video = EncodedVideo.from_path(video_path)

            # Load the desired clip
            video_data = video.get_clip(start_sec=start_sec, end_sec=end_sec)

            # Apply a transform to normalize the video input
            video_data = self.transform(video_data)

            # Move the inputs to the desired device
            inputs = video_data["video"]
            inputs = inputs.to(self.device)[None, ...] # for X3D model

            # Pass the input clip through the model 
            preds = self.model(inputs)

            # Get the predicted classes 
            post_act = torch.nn.Softmax(dim=1)
            preds = post_act(preds)
            pred_classes = preds.topk(k=topk).indices

            # Map the predicted classes to the label names
            pred_class_names = self.kinetics_id_to_classname.loc[[int(i) for i in pred_classes[0]], 'label'].values.tolist()
            pred_class_names_all.extend(pred_class_names)