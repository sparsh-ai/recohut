# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models/models.deepwalk.ipynb (unless otherwise specified).

__all__ = ['DeepWalk']

# Cell
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import networkx as nx
import random
import pickle

# Cell
class DeepWalk:
    def __init__(self, is_directed=False, p=1, q=1, num_walks=10, walk_length=80, n_factors=50):
        # p=q=1 for DeeWalk as the random walks are completely unbiased.
        self.is_directed = is_directed
        self.p = p
        self.q = q
        self.num_walks = num_walks
        self.walk_length = walk_length
        self.n_factors = n_factors

    def fit(self, df, save_path=None, user_col='user_id', item_col='item_id', rating_col='rating'):
        try:
            dataset = pickle.load(open(save_path, 'rb'))
            self.node_vecs = dataset['node_vecs']
            self.user2dict = dataset['user2dict']
            self.item2dict = dataset['item2dict']
            self.reverse_user2dict = dataset['reverse_user2dict']
            self.reverse_item2dict = dataset['reverse_item2dict']
        except:
            user_item_graph = nx.Graph()

            user2dict = dict()
            item2dict = dict()
            cnt = 0

            df = df[[user_col, item_col, rating_col]].copy()

            for x in df.values:
                usr = (x[0], 'user')
                item = (x[1], 'item')
                if usr in user2dict:
                    pass
                else:
                    user2dict[usr] = cnt
                    cnt += 1
                if item in item2dict:
                    pass
                else:
                    item2dict[item] = cnt
                    cnt += 1

            # create a user-movie weighted graph using python library networkx
            for x in df.values:
                usr = (x[0], 'user')
                item = (x[1], 'item')
                user_item_graph.add_node(user2dict[usr])
                user_item_graph.add_node(item2dict[item])
                user_item_graph.add_edge(user2dict[usr], item2dict[item], weight=float(x[2]))
            self.user_item_graph = user_item_graph

            # Compute the transition probabilities based on the edge weights.
            self.preprocess_transition_probs()
            walks = self.simulate_walks()
            node_embeddings = self.learn_embeddings(walks)

            self.item2dict = item2dict
            self.user2dict = user2dict
            self.reverse_item2dict = {k:v for v,k in item2dict.items()}
            self.reverse_user2dict = {k:v for v,k in user2dict.items()}

            node_vecs = [node_embeddings[str(i)] for i in range(cnt)]
            self.node_vecs = np.array(node_vecs)

            with open(save_path, 'wb') as f:
                dataset = {
                    'node_vecs': self.node_vecs,
                    'user2dict': self.user2dict,
                    'item2dict': self.item2dict,
                    'reverse_user2dict': self.reverse_user2dict,
                    'reverse_item2dict': self.reverse_item2dict
                }
                pickle.dump(dataset, f)

    def recommend(self, user_id=None, item_id=None, top_k=5):

        if item_id is not None:
            item_idx = self.item2dict[item_id]
            query = self.node_vecs[item_idx].reshape(1,-1)
        elif user_id is not None:
            """
            items are ranked for a given user in terms of the cosine similarities
            of their corresponding embeddings with the embedding of the user.
            """
            user_idx = self.user2dict[user_id]
            query = self.node_vecs[user_idx].reshape(1,-1)

        ranking = cosine_similarity(query, self.node_vecs)
        top_ids = np.argsort(-ranking)[0]
        top_item_ids = [self.reverse_item2dict[j] for j in top_ids if j in self.reverse_item2dict][:top_k]
        top_item_ids = [int(x[0]) for x in top_item_ids]
        return top_item_ids

    def node2vec_walk(self, start_node):
        '''
        Simulate a random walk starting from start node.
        '''
        G = self.user_item_graph
        alias_nodes = self.alias_nodes
        alias_edges = self.alias_edges

        walk = [start_node]

        while len(walk) < self.walk_length:
            cur = walk[-1]
            cur_nbrs = sorted(G.neighbors(cur))
            if len(cur_nbrs) > 0:
                if len(walk) == 1:
                    walk.append(cur_nbrs[self.alias_draw(alias_nodes[cur][0], alias_nodes[cur][1])])
                else:
                    prev = walk[-2]
                    next = cur_nbrs[self.alias_draw(alias_edges[(prev, cur)][0],
                        alias_edges[(prev, cur)][1])]
                    walk.append(next)
            else:
                break

        return walk

    def simulate_walks(self):
        '''
        Repeatedly simulate random walks from each node.
        '''
        G = self.user_item_graph
        walks = []
        nodes = list(G.nodes())
        print('Walk iteration:')
        for walk_iter in range(self.num_walks):
            random.shuffle(nodes)
            for node in nodes:
                walks.append(self.node2vec_walk(start_node=node))

        return walks

    def learn_embeddings(self, walks):
        '''
        Learn embeddings by optimizing the Skipgram objective using SGD.
        Uses Gensim Word2Vec.
        '''
        walks = [list(map(str, walk)) for walk in walks]
        model = Word2Vec(walks, size=50, window=10, min_count=0, sg=1, workers=8, iter=1)
        return model.wv

    def get_alias_edge(self, src, dst):
        '''
        Get the alias edge setup lists for a given edge.
        '''
        G = self.user_item_graph
        p = self.p
        q = self.q

        unnormalized_probs = []
        for dst_nbr in sorted(G.neighbors(dst)):
            if dst_nbr == src:
                unnormalized_probs.append(G[dst][dst_nbr]['weight']/p)
            elif G.has_edge(dst_nbr, src):
                unnormalized_probs.append(G[dst][dst_nbr]['weight'])
            else:
                unnormalized_probs.append(G[dst][dst_nbr]['weight']/q)
        norm_const = sum(unnormalized_probs)
        try:
            normalized_probs =  [float(u_prob)/norm_const for u_prob in unnormalized_probs]
        except:
            normalized_probs =  [0.0 for u_prob in unnormalized_probs]

        return self.alias_setup(normalized_probs)

    def preprocess_transition_probs(self):
        '''
        Preprocessing of transition probabilities for guiding the random walks.
        '''
        G = self.user_item_graph
        is_directed = self.is_directed

        alias_nodes = {}
        for node in G.nodes():
            unnormalized_probs = [G[node][nbr]['weight'] for nbr in sorted(G.neighbors(node))]
            norm_const = sum(unnormalized_probs)
            try:
                normalized_probs =  [float(u_prob)/norm_const for u_prob in unnormalized_probs]
            except:
                print(node)
                normalized_probs =  [0.0 for u_prob in unnormalized_probs]
            alias_nodes[node] = self.alias_setup(normalized_probs)

        alias_edges = {}
        triads = {}

        if is_directed:
            for edge in G.edges():
                alias_edges[edge] = self.get_alias_edge(edge[0], edge[1])
        else:
            for edge in G.edges():
                alias_edges[edge] = self.get_alias_edge(edge[0], edge[1])
                alias_edges[(edge[1], edge[0])] = self.get_alias_edge(edge[1], edge[0])

        self.alias_nodes = alias_nodes
        self.alias_edges = alias_edges

        return

    def alias_setup(self, probs):
        '''
        Compute utility lists for non-uniform sampling from discrete distributions.
        Refer to https://hips.seas.harvard.edu/blog/2013/03/03/the-alias-method-efficient-sampling-with-many-discrete-outcomes/
        for details
        '''
        K = len(probs)
        q = np.zeros(K)
        J = np.zeros(K, dtype=np.int)

        smaller = []
        larger = []
        for kk, prob in enumerate(probs):
            q[kk] = K*prob
            if q[kk] < 1.0:
                smaller.append(kk)
            else:
                larger.append(kk)

        while len(smaller) > 0 and len(larger) > 0:
            small = smaller.pop()
            large = larger.pop()

            J[small] = large
            q[large] = q[large] + q[small] - 1.0
            if q[large] < 1.0:
                smaller.append(large)
            else:
                larger.append(large)

        return J, q

    def alias_draw(self, J, q):
        '''
        Draw sample from a non-uniform discrete distribution using alias sampling.
        '''
        K = len(J)

        kk = int(np.floor(np.random.rand()*K))
        if np.random.rand() < q[kk]:
            return kk
        else:
            return J[kk]