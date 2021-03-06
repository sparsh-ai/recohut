# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/datasets/datasets.diginetica.ipynb (unless otherwise specified).

__all__ = ['DigineticaDataset', 'DigineticaDatasetv2']

# Cell
import numpy as np

from .bases.session import SessionDatasetv2
from .bases.session_graph import SessionGraphDataset
from ..utils.common_utils import download_url

# Cell
class DigineticaDataset(SessionDatasetv2):
    url = 'https://github.com/RecoHut-Datasets/diginetica/raw/main/train-item-views.csv'

    def __init__(self, root, column_names={'SESSION_ID':'sessionId',
                                        'ITEM_ID': 'itemId',
                                        'TIMEFRAME': 'timeframe',
                                        'EVENT_DATE': 'eventdate'}):
        super().__init__(root, column_names)

    @property
    def raw_file_names(self) -> str:
        return 'train-item-views.csv'

    def download(self):
        path = download_url(self.url, self.raw_dir)

# Cell
class DigineticaDatasetv2(SessionGraphDataset):
    train_url = "https://github.com/RecoHut-Datasets/diginetica/raw/v2/train.txt"
    test_url = "https://github.com/RecoHut-Datasets/diginetica/raw/v2/test.txt"
    all_train_seq_url = "https://github.com/RecoHut-Datasets/diginetica/raw/v2/all_train_seq.txt"

    def __init__(self, root, shuffle=False, n_node=43097, is_train=True):
        self.n_node = n_node
        self.shuffle = shuffle
        self.is_train = is_train
        super().__init__(root, shuffle, n_node)

    @property
    def raw_file_names(self) -> str:
        if self.is_train:
            return ['train.txt', 'all_train_seq.txt']
        return ['test.txt', 'all_train_seq.txt']

    def download(self):
        download_url(self.all_train_seq_url, self.raw_dir)
        if self.is_train:
            download_url(self.train_url, self.raw_dir)
        else:
            download_url(self.test_url, self.raw_dir)