"""This is a collection of utility functions and classes."""

from typing import List, Any
from collections.abc import Sequence

import os
import errno
import pandas as pd
import ast
import json
import pickle5 as pickle
import random
import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import time
import datetime
from pathlib import Path
import logging
from pytz import timezone

import faiss

from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import urllib.request
from urllib.error import HTTPError

import warnings
warnings.filterwarnings('ignore')


def parse_json(txt):
    if isinstance(txt, str):
        try:
            txt = json.loads(txt)
        except:
            txt = ast.literal_eval(txt)  
    return txt


def to_list(value: Any) -> Sequence:
    if isinstance(value, Sequence) and not isinstance(value, str):
        return value
    else:
        return [value]


def makedirs(path):
    try:
        os.makedirs(os.path.expanduser(os.path.normpath(path)))
    except OSError as e:
        if e.errno != errno.EEXIST and os.path.isdir(path):
            raise e


def files_exist(files: List[str]) -> bool:
    # NOTE: We return `False` in case `files` is empty, leading to a
    # re-processing of files on every instantiation.
    return len(files) != 0 and all([os.path.exists(f) for f in files])


def dict_melt(row, dict_col, id_col=None):
    _dict = row[dict_col]
    if _dict == _dict:
        _dict = parse_json(_dict)
        _df = pd.DataFrame(_dict)
        if id_col is not None:
            _df['id'] = row[id_col]
        return _df


def random_date(start, end):
    frmt = '%d-%m-%Y %H:%M'
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + random.random() * (etime - stime)
    dt = datetime.datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return dt
    
    
def calculate_bounce_rate(df):
    bounce_rate = len(df.query('bounced==True'))/len(df)
    return bounce_rate


def capitalize_words(txt, split='_'):
    stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
    txt = [i[0].upper()+i[1:] if i.lower() not in stopwords else i for i in txt.split(split)]
    txt = ' '.join(txt)
    return txt


def get_adventures(lst, primary=True):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        if primary:
            categories = [x['category'] for x in lst]
            categories = [x.lower().replace(' ','_') for x in categories]
        else:
            try:
                categories = [x['sub_category'] for x in lst]
                categories = [item for sublist in categories for item in sublist]
                categories = [x.lower().replace(' ','_') for x in categories]
            except:
                pass
        categories = list(set(categories))
    return categories


def get_adventures_v2(lst):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        categories = [x['category'] for x in lst]
        categories = [x.lower().replace(' ','_') for x in categories]
        subcategories = [x['sub_category'] for x in lst]
        subcategories = [item for sublist in subcategories for item in sublist]
        subcategories = [x.lower().replace(' ','_') for x in subcategories]
        categories+=subcategories
        categories = list(set(categories))
    return categories


def get_sights(lst, primary=True):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        if primary:
            categories = [x['category'] for x in lst]
            categories = [x.lower().replace(' ','_') for x in categories]
        else:
            try:
                categories = [x['sub_category'] for x in lst]
                categories = [item for sublist in categories for item in sublist]
                categories = [item['name'] for item in categories]
                categories = [x.lower().replace(' ','_') for x in categories]
            except:
                pass
        categories = list(set(categories))
    return categories


def get_sights_v2(lst):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        categories = [x['category'] for x in lst]
        categories = [x.lower().replace(' ','_') for x in categories]
        try:
            subcategories = [x['sub_category'] for x in lst]
            subcategories = [item for sublist in subcategories for item in sublist]
            subcategories = [item['name'] for item in subcategories]
            subcategories = [x.lower().replace(' ','_') for x in subcategories]
            categories+=subcategories
        except:
            pass
        categories = list(set(categories))
    return categories


def get_occassions_v2(lst):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        categories = [x['category'] for x in lst]
        categories = [x.lower().replace(' ','_') for x in categories]
        try:
            subcategories = [x['sub_category'] for x in lst]
            subcategories = [item for sublist in subcategories for item in sublist]
            subcategories = [item['name'] for item in subcategories]
            subcategories = [x.lower().replace(' ','_') for x in subcategories]
            categories+=subcategories
        except:
            pass
        categories = list(set(categories))
    return categories


