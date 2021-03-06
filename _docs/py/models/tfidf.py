# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models/models.tfidf.ipynb (unless otherwise specified).

__all__ = ['TFIDFRecommender']

# Cell
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Cell
class TFIDFRecommender:
    """
    TF-IDF (Term Frequency — Inverse Document Frequency) calculates how important
    words are in relation to the whole document. TF summarizes how often a given
    word appears within a document. IDF downscales words that appear frequently
    across documents. This allows TF-IDF to define the importance of words within
    a document based on the relationship and weighting factor.
    """
    def __init__(self, ngram_range=(1,2), min_df=50, analyzer='word', stop_words='english'):
        self.ngram_range = ngram_range
        self.min_df = min_df
        self.analyzer = analyzer
        self.stop_words = stop_words

    def clean_data(self):
        # selecting only id and text columns
        self.data = self.data[[self.id_col, self.text_col]]
        # dropping rows with NA in id/text column
        self.data = self.data.dropna()
        # make data type string
        self.data = self.data.astype('str')

    def fit(self, data, id_col='id', text_col='text'):
        self.data = data
        self.id_col = id_col
        self.text_col = text_col
        self.clean_data()
        self.ids = self.data[self.id_col]
        self.text = self.data[self.text_col]
        tf = TfidfVectorizer(analyzer=self.analyzer,
                             ngram_range=self.ngram_range,
                             min_df=self.min_df,
                             stop_words=self.stop_words)
        tfidf_matrix = tf.fit_transform(self.text)
        # Use numeric values to find similarities
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        self.indices = pd.Series(self.data.index, index=self.ids)
        self.indices = self.indices.to_dict()

    def _recommend(self, id):
        idx = self.indices[id]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # sim_scores = sim_scores[1:11] # How many results to display
        item_indices = [i[0] for i in sim_scores]
        id_df = pd.DataFrame({self.id_col: self.ids.iloc[item_indices].tolist(),
                              'similarity': [i[1] for i in sim_scores],
                              'text': self.text.iloc[item_indices].tolist()},
                             index=item_indices)
        return id_df

    def recommend(self, id, topk=10):

        id = str(id)

        # get recommended items
        rec_df = self._recommend(id)
        rec_df = rec_df.dropna()

        # get text of the target item
        rec_item_text = self.data[self.data[self.id_col] == id][self.text_col].to_list()[0].split()

        # create dictionary of text lists by item id
        item_text_dict = {}
        for id in rec_df[self.id_col].tolist():
            item_text_dict[id] = self.data[self.data[self.id_col] == id][self.text_col].to_list()

        # create dictionary of text statistics by item id
        text_stats = {}
        for item, text in item_text_dict.items():
            text = text[0].split()
            text_stats[item] = {}
            text_stats[item]['total_text'] = len(text)
            same_text = set(rec_item_text).intersection(set(text)) # Get text in recommended item that are also in target item
            text_stats[item]['%_common_text'] = (len(same_text) / len(text)) * 100

        # convert dictionary to dataframe
        text_stats_df = pd.DataFrame.from_dict(text_stats, orient='index').reset_index().rename(columns={'index': self.id_col})

        # merge text statistics dataframe to recommended items dataframe
        all_stats_df = pd.merge(rec_df, text_stats_df, on=self.id_col)
        return all_stats_df.iloc[1:topk+1]