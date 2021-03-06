# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/datasets/datasets.movielens.ipynb (unless otherwise specified).

__all__ = ['ML1mDataset', 'ML1mDataModule', 'ML1mDataset_v2', 'ML1mDataModule_v2', 'ML1mDataset_v3',
           'ML1mDataModule_v3', 'ML1mDataset_v4', 'ML100kDataset', 'sparseFeature', 'create_ml_1m_dataset',
           'create_implicit_ml_1m_dataset']

# Cell
from typing import Any, Iterable, List, Optional, Tuple, Union, Callable
import os
import json

import pandas as pd
import numpy as np

import torch

from ..utils.common_utils import *
from .bases.common import Dataset
from .bases.interactions import InteractionsDataset, InteractionsDataModule
from .bases.sequential import SequentialDataset, SequentialDataModule
from ..utils.splitting import stratified_split_v2

# Cell
class ML1mDataset(InteractionsDataset):
    url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"

    @property
    def raw_file_names(self):
        return 'ratings.dat'

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        from shutil import move, rmtree
        move(os.path.join(self.raw_dir, 'ml-1m', self.raw_file_names), self.raw_dir)
        rmtree(os.path.join(self.raw_dir, 'ml-1m'))
        os.unlink(path)

    def load_ratings_df(self):
        df = pd.read_csv(self.raw_paths[0], sep='::', header=None, engine='python')
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        # drop duplicate user-item pair records, keeping recent ratings only
        df.drop_duplicates(subset=['uid', 'sid'], keep='last', inplace=True)
        return df

# Cell
class ML1mDataModule(InteractionsDataModule):
    dataset_cls = ML1mDataset

# Cell
class ML1mDataset_v2(SequentialDataset):
    url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"

    @property
    def raw_file_names(self):
        return 'ratings.dat'

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        from shutil import move, rmtree
        move(os.path.join(self.raw_dir, 'ml-1m', self.raw_file_names), self.raw_dir)
        rmtree(os.path.join(self.raw_dir, 'ml-1m'))
        os.unlink(path)

    def load_ratings_df(self):
        df = pd.read_csv(self.raw_paths[0], sep='::', header=None, engine='python')
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df

# Cell
class ML1mDataModule_v2(SequentialDataModule):
    dataset_cls = ML1mDataset_v2