def get_interest_id(lst, df, interest_type='adventure'):
    categories = []
    if lst == lst:
        for x in lst:
            try:
                _id = df.loc[df['name']==x, 'id'].values[0]
                if interest_type == 'adventure':    
                    _id = 'a{}'.format(_id)
                elif interest_type == 'sight':
                    _id = 's{}'.format(_id)
                elif interest_type == 'occassion':
                    _id = 'o{}'.format(_id)
                categories.append(_id)
            except:
                continue
    return categories


def get_facility_categories(_dict):
    categories = []
    if _dict == _dict:
        _dict = parse_json(_dict)
        categories = [item for sublist in list(_dict.values()) for item in sublist]
        categories = [x.lower().replace(' ','_') for x in categories]
        categories = list(set(categories))
    return categories


def get_adventure_categories(lst):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        categories = [x['category'] for x in lst]
        categories = [x.lower().replace(' ','_') for x in categories]
        categories = list(set(categories))
    return categories


def get_food_categories(lst):
    categories = []
    if lst == lst:
        lst = parse_json(lst)
        categories = [x['type'] for x in lst]
        categories = [x.lower().replace(' ','_') for x in categories]
        categories = list(set(categories))
    return categories


def get_season_categories(_dict, key='best_time'):
    categories = []
    if _dict == _dict:
        _dict = parse_json(_dict)
        categories = [x['reason'] for x in _dict[key]]
        categories = [x.lower().replace(' ','_') for x in categories]
        categories = list(set(categories))
    return categories


def len_calendar(_dict, key='days'):
    _len_calendar = 7
    if _dict==_dict:
        _dict = parse_json(_dict)
        _len_calendar = len(_dict[key])
    _len_calendar = _len_calendar/7
    return _len_calendar


def calculate_calendar_length(_dict):
    _len_calendar = 7
    if _dict==_dict:
        _dict = parse_json(_dict)
        _len_calendar = len(_dict["days"])
    _len_calendar = _len_calendar/7
    return _len_calendar


def calculate_product_duration(_dict, key='duration'):
    _duration = 24*60 # 24 hours as the default duration in case it is missing
    if _dict==_dict:
        _dict = parse_json(_dict)
        _duration = int(_dict[key]) if key in _dict.keys() else _duration
    _duration = _duration/(24*60)
    return _duration


def calculate_product_duration_v2(_dict, key='duration'):
    _duration = 24*60 # 24 hours as the default duration in case it is missing
    if _dict==_dict:
        _dict = parse_json(_dict)
        _duration = int(_dict[key]) if key in _dict.keys() else _duration
    _duration = _duration/(24*60)
    return _duration


def pd_melt_lists(df, col):
    lst = df[col].tolist()
    lst = [item for sublist in lst for item in sublist]
    lst = list(set(lst))
    return lst
    

def calculate_age_compatibility(row, trip_min_age, trip_max_age):
    try:
        return 1 if (max(row['min_age'], trip_min_age) - min(row['max_age'], trip_max_age))<=0 else 0
    except Exception as e:
        print(e)
    

def _timediff(start, end, unit='mins', format='%I:%M %p'):
    _timediff = datetime.datetime.strptime(end, format) - datetime.datetime.strptime(start, format)
    _timediff = int(_timediff.seconds)
    if unit=='mins':
        _timediff = _timediff//60
    return _timediff


def calculate_product_period(_dict):
    _period = 24*60
    # if within time period, sum it up
    if _dict==_dict:
        _dict = parse_json(_dict)
        keys = _dict.keys()
        if 'within_time_periods' in list(keys):
            try:
                _lst = _dict['within_time_periods']
                _lst = [dict(t) for t in {tuple(d.items()) for d in _lst}] # remove duplicates
                _period = sum([_timediff(i['from'], i['to']) for i in _lst])
            except:
                pass
        # calculate time different time_period.from - time_period.to
        elif 'time_period' in keys:
            try:
                _period = _timediff(_dict['time_period']['from'], _dict['time_period']['to'])
            except:
                pass
    _period = _period/(24*60)
    return _period


