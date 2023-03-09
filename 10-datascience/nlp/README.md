# Natural Language Processing (NLP)

## Labs

1. [Natural Language Processing 101](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2021-07-09-concept-nlp-basics.ipynb)
2. [Training Embeddings Using Gensim and FastText](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2021-07-10-concept-embedding-gensim-fasttext.ipynb)
3. [NLP Playground](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2022-01-29-nlp.ipynb)
4. [Email Classification](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-02-email-classification.ipynb)

## Text Preprocessing and Cleaning

```py
import nltk
from nltk.corpus import stopwords
stopwords = list(set(stopwords.words('english')))
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

def preprocess(text):
  text = ' ' + text + ' '
  text = re.sub(confidential_label, 'confidential', text)
  text = text.lower()
  text = re.sub(r'[^a-z ]', ' ', text)
  text = re.sub(r'\b[a-z]\b', ' ', text)
  text = ' '.join([lemmatizer.lemmatize(w, 'v') for w in text.split()])
  text = ' '.join([w for w in text.split() if not w in stopwords])
  text = ' '.join([w for w in text.split() if not w in custom_stopwords])
  seen = set()
  seen_add = seen.add
  text = ' '.join([x for x in text.split() if not (x in seen or seen_add(x))])
  return text
```

```py
import pandas as pd
import re
import nltk
from bs4 import BeautifulSoup
from itertools import groupby
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
nltk.download('stopwords')
stopwords = list(set(stopwords.words('english')))
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')

from tqdm.notebook import tqdm
tqdm.pandas()
```

```py
!pip install ekphrasis
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

text_processor = TextPreProcessor(
  normalize=['url', 'email', 'percent', 'money', 'phone', 
              'user', 'time', 'date', 'number'],
  ### annotate={"hashtag", "allcaps", "elongated", "repeated",
  ###           'emphasis', 'censored'},
  fix_html=True,
  segmenter="twitter",
  corrector="twitter", 
  unpack_hashtags=True,
  unpack_contractions=True,
  spell_correct_elong=False,
  tokenizer=SocialTokenizer(lowercase=False).tokenize,
  dicts=[emoticons]
  )
```

```py
!pip install autocorrect
import autocorrect
speller = autocorrect.Speller()
```

```py
!pip install clean-text[gpl]
from cleantext import clean

def clean_text(text):
    if type(text) is float:
        return ' '
    text = ' ' + text + ' '
    text = BeautifulSoup(text, "lxml").text
    text = re.sub(r"http[s]?://\S+", "", text)
    ### noise removal
    rules = [
        {r'>\s+': u'>'},  ### remove spaces after a tag opens or closes
        {r'\s+': u' '},  ### replace consecutive spaces
        {r'\s*<br\s*/?>\s*': u'\n'},  ### newline after a <br>
        {r'</(div)\s*>\s*': u'\n'},  ### newline after </p> and </div> and <h1/>...
        {r'</(p|h\d)\s*>\s*': u'\n\n'},  ### newline after </p> and </div> and <h1/>...
        {r'<head>.*<\s*(/head|body)[^>]*>': u''},  ### remove <head> to </head>
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  ### show links instead of texts
        {r'[ \t]*<[^<]*?/?>': u''},  ### remove remaining tags
        {r'^\s+': u''}  ### remove spaces at the beginning
    ]
    for rule in rules:
        for (k, v) in rule.items():
            regex = re.compile(k)
            text = regex.sub(v, text)
    text = text.rstrip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'\{[^{}]*\}', ' ', text)
    text = re.sub(r'\s', ' ', text)
    text = ' '.join(text_processor.pre_process_doc(text))
    text = ' '.join(text.split())
    text = re.sub(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', '<hash>', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = ' '.join([k for k,v in groupby(text.split())])
    text = text.lower()
    text = clean(text,
        fix_unicode=True,               ### fix various unicode errors
        to_ascii=True,                  ### transliterate to closest ASCII representation
        lower=True,                     ### lowercase text
        no_line_breaks=False,           ### fully strip line breaks as opposed to only normalizing them
        no_urls=True,                  ### replace all URLs with a special token
        no_emails=True,                ### replace all email addresses with a special token
        no_phone_numbers=True,         ### replace all phone numbers with a special token
        no_numbers=True,               ### replace all numbers with a special token
        no_digits=True,                ### replace all digits with a special token
        no_currency_symbols=True,      ### replace all currency symbols with a special token
        no_punct=True,                 ### remove punctuations
        replace_with_punct="",          ### instead of removing punctuations you may replace them
        replace_with_url="<URL>",
        replace_with_email="<EMAIL>",
        replace_with_phone_number="<PHONE>",
        replace_with_number="<NUMBER>",
        replace_with_digit="0",
        replace_with_currency_symbol="<CUR>",
        lang="en"                       ### set to 'de' for German special handling
    )
    text = re.sub(r'[^a-z<> ]', ' ', text)
    text = re.sub(r'\b[a-z]\b', ' ', text)
    ### text = speller.autocorrect_sentence(text)
    ### text = ' '.join([ps.stem(w) for w in text.split()])
    ### text = ' '.join([lemmatizer.lemmatize(w, 'v') for w in text.split()])
    ### text = ' '.join([w for w in text.split() if not w in stopwords])
    ### seen = set()
    ### seen_add = seen.add
    ### text = ' '.join([x for x in text.split() if not (x in seen or seen_add(x))])
    text = ' '.join(text.split())
    return text
```

