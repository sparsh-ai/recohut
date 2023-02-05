# Text Cleaning

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
  # annotate={"hashtag", "allcaps", "elongated", "repeated",
  #           'emphasis', 'censored'},
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
```

```py
def clean_text(text):
    if type(text) is float:
        return ' '
    text = ' ' + text + ' '
    text = BeautifulSoup(text, "lxml").text
    text = re.sub(r"http[s]?://\S+", "", text)
    # noise removal
    rules = [
        {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
        {r'\s+': u' '},  # replace consecutive spaces
        {r'\s*<br\s*/?>\s*': u'\n'},  # newline after a <br>
        {r'</(div)\s*>\s*': u'\n'},  # newline after </p> and </div> and <h1/>...
        {r'</(p|h\d)\s*>\s*': u'\n\n'},  # newline after </p> and </div> and <h1/>...
        {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove <head> to </head>
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # show links instead of texts
        {r'[ \t]*<[^<]*?/?>': u''},  # remove remaining tags
        {r'^\s+': u''}  # remove spaces at the beginning
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
        fix_unicode=True,               # fix various unicode errors
        to_ascii=True,                  # transliterate to closest ASCII representation
        lower=True,                     # lowercase text
        no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
        no_urls=True,                  # replace all URLs with a special token
        no_emails=True,                # replace all email addresses with a special token
        no_phone_numbers=True,         # replace all phone numbers with a special token
        no_numbers=True,               # replace all numbers with a special token
        no_digits=True,                # replace all digits with a special token
        no_currency_symbols=True,      # replace all currency symbols with a special token
        no_punct=True,                 # remove punctuations
        replace_with_punct="",          # instead of removing punctuations you may replace them
        replace_with_url="<URL>",
        replace_with_email="<EMAIL>",
        replace_with_phone_number="<PHONE>",
        replace_with_number="<NUMBER>",
        replace_with_digit="0",
        replace_with_currency_symbol="<CUR>",
        lang="en"                       # set to 'de' for German special handling
    )
    text = re.sub(r'[^a-z<> ]', ' ', text)
    text = re.sub(r'\b[a-z]\b', ' ', text)
    # text = speller.autocorrect_sentence(text)
    # text = ' '.join([ps.stem(w) for w in text.split()])
    # text = ' '.join([lemmatizer.lemmatize(w, 'v') for w in text.split()])
    # text = ' '.join([w for w in text.split() if not w in stopwords])
    # seen = set()
    # seen_add = seen.add
    # text = ' '.join([x for x in text.split() if not (x in seen or seen_add(x))])
    text = ' '.join(text.split())
    return text
```