def label_binarizer(df, col):
    mlb = MultiLabelBinarizer(sparse_output=True)
    df = df.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(df.pop(col)),
                index=df.index,
                columns=[col+'_'+x for x in mlb.classes_]))
    return df, mlb


def label_binarizer_v2(df, col):
    mlb = MultiLabelBinarizer(sparse_output=True)
    dfOneHot = pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(df.pop(col)),
                index=df.index,
                columns=[x for x in mlb.classes_])
    df = pd.concat([df, dfOneHot], axis=1)
    return df


def onehot_encoder(df, col, threshold=0.1):
    df[col] = df[col].fillna('Unknown')
    df[col].mask(df[col].map(df[col].value_counts(normalize=True)) < threshold, 'Unknown')
    onehotencoder = OneHotEncoder()
    X = onehotencoder.fit_transform(df[col].values.reshape(-1,1)).toarray()
    dfOneHot = pd.DataFrame(X, columns = [col+'_'+str(int(i)) for i in range(X.shape[1])])
    dfOneHot = dfOneHot.astype('int')
    df = pd.concat([df, dfOneHot], axis=1)
    df = df.drop([col], axis=1)
    return df, onehotencoder


def onehot_encoder_v2(df, col):
    onehotencoder = OneHotEncoder()
    X = onehotencoder.fit_transform(df[col].values.reshape(-1,1)).toarray()
    cols = [x.replace('x0_','') for x in onehotencoder.get_feature_names()]
    dfOneHot = pd.DataFrame(X, columns = cols)
    dfOneHot = dfOneHot.astype('int')
    df = pd.concat([df, dfOneHot], axis=1)
    df = df.drop([col], axis=1)
    return df, onehotencoder


def product_vectorisation(df):
    # select columns
    selected_cols = ['id','day_type','calendar_days','city','country',
                    'adventures','facilities','booking_time_periods',
                    'meals_and_drinks','calendar_season']
    df = df[selected_cols].copy()

    # change from int to str
    df['id'] = df['id'].astype('str')

    # 1-hot encode day_type
    df['day_type'].replace({'all_day':0, 'within_day':1}, inplace=True)
    df['day_type'].fillna(0, inplace=True)

    # derive calendar length from calendar days
    df['calendar_length'] = df.calendar_days.apply(len_calendar, key='days')

    # binary flag (1-hot encode) of calendar days
    df['calendar_days'] = df['calendar_days'].apply(lambda x: parse_json(x)['days'] if x==x else [])
    df, mlb_calendar_days = label_binarizer(df, 'calendar_days')
    
    # for city, country, adventures, facilities
    # impute missing value with 'na' label
    # select top 90%ile categories, replace othet with 'na' label
    # 1-hot encode
    df, city_onehotencoder = onehot_encoder(df, 'city')
    df, country_onehotencoder = onehot_encoder(df, 'country')

    df['adventures'] = df['adventures'].apply(get_adventure_categories)
    df, mlb_adventures = label_binarizer(df, 'adventures')
    df['facilities'] = df['facilities'].apply(get_facility_categories)
    df, mlb_facilities = label_binarizer(df, 'facilities')

    # derive product_period and product_duration from booking_time_periods
    df['product_duration'] = df.booking_time_periods.apply(calculate_product_duration)
    # df['product_period'] = df.apply(calculate_product_period, axis=1)
    df['product_period'] = df.booking_time_periods.apply(calculate_product_period)

    # derive meals and drinks types from meals_and_drinks
    # e.g. whether breakfast is included, dinner is included
    # binary/bool encode
    df['meals_and_drinks'] = df['meals_and_drinks'].apply(get_food_categories)
    df, mlb_meals_and_drinks = label_binarizer(df, 'meals_and_drinks')

    # labels (e.g. summer, winter, automn) for best time, high season and best weather
    df['best_time'] = df['calendar_season'].apply(get_season_categories, key='best_time')
    df, mlb_best_time = label_binarizer(df, 'best_time')
    df['high_season'] = df['calendar_season'].apply(get_season_categories, key='high_season')
    df, mlb_high_season = label_binarizer(df, 'high_season')
    df['best_weather'] = df['calendar_season'].apply(get_season_categories, key='best_weather')
    df, mlb_best_weather = label_binarizer(df, 'best_weather')

    # drop columns
    drop_cols = ['booking_time_periods', 'calendar_season']
    df.drop(drop_cols, inplace=True, axis=1)

    # return data
    return df