# Cell
class ML1mDataset_v3(SequentialDataset):
    url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"

    def __init__(self, data_dir, data_type='train', *args, **kwargs):
        super().__init__(data_dir, data_type, *args, **kwargs)
        if data_type == 'train':
            self.ratings_frame = pd.read_csv(self.processed_paths[0], delimiter=",")
        elif data_type == 'valid':
            self.ratings_frame = pd.read_csv(self.processed_paths[1], delimiter=",")
        elif data_type == 'test':
            self.ratings_frame = pd.read_csv(self.processed_paths[2], delimiter=",")

    @property
    def raw_file_names(self):
        return ['ratings.dat', 'movies.dat', 'users.dat']

    @property
    def processed_file_names(self):
        return ['train.csv', 'valid.csv', 'test.csv']

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        from shutil import move, rmtree
        for raw_file_name in self.raw_file_names:
            move(os.path.join(self.raw_dir, 'ml-1m', raw_file_name), self.raw_dir)
        rmtree(os.path.join(self.raw_dir, 'ml-1m'))
        os.unlink(path)

    def load_ratings_df(self):
        df = pd.read_csv(self.raw_paths[0], sep='::', header=None, engine='python')
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df

    def load_movies_df(self):
        df = pd.read_csv(self.raw_paths[1], sep='::', header=None, engine='python')
        df.columns = ["sid", "title", "genres"]
        return df

    def load_users_df(self):
        df = pd.read_csv(self.raw_paths[2], sep='::', header=None, engine='python')
        df.columns = ["uid", "sex", "age_group", "occupation", "zip_code"]
        return df

    def process(self):
        ## movies
        movies = self.load_movies_df()
        movies["year"] = movies["title"].apply(lambda x: x[-5:-1])
        movies.year = pd.Categorical(movies.year)
        movies["year"] = movies.year.cat.codes
        movies["sid"] = movies["sid"].astype(str)

        genres = ["Action","Adventure","Animation","Children's","Comedy","Crime",
                "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical",
                "Mystery","Romance","Sci-Fi","Thriller","War","Western"]

        for genre in genres:
            movies[genre] = movies["genres"].apply(
                lambda values: int(genre in values.split("|"))
            )

        ## users
        users = self.load_users_df()
        users.sex = pd.Categorical(users.sex)
        users["sex"] = users.sex.cat.codes
        users.age_group = pd.Categorical(users.age_group)
        users["age_group"] = users.age_group.cat.codes
        users.occupation = pd.Categorical(users.occupation)
        users["occupation"] = users.occupation.cat.codes
        users.zip_code = pd.Categorical(users.zip_code)
        users["zip_code"] = users.zip_code.cat.codes
        users["uid"] = users["uid"].astype(str)

        # ratings
        ratings = self.load_ratings_df()
        ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')
        ratings["sid"] = ratings["sid"].astype(str)
        ratings["uid"] = ratings["uid"].astype(str)

        # Transform the movie ratings data into sequences
        # First, let's sort the the ratings data using the unix_timestamp,
        # and then group the movie_id values and the rating values by user_id.
        # The output DataFrame will have a record for each user_id, with two
        # ordered lists (sorted by rating datetime): the movies they have rated,
        # and their ratings of these movies.

        ratings_group = ratings.sort_values(by=["timestamp"]).groupby("uid")

        ratings_data = pd.DataFrame(
            data={
                "uid": list(ratings_group.groups.keys()),
                "sids": list(ratings_group.sid.apply(list)),
                "ratings": list(ratings_group.rating.apply(list)),
                "timestamps": list(ratings_group.timestamp.apply(list)),
            }
        )

        # Now, let's split the movie_ids list into a set of sequences of a fixed
        # length. We do the same for the ratings. Set the sequence_length variable
        # to change the length of the input sequence to the model. You can also
        # change the step_size to control the number of sequences to generate for
        # each user.
        ratings_data.sids = ratings_data.sids.apply(
            lambda ids: self.create_sequences(ids, self.history_size, self.step_size)
        )
        ratings_data.ratings = ratings_data.ratings.apply(
            lambda ids: self.create_sequences(ids, self.history_size, self.step_size)
        )
        del ratings_data["timestamps"]

        # After that, we process the output to have each sequence in a separate
        # records in the DataFrame. In addition, we join the user features with
        # the ratings data.
        ratings_data_movies = ratings_data[["uid", "sids"]].explode(
            "sids", ignore_index=True
        )
        ratings_data_rating = ratings_data[["ratings"]].explode("ratings", ignore_index=True)
        ratings_data_transformed = pd.concat([ratings_data_movies, ratings_data_rating], axis=1)
        ratings_data_transformed = ratings_data_transformed.join(
            users.set_index("uid"), on="uid"
        )
        ratings_data_transformed.sids = ratings_data_transformed.sids.apply(
            lambda x: ",".join(x)
        )
        ratings_data_transformed.ratings = ratings_data_transformed.ratings.apply(
            lambda x: ",".join([str(v) for v in x])
        )
        del ratings_data_transformed["zip_code"]
        ratings_data_transformed.rename(
            columns={"sids": "sequence_sids", "ratings": "sequence_ratings"},
            inplace=True,
        )
        # Finally, we split the data into training and testing splits, with 85%
        # and 15% of the instances, respectively, and store them to CSV files.
        random_selection = np.random.rand(len(ratings_data_transformed.index)) <= 0.85
        train_data = ratings_data_transformed[random_selection]
        test_data = ratings_data_transformed[~random_selection]

        # save
        train_data.to_csv(self.processed_paths[0], index=False, sep=",")
        test_data.to_csv(self.processed_paths[1], index=False, sep=",")
        test_data.to_csv(self.processed_paths[2], index=False, sep=",")

    def __len__(self):
        return len(self.ratings_frame)

    def __getitem__(self, idx):
        data = self.ratings_frame.iloc[idx]
        user_id = data.uid
        movie_history = eval(data.sequence_sids)
        movie_history_ratings = eval(data.sequence_ratings)
        target_movie_id = movie_history[-1:][0]
        target_movie_rating = movie_history_ratings[-1:][0]
        movie_history = torch.LongTensor(movie_history[:-1])
        movie_history_ratings = torch.LongTensor(movie_history_ratings[:-1])
        sex, age_group, occupation = data.sex, data.age_group, data.occupation
        output = (user_id, movie_history, target_movie_id, movie_history_ratings,
                  target_movie_rating, sex, age_group, occupation)
        return output

# Cell
class ML1mDataModule_v3(SequentialDataModule):
    dataset_cls = ML1mDataset_v3

