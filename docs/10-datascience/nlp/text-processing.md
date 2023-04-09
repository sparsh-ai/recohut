# Text Processing

## Tokenization

### Gensim tokenizer

```py
import gensim

df['tokens'] = df['clean_text'].apply(gensim.utils.simple_preprocess)
```