def calculate_cosine_similarity(product_vecs, target_vec):
    target_vec = target_vec.reshape(1, -1)
    sims = pd.DataFrame(index = product_vecs.index)
    sims['similarity'] = cosine_similarity(product_vecs, target_vec)
    sims = sims.sort_values(by='similarity', ascending=False)
    return sims


def calculate_cosine_similarity_v2(df):
    A = df.to_numpy()
    similarities = cosine_similarity(A)
    similarities[np.tril_indices(df.shape[0])] = -2
    cos_score_df = pd.DataFrame(similarities)
    cos_score_df.index = df.index
    cos_score_df.columns = np.array(df.index)
    return cos_score_df


def onehot_list_encoder(df, col):
    mlb = MultiLabelBinarizer()
    df = df.join(pd.DataFrame(mlb.fit_transform(df.pop(col)),
                        columns=mlb.classes_,
                        index=df.index))
    return df, mlb


def get_product_maps(df):
    product_category_map = df[['id', 'product_category_id']].set_index('id').to_dict()['product_category_id']
    product_category_map = {str(k):str(v) for k,v in product_category_map.items()}
    product_category_map_reversed = defaultdict(list)
    for key, value in product_category_map.items():
        product_category_map_reversed[value].append(key)

    product_sub_category_map = df[['id', 'product_sub_category_id']].set_index('id').to_dict()['product_sub_category_id']
    product_sub_category_map = {str(k):str(v) for k,v in product_sub_category_map.items()}
    product_sub_category_map_reversed = defaultdict(list)
    for key, value in product_sub_category_map.items():
        product_sub_category_map_reversed[value].append(key)

    return {
        'product_category_map': product_category_map,
        'product_category_map_reversed': product_category_map_reversed,
        'product_sub_category_map': product_sub_category_map,
        'product_sub_category_map_reversed': product_sub_category_map_reversed,
    }


def save_pickle(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)
    

