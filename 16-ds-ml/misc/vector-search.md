# Vector Search

## Faiss

```python
import faiss
from vector_engine.utils import vector_search, id2details

# Step 1: Change data type
embeddings = np.array([embedding for embedding in embeddings]).astype("float32")

# Step 2: Instantiate the index
index = faiss.IndexFlatL2(embeddings.shape[1])

# Step 3: Pass the index to IndexIDMap
index = faiss.IndexIDMap(index)

# Step 4: Add vectors and their IDs
index.add_with_ids(embeddings, df.id.values)

print(f"Number of vectors in the Faiss index: {index.ntotal}")

# Retrieve the 10 nearest neighbours
D, I = index.search(np.array([embeddings[5415]]), k=10)
print(f'L2 distance: {D.flatten().tolist()}\n\nMAG paper IDs: {I.flatten().tolist()}')

# Wrap all steps in the vector_search function.
# It takes four arguments: 
# A query, the sentence-level transformer, the Faiss index and the number of requested results
D, I = vector_search([user_query], model, index, num_results=10)
print(f'L2 distance: {D.flatten().tolist()}\n\nMAG paper IDs: {I.flatten().tolist()}')

# Serialise index and store it as a pickle
with open(f"{project_dir}/models/faiss_index.pickle", "wb") as h:
    pickle.dump(faiss.serialize_index(index), h)
```

## Elasticsearch

<a href="https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2021-04-20-dl-retrieval.ipynb" alt=""> <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>

```python
# download the latest elasticsearch version
!wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.11.1-linux-x86_64.tar.gz
!tar -xzvf elasticsearch-7.11.1-linux-x86_64.tar.gz
!chown -R daemon:daemon elasticsearch-7.11.1

# prep the elasticsearch server
import os
from subprocess import Popen, PIPE, STDOUT
es_subprocess = Popen(['elasticsearch-7.11.1/bin/elasticsearch'], stdout=PIPE, stderr=STDOUT, preexec_fn=lambda : os.setuid(1))

# wait for a few minutes for the local host to start
!curl -X GET "localhost:9200/"

# install elasticsearch python api
!pip install -q elasticsearch

# check if elasticsearch server is properly running in the background
from elasticsearch import Elasticsearch, helpers
es_client = Elasticsearch(['localhost'])
es_client.info()
```

## Annoy

<a href="https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2021-04-27-image-similarity-recommendations.ipynb" alt=""> <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>


```python
!pip install -q annoy

from annoy import AnnoyIndex

# Defining data structures as empty dict
file_index_to_file_name = {}
file_index_to_file_vector = {}
file_index_to_product_id = {}

# Configuring annoy parameters
dims = 256
n_nearest_neighbors = 20
trees = 10000

# Reads all file names which stores feature vectors 
allfiles = glob.glob('/content/img_vectors/*.npz')

t = AnnoyIndex(dims, metric='angular')

for findex, fname in tqdm(enumerate(allfiles)):
  file_vector = np.loadtxt(fname)
  file_name = os.path.basename(fname).split('.')[0]
  file_index_to_file_name[findex] = file_name
  file_index_to_file_vector[findex] = file_vector
  try:
    file_index_to_product_id[findex] = match_id(file_name)
  except IndexError:
    pass 
  t.add_item(findex, file_vector)

t.build(trees)
t.save('t.ann')

file_path = '/content/drive/MyDrive/ImgSim/'
t.save(file_path+'indexer.ann')
pickle.dump(file_index_to_file_name, open(file_path+"file_index_to_file_name.p", "wb"))
pickle.dump(file_index_to_file_vector, open(file_path+"file_index_to_file_vector.p", "wb"))
pickle.dump(file_index_to_product_id, open(file_path+"file_index_to_product_id.p", "wb"))

path_dict = {}
for path in Path('/content/Fashion_data/categories').rglob('*.jpg'):
  path_dict[path.name] = path

nns = t.get_nns_by_vector(test_vec, n=topK)
plt.figure(figsize=(20, 10))
for i in range(topK):
  x = file_index_to_file_name[nns[i]]
  x = path_dict[x+'.jpg']
  y = file_index_to_product_id[nns[i]]
  title = '\n'.join([str(j) for j in list(styles.loc[y].values[-5:])])
  plt.subplot(1, topK, i+1)
  plt.title(title)
  plt.imshow(mpimg.imread(x))
  plt.axis('off')
plt.tight_layout()
```

## Milvus Redis

<a href="https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2021-06-23-movielens-milvus-redis-efficient-retrieval.ipynb" alt=""> <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>


```python
!git clone -b 1.1 https://github.com/milvus-io/milvus.git
% cd /content/milvus/core
! ./ubuntu_build_deps.sh
!./build.sh -t Release
# !./build.sh -t Release -g

% cd /content/milvus/core/milvus
! echo $LD_LIBRARY_PATH
import os
os.environ['LD_LIBRARY_PATH'] +=":/content/milvus/core/milvus/lib"
! echo $LD_LIBRARY_PATH
% cd scripts
! nohup ./start_server.sh &
! cat nohup.out

from milvus import Milvus, IndexType, MetricType, Status
import redis

milv = Milvus(host = '127.0.0.1', port = 19530)
r = redis.StrictRedis(host="127.0.0.1", port=6379)

COLLECTION_NAME = 'demo_films'
PARTITION_NAME = 'Movie'

#Dropping collection for clean slate run
milv.drop_collection(COLLECTION_NAME)

param = {'collection_name':COLLECTION_NAME, 
         'dimension':32, 
         'index_file_size':2048, 
         'metric_type':MetricType.L2
        }

milv.create_collection(param)

status = milv.insert(collection_name=COLLECTION_NAME, records=embeddings, ids=ids)

import numpy as np
from paddle_serving_app.local_predict import LocalPredictor

class RecallServerServicer(object):
    def __init__(self):
        self.uv_client = LocalPredictor()
        self.uv_client.load_model_config("movie_recommender/user_vector_model/serving_server_dir") 
        
    def hash2(self, a):
        return hash(a) % 1000000

    def get_user_vector(self):
        dic = {"userid": [], "gender": [], "age": [], "occupation": []}
        lod = [0]
        dic["userid"].append(self.hash2('0'))
        dic["gender"].append(self.hash2('M'))
        dic["age"].append(self.hash2('23'))
        dic["occupation"].append(self.hash2('6'))
        lod.append(1)

        dic["userid.lod"] = lod
        dic["gender.lod"] = lod
        dic["age.lod"] = lod
        dic["occupation.lod"] = lod
        for key in dic:
            dic[key] = np.array(dic[key]).astype(np.int64).reshape(len(dic[key]),1)
        fetch_map = self.uv_client.predict(feed=dic, fetch=["save_infer_model/scale_0.tmp_1"], batch=True)
        return fetch_map["save_infer_model/scale_0.tmp_1"].tolist()[0]

recall = RecallServerServicer()
user_vector = recall.get_user_vector()
```

## Matrix Factorization Recommendation Retrieval

<a href="https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-31-retrieval-preferredai.ipynb" alt=""> <img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