# Cell
class ML1mDataset_v4(InteractionsDataset):
    url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"

    @property
    def raw_file_names(self):
        return 'ratings.dat'

    @property
    def processed_file_names(self):
        return 'data.json'

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        from shutil import move, rmtree
        move(os.path.join(self.raw_dir, 'ml-1m', self.raw_file_names), self.raw_dir)
        rmtree(os.path.join(self.raw_dir, 'ml-1m'))
        os.unlink(path)

    def load_ratings_df(self):
        df = pd.read_csv(self.raw_paths[0], sep='::', header=None, engine='python')
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        # drop duplicate user-item pair records, keeping recent ratings only
        df.drop_duplicates(subset=['uid', 'sid'], keep='last', inplace=True)
        return df

    def process(self):
        df = self.load_ratings_df()
        train, test = stratified_split_v2(df, ratio=0.7, col_user='uid', col_item='sid')

        min_session_length = 2
        session_len = test.groupby('uid').size()
        test = test[np.in1d(test['uid'], session_len[session_len >= min_session_length].index)]

        last_items = test.sort_values(by=['uid', 'timestamp']).groupby('uid').timestamp.idxmax()
        y_test = test.loc[last_items]
        x_test = test[~test.index.isin(y_test.index)]

        data = dict()

        def formatRecords(g):
            keys = ['uid','sid','rating']
            result = []
            for item in g.values.tolist():
                item = dict(zip(keys, item))
                result.append(item)
            return result

        data['x_train'] = list(train.groupby('uid').apply(lambda g: formatRecords(g)).to_dict().values())
        data['x_test'] = list(x_test.groupby('uid').apply(lambda g: formatRecords(g)).to_dict().values())
        data['y_test'] = list(y_test.groupby('uid').apply(lambda g: formatRecords(g)).to_dict().values())

        with open(self.processed_paths[0], "w") as f:
            json.dump(data, f)

    def load(self):
        with open(self.processed_paths[0]) as f:
            data = json.load(f)
        return data

# Cell
class ML100kDataset(Dataset):
    url = 'https://files.grouplens.org/datasets/movielens/ml-100k.zip'

    def __init__(self, root):
        super().__init__(root)

    @property
    def raw_file_names(self) -> str:
        return ['u1.base', 'u1.test', 'u4.test', 'allbut.pl', 'u.item',
                'ua.test', 'u.occupation', 'u3.test', 'u5.base', 'ub.test',
                'u2.test', 'u3.base', 'u.genre', 'u.data', 'u4.base',
                'u5.test', 'u.info', 'README', 'ub.base', 'mku.sh', 'u2.base',
                'u.user', 'ua.base']

    @property
    def processed_file_names(self) -> str:
        raise NotImplementedError

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        from shutil import move, rmtree
        file_names = os.listdir(osp.join(self.raw_dir, 'ml-100k'))
        for file_name in file_names:
            move(osp.join(self.raw_dir, 'ml-100k', file_name), self.raw_dir)
        rmtree(osp.join(self.raw_dir, 'ml-100k'))
        os.unlink(path)

    def process(self):
        raise NotImplementedError

# Cell
import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from collections import defaultdict

# Cell
def sparseFeature(feat, feat_num, embed_dim=4):
    """
    create dictionary for sparse feature
    :param feat: feature name
    :param feat_num: the total number of sparse features that do not repeat
    :param embed_dim: embedding dimension
    :return:
    """
    return {'feat': feat, 'feat_num': feat_num, 'embed_dim': embed_dim}