def load_pickle(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


def get_average_amount(val, mode='min'):
    default = {'min':500, 'max':2500}
    if val == val:
        if val == '$500 - $2500':
            default = {'min':500, 'max':2500}
        elif val == '$2500 - $5000':
            default = {'min':2500, 'max':5000}
        elif val == '$5000 - $7500':
            default = {'min':5000, 'max':7500}
        elif val == '$7500 +':
            default = {'min':7500, 'max':1e8}
    if mode == 'min':
        return default['min']
    else:
        return default['max']


def calculate_product_price(row):
    product_id = row['id']
    retail_price = pd.DataFrame([{'retail_price':None, 'min':None, 'max':None}])
    _dict = row['adult_price']
    if _dict == _dict:
        _dict = parse_json(_dict)
        if 'retail_price' in _dict.keys():
            retail_price = pd.DataFrame([{'retail_price':_dict['retail_price'], 'min':1, 'max':1}])
            if 'group_price' in _dict.keys():
                try:
                    retail_price = pd.concat([retail_price,
                                            pd.DataFrame(_dict['group_price'])[['retail_price','min','max']]],
                                            axis=0)
                except:
                    pass
    retail_price['id'] = product_id
    return retail_price


def get_age_range(col):
    default_age = (30, 30)
    if col == col:
        try:
            col = parse_json(col)
        except:
            return default_age
        if isinstance(col, list):
            if not len(col):
                return default_age
            col = col[0]
        min = col['min_age']
        max = col['max_age']
        diff = (int(min), int(max))
        return diff
    return default_age


def interest_similarity(trip_id, product_vecs, common_cols, trip_choices):
    trip_id = str(trip_id)
    target_vec = trip_choices.loc[[trip_id]]
    target_vec = target_vec[common_cols]
    sims = calculate_cosine_similarity(product_vecs, target_vec.to_numpy())
    sims.reset_index(inplace=True)
    sims = sims[['id','similarity']].set_index('id')
    return sims


def calculate_season(_dict, days, key='best_time'):
    output = None
    if _dict == _dict:
        _dict = parse_json(_dict)
        start_month = [x['from'] for x in _dict['best_time']][0]
        end_month = [x['to'] for x in _dict['best_time']][0]
        months = pd.date_range(f'{start_month} 01, 2021', f'{end_month} 01, 2022', freq='MS').strftime("%B").tolist()
        if len(months) > 12:
            months = pd.date_range(f'{start_month} 01, 2022', f'{end_month} 01, 2022', freq='MS').strftime("%B").tolist()
        # current_month = datetime.datetime.utcnow().strftime("%B")
        # output = 1 if current_month in months else 0
        output = len([x for x in months if x in days])
    return output


def calculate_trip_length(trip_id, trips, unit='day'):
    trip_start_date = trips.loc[trips['id']==trip_id, 'start_date'].values.tolist()[0]
    trip_end_date = trips.loc[trips['id']==trip_id, 'end_date'].values.tolist()[0]
    list_days = []
    if unit == 'day':
        list_days = pd.date_range(trip_start_date, trip_end_date, freq='d').strftime("%a").tolist()
    elif unit == 'month':
        list_days = pd.date_range(trip_start_date, trip_end_date, freq='m').strftime("%B").tolist()
    return list_days


def calculate_days_overlap(_dict, days):
    output = None
    if _dict==_dict:
        _dict = parse_json(_dict)["days"]
        days = {x:days.count(x) for x in days}
        output = {k:v for k,v in days.items() if k in _dict}
    return output


def calculate_guest_compatibility(row, trip_guests):
    output = 0
    min_guests = row['min_travellers']
    max_guests = row['max_travellers']
    if (min_guests==min_guests) and (max_guests==max_guests):
        output = 1 if ((trip_guests>=min_guests) and (trip_guests<=max_guests)) else 0
    return output


def standardize(data, col, zero_as_miss=True):
    # select col
    df = data[[col]]
    # convert missing to nan
    if zero_as_miss:
        df = df.replace({'0':np.nan, 0:np.nan})
    # fill nan with mean
    df.fillna(df.mean(), inplace=True)
    df.fillna(0, inplace=True) # for handling all-zero cases
    # normalize the data
    min_max_scaler = MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(df.values)
    df = pd.DataFrame(x_scaled)
    df.columns = [col]
    return df, min_max_scaler


def print_json(_json):
    parsed = json.loads(_json)
    print(json.dumps(parsed, indent=4, sort_keys=True))


def generate_base_image(path='./base.png', dimension=(100,200)):
    array = np.zeros([dimension[0], dimension[1], 3], dtype=np.uint8)
    img = Image.fromarray(array)
    base_img_path = os.path.join(path)
    img.save(base_img_path)


def download_images(row, basepath='./', use_base_image=True):
    if isinstance(row, str):
        url = row
    else:
        url = row['url']
    base_img_path = os.path.join(basepath, 'base.png')
    filename = url.split('/')[-1]
    save_path = os.path.join(basepath, filename)
    if not (os.path.exists(save_path) and os.stat(save_path).st_size > 0):
        try:
            urllib.request.urlretrieve(url, save_path)
            if os.path.exists(save_path) and os.stat(save_path).st_size > 0:
                print('Downloaded at {}'.format(save_path))
                return save_path
        except (ValueError, HTTPError):
            if use_base_image:
                return base_img_path
            else:
                pass
    else:
        return save_path
    
    
def download_videos(url, basepath='./'):
    filename = url.split('/')[-1]
    # if (len(filename.split('.'))<2) or (filename.split('.')[-1] not in ['mp4']):
    if (len(filename.split('.'))<2):
        # adding .mp4 extension, but a better logic will be added in later version
        filename+='.mp4'
    save_path = os.path.join(basepath, filename)
    if not (os.path.exists(save_path) and os.stat(save_path).st_size > 0):
        try:
            urllib.request.urlretrieve(url, save_path)
            if os.path.exists(save_path) and os.stat(save_path).st_size > 0:
                print('Downloaded at {}'.format(save_path))
                return save_path
        except (ValueError, HTTPError):
            pass
    else:
        return save_path
        

def get_photos_videos(row):
    _dict = row['photos_and_videos']
    if _dict == _dict:
        _df = pd.DataFrame(parse_json(_dict))
    else:
        _df = pd.DataFrame([{'type':None, 'url':None}])
    _df['id'] = row['id']
    return _df


def get_img_path(url, basepath='./'):
    base_img_path = os.path.join(basepath, 'base.png')
    filename = url.split('/')[-1]
    save_path = os.path.join(basepath, filename)
    if os.path.exists(save_path) and os.stat(save_path).st_size > 0:
        return save_path
    else:
        return base_img_path


def get_ann_top_items_img_grid(embedding_model, ann_index, img_path, k=10):
    query = Image.open(img_path).convert('RGB')
    query_vector = embedding_model([query])
    top_docs = ann_index.query(query_vector, k)
    images = [mpimg.imread(img_path[1]['save_path']) for img_path in top_docs]
    titles = ["({}, dist={:.2f})".format(x[1]['name'], x[0]) for x in top_docs]
    plt.figure(figsize=(20,10))
    columns = 5
    for i, image in enumerate(images):
        plt.subplot(len(images) / columns + 1, columns, i + 1)
        plt.title(titles[i])
        plt.imshow(image)
        plt.axis('off')


def get_ann_top_items(embedding_model, ann_index, query, k=10):
    query_vector = embedding_model([query]).numpy()
    top_docs = ann_index.query(query_vector, k)
    return top_docs


def get_ann_top_items_img(embedding_model, ann_index, img_path, k=10):
    query = Image.open(img_path).convert('RGB')
    query_vector = embedding_model([query])
    top_docs = ann_index.query(query_vector, k)
    return top_docs


class IndexFlatL2():
    
  def __init__(self, dimension, documents, embeddings=None, index=None):
    self.dimension = dimension
    self.documents = documents
    self.embeddings = embeddings
    self.index = index

  def build(self, num_bits=8):
    if self.index is None:
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)

  def query(self, input_embedding, k=5):
    distances, indices = self.index.search(input_embedding, k)
    return [(distance, self.documents.loc[index].to_dict()) for distance, index in zip(distances[0], indices[0])]


