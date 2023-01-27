# Python code

## Generating a hash for given string

```py
# import hashlib
import sys

input_str = sys.argv[1]
# hash_object = hashlib.sha256(b"{}".format(input_str))
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

from passlib.context import CryptContext
hash_object = CryptContext(schemes=["bcrypt"])
print(hash_object.hash(input_str))
```

## Insert path in scripts

```py
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
```

## Clean filenames in a folder

```python
import re
import os
import pathlib
import glob

nbs = glob.glob('/content/docs/docs/tutorials/*.md')

def process(path):
    x = str(pathlib.Path(path).stem)
    x = x.lower()
    x = re.sub(r'[^a-z]','-',x)
    x = re.sub(r'-+','-',x)
    x = x.strip('-')
    x = os.path.join(str(pathlib.Path(path).parent), x+'.mdx')
    x = re.sub('/[a-z]\-','/',x)
    os.rename(path, x)

_ = [process(x) for x in nbs]
```

## Converting Jupyter notebooks into markdown

```python
!cd /content && git clone https://github.com/abc/nbs.git
!pip install -q jupytext
!cd /content/nbs && jupytext *.ipynb --to markdown
```

```python
import glob
import os

nbs = glob.glob('/content/nbs/*.ipynb')

for x in nbs:
    mds = x[:-6]+'.md'
    if not os.path.exists(mds):
        try:
          !jupyter nbconvert --to markdown "{x}"
        except:
            print('error in {}'.format(x))
```

## Scraping

### BS4

```python
import bs4
import requests
import lxml.etree as xml

URLs = ["https://www.flexjobs.com/blog/post/job-search-strategies-for-success-v2/",
        "https://www.monster.com/career-advice/article/five-ps-of-job-search-progress"]

i = 0
web_page = bs4.BeautifulSoup(requests.get(URLs[i], {}).text, "lxml")
df.loc[i,'title'] = web_page.head.title.text
sub_web_page = web_page.find_all(name="article", attrs={"class": "single-post-page"})[0]
article = '. '.join([wp.text for wp in sub_web_page.find_all({"h2","p"})])
df.loc[i,'text'] = article
        
```