```py
import re
NON_ALPHANUM = re.compile(r'[\W]')
NON_ASCII = re.compile(r'[^a-z0-1\s]')

def normalize_texts(texts):
  normalized_texts = ''
  lower = texts.lower()
  no_punctuation = NON_ALPHANUM.sub(r' ', lower)
  no_non_ascii = NON_ASCII.sub(r'', no_punctuation)
  return no_non_ascii

def get_ntc(text):
    name = text.split('-')[0].strip().strip(',')
    text1 = ' '.join(text.split('-')[1:])
    title = text1.split('/')[0].strip().strip(',')
    company = '/'.join(text.split('/')[1:]).split('Phone')[0].split('Email')[0].strip().strip(',')
    return [x.strip() for x in [name, title, company]]

def get_phone_number(text):
    try:
        return text.split('Phone:')[1].split('Email')[0].strip().strip(',')
    except:
        return None

### phoneRegex = re.compile(r'''((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))''', re.VERBOSE)
emailRegex = re.compile(r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''', re.VERBOSE)

def get_email(text):
    matches = []
    for groups in emailRegex.findall(text):
        matches.append(groups) 
    return ','.join(matches).strip().strip(',')

def split_phone(text):
    text = text.replace('/',',')
    text = re.sub("[^+,0-9]", " ", text)
    return text.strip().strip(',')
```

```py
import ast

def pandas_list_parse(lst):
    return ','.join(list(set(ast.literal_eval(lst))))

def pandas_list_explode(df, col, prefix=None, drop_original=True, explode_type=1, split_sign=',', n=5):
    if prefix is None:
        prefix = col+'_'
    if explode_type==1:
        df[col] = df[col].apply(lambda x: '///'.join(x))
        _df = df[col].str.split('///', expand=True).add_prefix(prefix)
    else:
        _df = df[col].str.split(split_sign, expand=True).add_prefix(prefix)
    if _df.shape[1]>n:
        _df = _df.iloc[:,:n]
    df = df.join(_df)
    if drop_original:
        df.drop(col, axis=1, inplace=True)
    return df
```

## TF-IDF Vectorizor

```py
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(stop_words='english', max_df=0.70, min_df=5, ngram_range=(1,2))
X = vect.fit_transform(text)

X_dense = X.todense()
from sklearn.decomposition import PCA
coords = PCA(n_components=2).fit_transform(X_dense)
plt.scatter(coords[:, 0], coords[:, 1], c='m')
plt.show()

def top_tfidf_feats(row, features, top_n=20):
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids]
    df = pd.DataFrame(top_feats, columns=['features', 'score'])
    return df
def top_feats_in_doc(X, features, row_id, top_n=25):
    row = np.squeeze(X[row_id].toarray())
    return top_tfidf_feats(row, features, top_n)

df1 = df.copy()
df1['text'] = df1.text.apply(preprocess)
### df1[df1.text.str.contains('avast')]

features = vect.get_feature_names()
print(top_feats_in_doc(X, features, 10, 10))

def top_mean_feats(X, features, grp_ids=None, min_tfidf=0.1, top_n=25):
  if grp_ids:
      D = X[grp_ids].toarray()
  else:
      D = X.toarray()
  D[D < min_tfidf] = 0
  tfidf_means = np.mean(D, axis=0)
  return top_tfidf_feats(tfidf_means, features, top_n)

  print(top_mean_feats(X, features, top_n=10))
```

## Count Vectorizer

```py
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(stop_words='english', max_df=0.5, min_df=10, ngram_range=(1,3))
vectorizer.fit_transform(df.clean.tolist())

idx = 100
print(df.text.iloc[[idx]].tolist()[0])
pd.DataFrame(vectorizer.inverse_transform(vectorizer.transform([df.clean.tolist()[idx]]))).T[0]
```

## Wordcloud

```py
from wordcloud import WordCloud
all_words = ''.join([word for word in df['clean_text']])
wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title("Some frequent words used in the headlines", weight='bold', fontsize=14)
plt.show()
```