def convert_sparse_to_dense(df):
    sparse_int_cols = [x[0] for x in zip(df.columns, df.dtypes) if 'Sparse[int64' in str(x[1])]
    df.loc[:, sparse_int_cols] = df.loc[:, sparse_int_cols].sparse.to_dense()
    return df


def set_logger(log_path):
    """A Python module.

    Args:
        log_path (str): Path where you want to save the log file
    
    Examples:
        ```python
        set_logger('./model_a.log')
        logging.info('Model A Logging Test Success')
        ```
    """
    log_dir = str(Path(log_path).parent)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # logs may not show in the file without the two lines
    for handler in logging.root.handlers[:]: 
        logging.root.removeHandler(handler)
        
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s P%(process)d %(levelname)s %(message)s',
                        handlers=[logging.FileHandler(log_path, mode='w'),
                                  logging.StreamHandler()])
    

def get_now(datetime_format="%Y%m%d%H%M%S"):
    return datetime.datetime.now(timezone('utc')).strftime(datetime_format)    


def calculate_product_deprior(self, mode='train', path=None, weights=None,
                              feedbacks=None, product_ids=None, return_df=False):
    """Sort products based on feedback responses and de-prioritise low-feedback products."""
    
    if mode == 'train':
        # load the raw datasets
        customer_product_feedbacks = pd.read_csv(self.raw_path_customer_product_feedbacks)
        product_ratings = pd.read_csv(self.raw_path_product_ratings)
        vendor_ratings = pd.read_csv(self.raw_path_vendor_ratings)
        products = pd.read_csv(self.raw_path_products)

        feedbacks = products[['id','vendor_organization_id']]\
        .merge(vendor_ratings[['vendor_organization_id', 'stars', 
                            'quality_of_information', 'customer_experience']],
            on='vendor_organization_id', how='left')
        
        feedbacks = feedbacks[['id', 'stars', 
                            'quality_of_information', 
                            'customer_experience']]

        feedbacks.rename(columns={'stars':'vendor_stars',
                                'quality_of_information':'vendor_quality_of_info',
                                'customer_experience':'vendor_customer_experience'},
                        inplace=True)
        feedbacks = feedbacks.merge(product_ratings[['product_id', 'description', 'photos_and_videos',
            'customer_feedback', 'type_of_adventure', 'top_sights',
            'review_connections', 'customer_requests', 'covid_19_updates']],
            how='left', left_on='id', right_on='product_id')\
            .drop('product_id', axis=1)

        cust_feedbacks = customer_product_feedbacks[['product_id','thumbs']]
        thumbs_down = cust_feedbacks.loc[cust_feedbacks['thumbs']=='down'].groupby(by='product_id').count()
        thumbs_down.fillna(thumbs_down.mean(), inplace=True)
        thumbs_up = cust_feedbacks.loc[cust_feedbacks['thumbs']=='up'].groupby(by='product_id').count()
        thumbs_up.fillna(thumbs_up.mean(), inplace=True)
        thumbs = thumbs_down.merge(thumbs_up, on='product_id', how='outer', suffixes=('_down', '_up'))
        thumbs['thumbs'] = thumbs['thumbs_up']/thumbs['thumbs_down']
        thumbs = thumbs[['thumbs']]

        feedbacks = feedbacks.merge(thumbs, left_on='id', right_on='product_id', how='left')
        feedbacks.set_index('id', inplace=True)

        cols = ['vendor_stars', 'vendor_quality_of_info', 'vendor_customer_experience',
            'description', 'photos_and_videos', 'customer_feedback',
            'type_of_adventure', 'top_sights', 'review_connections',
            'customer_requests', 'covid_19_updates', 'thumbs']

        feedback_se = {}

        for col in cols:
            stds = standardize(feedbacks, col)
            feedbacks[col] = stds[0][col].values
            feedback_se[col] = stds[1]

        # save the processed data
        feedbacks.to_pickle(path)
        
    else:
        if weights is None:
            weights = {
                    'covid_19_updates': 1,
                    'customer_feedback': 3,
                    'customer_requests': 1,
                    'description': 2,
                    'photos_and_videos': 2,
                    'review_connections': 2,
                    'thumbs': 3,
                    'top_sights': 1,
                    'type_of_adventure': 1,
                    'vendor_customer_experience': 1,
                    'vendor_quality_of_info': 1,
                    'vendor_stars': 1
                    }
            
        feedbacks.index = feedbacks.index.astype('str')
        
        # left join with product ids list to make sure all the given input product ids have some score
        if product_ids is not None:
            product_ids = [str(x) for x in product_ids]
            _df = pd.DataFrame({"id":product_ids})
            feedbacks = _df.merge(feedbacks, how='left', on='id')
            feedbacks.fillna(0, inplace=True)
            feedbacks.set_index('id', inplace=True)
            
        # calculate weighted feedback scores
        feedbacks['final_score'] = np.array([(feedbacks[x]*weights[x]).values for x in feedbacks.columns]).sum(axis=0)
            
        # sort values
        feedbacks.sort_values(by='final_score', ascending=False, inplace=True)
        
        if return_df:
            return feedbacks.to_json()

        return feedbacks[['final_score']].to_dict()