# Cell
def create_ml_1m_dataset(file, trans_score=2, embed_dim=8, test_neg_num=100):
    """
    :param file: A string. dataset path.
    :param trans_score: A scalar. Greater than it is 1, and less than it is 0.
    :param embed_dim: A scalar. latent factor.
    :param test_neg_num: A scalar. The number of test negative samples
    :return: user_num, item_num, train_df, test_df
    """
    print('==========Data Preprocess Start=============')
    data_df = pd.read_csv(file, sep="::", engine='python',
                          names=['user_id', 'item_id', 'label', 'Timestamp'])
    # filtering
    data_df['item_count'] = data_df.groupby('item_id')['item_id'].transform('count')
    data_df = data_df[data_df.item_count >= 5]
    # trans score
    data_df = data_df[data_df.label >= trans_score]
    # sort
    data_df = data_df.sort_values(by=['user_id', 'Timestamp'])
    # split dataset and negative sampling
    print('============Negative Sampling===============')
    train_data, val_data, test_data = defaultdict(list), defaultdict(list), defaultdict(list)
    item_id_max = data_df['item_id'].max()
    for user_id, df in tqdm(data_df[['user_id', 'item_id']].groupby('user_id')):
        pos_list = df['item_id'].tolist()

        def gen_neg():
            neg = pos_list[0]
            while neg in set(pos_list):
                neg = random.randint(1, item_id_max)
            return neg

        neg_list = [gen_neg() for i in range(len(pos_list) + test_neg_num)]
        for i in range(1, len(pos_list)):
            hist_i = pos_list[:i]
            if i == len(pos_list) - 1:
                test_data['user_id'].append(user_id)
                test_data['pos_id'].append(pos_list[i])
                test_data['neg_id'].append(neg_list[i:])
            elif i == len(pos_list) - 2:
                val_data['user_id'].append(user_id)
                val_data['pos_id'].append(pos_list[i])
                val_data['neg_id'].append(neg_list[i])
            else:
                train_data['user_id'].append(user_id)
                train_data['pos_id'].append(pos_list[i])
                train_data['neg_id'].append(neg_list[i])
    # feature columns
    user_num, item_num = data_df['user_id'].max() + 1, data_df['item_id'].max() + 1
    feat_col = [sparseFeature('user_id', user_num, embed_dim),
                sparseFeature('item_id', item_num, embed_dim)]
    # shuffle
    random.shuffle(train_data)
    random.shuffle(val_data)
    train = [np.array(train_data['user_id']), np.array(train_data['pos_id']),
               np.array(train_data['neg_id'])]
    val = [np.array(val_data['user_id']), np.array(val_data['pos_id']),
             np.array(val_data['neg_id'])]
    test = [np.array(test_data['user_id']), np.array(test_data['pos_id']),
              np.array(test_data['neg_id'])]
    print('============Data Preprocess End=============')
    return feat_col, train, val, test

# Cell
def create_implicit_ml_1m_dataset(file, trans_score=2, embed_dim=8, maxlen=40):
    """
    :param file: A string. dataset path.
    :param trans_score: A scalar. Greater than it is 1, and less than it is 0.
    :param embed_dim: A scalar. latent factor.
    :param maxlen: A scalar. maxlen.
    :return: user_num, item_num, train_df, test_df
    """
    print('==========Data Preprocess Start=============')
    data_df = pd.read_csv(file, sep="::", engine='python',
                          names=['user_id', 'item_id', 'label', 'Timestamp'])
    # implicit dataset
    data_df = data_df[data_df.label >= trans_score]

    # sort
    data_df = data_df.sort_values(by=['user_id', 'Timestamp'])

    train_data, val_data, test_data = [], [], []

    item_id_max = data_df['item_id'].max()
    for user_id, df in tqdm(data_df[['user_id', 'item_id']].groupby('user_id')):
        pos_list = df['item_id'].tolist()

        def gen_neg():
            neg = pos_list[0]
            while neg in pos_list:
                neg = random.randint(1, item_id_max)
            return neg

        neg_list = [gen_neg() for i in range(len(pos_list) + 100)]
        for i in range(1, len(pos_list)):
            hist_i = pos_list[:i]
            if i == len(pos_list) - 1:
                test_data.append([user_id, hist_i, pos_list[i], 1])
                for neg in neg_list[i:]:
                    test_data.append([user_id, hist_i, neg, 0])
            elif i == len(pos_list) - 2:
                val_data.append([user_id, hist_i, pos_list[i], 1])
                val_data.append([user_id, hist_i, neg_list[i], 0])
            else:
                train_data.append([user_id, hist_i, pos_list[i], 1])
                train_data.append([user_id, hist_i, neg_list[i], 0])
    # item feature columns
    user_num, item_num = data_df['user_id'].max() + 1, data_df['item_id'].max() + 1
    feature_columns = [sparseFeature('user_id', user_num, embed_dim),
                       sparseFeature('item_id', item_num, embed_dim)]

    # shuffle
    random.shuffle(train_data)
    random.shuffle(val_data)
    # random.shuffle(test_data)

    # create dataframe
    train = pd.DataFrame(train_data, columns=['user_id', 'hist', 'target_item', 'label'])
    val = pd.DataFrame(val_data, columns=['user_id', 'hist', 'target_item', 'label'])
    test = pd.DataFrame(test_data, columns=['user_id', 'hist', 'target_item', 'label'])

    print('==================Padding===================')
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    train_X = [train['user_id'].values, pad_sequences(train['hist'], maxlen=maxlen), train['target_item'].values]
    train_y = train['label'].values
    val_X = [val['user_id'].values, pad_sequences(val['hist'], maxlen=maxlen), val['target_item'].values]
    val_y = val['label'].values
    test_X = [test['user_id'].values, pad_sequences(test['hist'], maxlen=maxlen), test['target_item'].values]
    test_y = test['label'].values.tolist()
    print('============Data Preprocess End=============')
    return feature_columns, (train_X, train_y), (val_X, val_y), (test_X, test_y)