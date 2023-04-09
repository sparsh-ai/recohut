# Natural Language Processing (NLP)

## Text Classification

![/img/content-concepts-raw-text-classification-img.png](/img/content-concepts-raw-text-classification-img.png)

### Introduction

- **Definition**: Text classification is a supervised learning method for learning and predicting the category or the class of a document given its text content. The state-of-the-art methods are based on neural networks of different architectures as well as pre-trained language models or word embeddings.
- **Applications**: Spam classification, sentiment analysis, email classification, service ticket classification, question and comment classification
- **Scope**: Muticlass and Multilabel classification
- **Tools**: TorchText, Spacy, NLTK, FastText, HuggingFace, pyss3

### Models

#### FastText

*[Bag of Tricks for Efficient Text Classification. arXiv, 2016.](https://arxiv.org/abs/1607.01759)*

fastText is an open-source library, developed by the Facebook AI Research lab. Its main focus is on achieving scalable solutions for the tasks of text classification and representation while processing large datasets quickly and accurately.

#### XLNet

*[XLNet: Generalized Autoregressive Pretraining for Language Understanding. arXiv, 2019.](https://arxiv.org/abs/1906.08237)*

#### BERT

*[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv, 2018.](https://arxiv.org/abs/1810.04805)*

#### TextCNN

*[What Does a TextCNN Learn?. arXiv, 2018.](https://arxiv.org/abs/1801.06287)*

#### Embedding

Feature extraction using either any pre-trained embedding models (e.g. Glove, FastText embedding) or custom-trained embedding model (e.g. using Doc2Vec) and then training an ML classifier (e.g. SVM, Logistic regression) on these extracted features.

#### Bag-of-words

Feature extraction using methods (CountVectorizer, TF-IDF) and then training an ML classifier (e.g. SVM, Logistic regression) on these extracted features.

### Process flow

Step 1: Collect text data

Collect via surveys, scrap from the internet or use public datasets

Step 2: Create Labels

In-house labeling or via outsourcing e.g. amazon mechanical turk

Step 3: Data Acquisition

Setup the database connection and fetch the data into python environment

Step 4: Data Exploration

Explore the data, validate it and create preprocessing strategy

Step 5: Data Preparation

Clean the data and make it ready for modeling

Step 6: Model Building

Create the model architecture in python and perform a sanity check

Step 7: Model Training

Start the training process and track the progress and experiments

Step 8: Model Validation

Validate the final set of models and select/assemble the final model

Step 9: UAT Testing

Wrap the model inference engine in API for client testing

Step 10: Deployment

Deploy the model on cloud or edge as per the requirement

Step 11: Documentation

Prepare the documentation and transfer all assets to the client  

### Use Cases

#### Email Classification

The objective is to build an email classifier, trained on 700K emails and 300+ categories. Preprocessing pipeline to handle HTML and template-based content. Ensemble of FastText and BERT classifier. Check out [this](https://www.notion.so/MOFSL-Email-Classification-309EC-7a451afa54d446b7b8f2f656450c6167) notion.

#### User Sentiment towards Vaccine

Based on the tweets of the users, and manually annotated labels (label 0 means against vaccines and label 1 means in-favor of vaccine), build a binary text classifier. 1D-CNN was trained on the training dataset. Check out [this](https://www.notion.so/Twitter-Sentiment-Analysis-18d2d4ca41314b88a18db5c93f9eb2b2) notion

#### ServiceNow IT Ticket Classification

Based on the short description, along with a long description if available for that particular ticket, identify the subject of the incident ticket in order to automatically classify it into a set of pre-defined categories. e.g. If custom wrote "Oracle connection giving error", this ticket type should be labeled as "Database". Check out [this](https://www.notion.so/ESMCafe-IT-Support-Ticket-Management-69965830d39d486194f9a2f1222a81d8) notion.

#### Toxic Comment Classification

Check out [this](https://www.notion.so/Toxic-Comment-Classification-Challenge-E5207-affac70cc5614f6dad38ab11ac15e1ab) notion.

#### Pre-trained Transformer Experiments

Experiment with different types of text classification models that are available in the HuggingFace Transformer library. Wrapped experiment based inference as a streamlit app.

#### Long Docs Classification

Check out this [colab](https://colab.research.google.com/github/ArmandDS/bert_for_long_text/blob/master/final_bert_long_docs.ipynb).

#### BERT Sentiment Classification

Scrap App reviews data from Android playstore. Fine-tune a BERT model to classify the review as positive, neutral or negative. And then deploy the model as an API using FastAPI. Check out [this](https://www.notion.so/BERT-Sentiment-Analysis-and-FastAPI-Deployment-43175-d0d19b234561445a84517538ad211405) notion.

### Libraries

- pySS3
- FastText
- TextBrewer
- HuggingFace
- QNLP
- RMDL
- Spacy

### Common applications

- Sentiment analysis.
- Hate speech detection.
- Document indexing in digital libraries.
- **Forum data**: Find out how people feel about various products and features.
- **Restaurant and movie reviews**: What are people raving about? What do people hate?
- **Social media**: What is the sentiment about a hashtag, e.g. for a company, politician, etc?
- **Call center transcripts**: Are callers praising or complaining about particular topics?
- General-purpose categorization in medical, academic, legal, and many other domains.

### Links

- [Text Classification - PyTorch Official](https://pytorch.org/tutorials/beginner/text_sentiment_ngrams_tutorial.html)
- [Building a News Classifier ML App with Streamlit and Python](https://youtu.be/bEOiYF1a6Ak)
- [https://github.com/brightmart/text_classification](https://github.com/brightmart/text_classification)
- [IMDB Sentiment. Tensorflow.](https://www.tensorflow.org/tutorials/keras/text_classification)
- [XLNet Fine-tuning. Toxic Comment Multilabel.](https://towardsdatascience.com/multi-label-text-classification-with-xlnet-b5f5755302df)
- [XLNet Fine-tuning. CoLA.](https://mccormickml.com/2019/09/19/XLNet-fine-tuning/)
- [Classification Demo Notebooks](https://notebooks.quantumstat.com/)
- [Microsoft NLP Recipes](https://github.com/microsoft/nlp-recipes/tree/master/examples/text_classification)
- [Report on Text Classification using CNN, RNN & HAN](https://medium.com/jatana/report-on-text-classification-using-cnn-rnn-han-f0e887214d5f)
- [Implementing a CNN for Text Classification in TensorFlow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
- [prakashpandey9/Text-Classification-Pytorch](https://github.com/prakashpandey9/Text-Classification-Pytorch)
- [Google Colaboratory](https://colab.research.google.com/github/georgianpartners/Multimodal-Toolkit/blob/master/notebooks/text_w_tabular_classification.ipynb#scrollTo=QZR8kqmfRssU)
- [Classify text with BERT | TensorFlow Core](https://www.tensorflow.org/tutorials/text/classify_text_with_bert)
- [Deep Learning Based Text Classification: A Comprehensive Review](https://arxiv.org/pdf/2004.03705v1.pdf)
- [https://stackabuse.com/text-classification-with-bert-tokenizer-and-tf-2-0-in-python/](https://stackabuse.com/text-classification-with-bert-tokenizer-and-tf-2-0-in-python/)
- [https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_text_classification.ipynb](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_text_classification.ipynb)
- [https://blog.valohai.com/machine-learning-pipeline-classifying-reddit-posts](https://blog.valohai.com/machine-learning-pipeline-classifying-reddit-posts)
- [https://www.kdnuggets.com/2018/03/simple-text-classifier-google-colaboratory.html](https://www.kdnuggets.com/2018/03/simple-text-classifier-google-colaboratory.html)
- [https://github.com/AbeerAbuZayed/Quora-Insincere-Questions-Classification](https://github.com/AbeerAbuZayed/Quora-Insincere-Questions-Classification)
- Document Classification: 7 pragmatic approaches for small datasets | Neptune's Blog
- Multi-label Text Classification using BERT - The Mighty Transformer
- [https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.6-classifying-newswires.ipynb](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.6-classifying-newswires.ipynb)
- XLNet Fine-Tuning Tutorial with PyTorch
- Text Classification with XLNet in Action
- AchintyaX/XLNet_Classification_tuning
- [https://github.com/Dkreitzer/Text_ML_Classification_UMN](https://github.com/Dkreitzer/Text_ML_Classification_UMN)
- [https://colab.research.google.com/github/markdaoust/models/blob/basic-text-classification/samples/core/get_started/basic_text_classification.ipynb](https://colab.research.google.com/github/markdaoust/models/blob/basic-text-classification/samples/core/get_started/basic_text_classification.ipynb)
- [https://towardsdatascience.com/how-to-do-text-binary-classification-with-bert-f1348a25d905](https://towardsdatascience.com/how-to-do-text-binary-classification-with-bert-f1348a25d905)
- [https://colab.research.google.com/github/tensorflow/hub/blob/master/docs/tutorials/text_classification_with_tf_hub.ipynb](https://colab.research.google.com/github/tensorflow/hub/blob/master/docs/tutorials/text_classification_with_tf_hub.ipynb)
- [https://github.com/thomas-chauvet/kaggle_toxic_comment_classification](https://github.com/thomas-chauvet/kaggle_toxic_comment_classification)
- [https://github.com/scionoftech/TextClassification-Vectorization-DL](https://github.com/scionoftech/TextClassification-Vectorization-DL)
- [https://github.com/netik1020/Concise-iPython-Notebooks-for-Deep-learning/blob/master/Text_Classification/classification_imdb.ipynb](https://github.com/netik1020/Concise-iPython-Notebooks-for-Deep-learning/blob/master/Text_Classification/classification_imdb.ipynb)
- [https://github.com/getmrinal/ML-Notebook/tree/master/17. textClassificationProject](https://github.com/getmrinal/ML-Notebook/tree/master/17.%20textClassificationProject)
- [https://github.com/mpuig/textclassification](https://github.com/mpuig/textclassification)
- [https://github.com/netik1020/Concise-iPython-Notebooks-for-Deep-learning/blob/master/Text_Classification/self_Attn_on_seperate_fets_of_2embds.ipynb](https://github.com/netik1020/Concise-iPython-Notebooks-for-Deep-learning/blob/master/Text_Classification/self_Attn_on_seperate_fets_of_2embds.ipynb)
- [https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.5-classifying-movie-reviews.ipynb](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.5-classifying-movie-reviews.ipynb)
- sgrvinod/a-PyTorch-Tutorial-to-Text-Classification

## Text Embeddings

### Utilities

#### Averaging word vectors to create sentence vector

In case we already have the vectors for the words in the text, it makes sense to aggregate the word embeddings into a single vector representing the whole text.

![](/img/nlp_vec_avg.png)

This is a great baseline approach chosen by many practitioners, and probably the one we should take first if we already have the word vectors or can easily obtain them.

The most frequent operations for aggregation are:
1. averaging
2. max-pooling

```py
def get_mean_vector(words, word2vec_model):
    ## remove out-of-vocabulary words
    words = [word for word in words if word in word2vec_model.wv.vocab]
    if len(words) >= 1:
        return np.mean(word2vec_model.wv[words], axis=0)
    else:
        return []
```

### Word2vec

#### Training a custom Word2vec CBoW model with Gensim

```py
model_cbow = gensim.models.Word2Vec(window=10, min_count=10, workers=2, size=100)
model_cbow.build_vocab(df.tokens.tolist())
model_cbow.train(df.tokens.tolist(), total_examples=model_cbow.corpus_count, epochs=20)
df['vecs_w2v_cbow'] = df['tokens'].apply(get_mean_vector, word2vec_model=model_cbow)
df.head()
```

#### Training a custom Word2vec SkipGram model with Gensim

```py
model_sg = gensim.models.Word2Vec(window=10, min_count=10, workers=2, size=100, sg=1)
model_sg.build_vocab(df.tokens.tolist())
model_sg.train(df.tokens.tolist(), total_examples=model_sg.corpus_count, epochs=20)
df['vecs_w2v_sg'] = df['tokens'].apply(get_mean_vector, word2vec_model=model_sg)
df.head()
```

### GloVe

Files with the pre-trained vectors Glove can be found in many sites like Kaggle or in the previous link of the Stanford University. We will use the glove.6B.100d.txt file containing the glove vectors trained on the Wikipedia and GigaWord dataset.

First we convert the GloVe file containing the word embeddings to the word2vec format for convenience of use. We can do it using the gensim library, a function called glove2word2vec.

```sh
wget -O glove.6B.zip -q --show-progress https://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
```

```py
## We just need to run this code once, the function glove2word2vec saves the Glove embeddings in the word2vec format 
## that will be loaded in the next section
from gensim.scripts.glove2word2vec import glove2word2vec

## glove_input_file = glove_filename
word2vec_output_file = 'glove.word2vec'
glove2word2vec('glove.6B.100d.txt', word2vec_output_file)
```

So our vocabulary contains 400K words represented by a feature vector of shape 100. Now we can load the Glove embeddings in word2vec format and then analyze some analogies. In this way if we want to use a pre-trained word2vec embeddings we can simply change the filename and reuse all the code below.

```py
## load the Stanford GloVe model
model_glove = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

df['vecs_w2v_glove'] = df['tokens'].apply(get_mean_vector, word2vec_model=model_glove)
df.head()
```

### TF-IDF

The TfidfVectorizer will tokenize documents, learn the vocabulary and inverse document frequency weightings, and allow you to encode new documents. Alternately, if you already have a learned CountVectorizer, you can use it with a TfidfTransformer to just calculate the inverse document frequencies and start encoding documents.

Counts and frequencies can be very useful, but one limitation of these methods is that the vocabulary can become very large.

This, in turn, will require large vectors for encoding documents and impose large requirements on memory and slow down algorithms.

A clever work around is to use a one way hash of words to convert them to integers. The clever part is that no vocabulary is required and you can choose an arbitrary-long fixed length vector. A downside is that the hash is a one-way function so there is no way to convert the encoding back to a word (which may not matter for many supervised learning tasks).

The HashingVectorizer class implements this approach that can be used to consistently hash words, then tokenize and encode documents as needed.

```py
from sklearn.feature_extraction.text import HashingVectorizer

## create the transform
vectorizer = HashingVectorizer(n_features=100)

## encode document
vector = vectorizer.transform(df.clean_text.tolist())

## summarize encoded vector
print(vector.shape)

df['vecs_tfidf'] = list(vector.toarray())
df.head()
```

### BERT

#### Sentence BERT

```py
from sentence_transformers import SentenceTransformer

sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')

df['vecs_bert'] = df['clean_text'].progress_apply(sbert_model.encode)
```

## Text Similarity

![content-concepts-raw-nlp-text-similarity-img](https://user-images.githubusercontent.com/62965911/216823098-80abfe58-bb80-40a1-bced-7e144a61b042.png)

### **Introduction**

- **Definition:** Text similarity has to determine how 'close' two pieces of text are both in surface closeness (lexical similarity) and meaning (semantic similarity)
- **Applications:** Duplicate document detection, text clustering, product recommendations
- **Scope:** No scope decided yet
- **Tools:** Sentence Transformer Library, Universal Sentence Encoder Model (TFHub), Scikit-learn

### **Models**

#### BERT

Use transfer learning to fine-tune a BERT encoder. This encoder will work as a feature extractor. e.g.  the most common version of BERT convert any given text into a numeric vector of length 768 (this vector is also known as contextual embedding).

#### Bag-of-words

Extract features using models like TF-IDF, CountVectorizer.

#### DeepRank

*[DeepRank: A New Deep Architecture for Relevance Ranking in Information Retrieval. arXiv, 2017.](https://arxiv.org/abs/1710.05649)*

#### FAISS

*[Billion-scale similarity search with GPUs. arXiv, 2017.](https://arxiv.org/abs/1702.08734)*

Faiss is a library for efficient similarity search and clustering of dense vectors.

#### Similarity Measures

L1 (Manhatten distance), L2 (Euclidean distance), Hinge Loss for Triplets.

### **Process flow**

Step 1: Collect Text Data

Fetch the raw text dataset into a directory.

Step 2: Encoder Training/Fine-tuning

Download the pre-trained models if available (e.g. BERT model) or train the model from scratch (e.g. TF-IDF model). After training/fine-tuning the model, we will save it as a feature extractor for later use.

Step 3: Text Vectorization

Now, we will use the encoder (prepared in step 2) to encode the text (prepared in step 1). We will save the feature vector of each image as an array in a directory. After processing, we will save these embeddings for later use.

Step 4: Metadata and Indexing

We will assign a unique id to each text document and create dictionaries to locate information of these documents: 1) Document id to document name dictionary, 2) Document id to document feature vector dictionary, and 3) (optional) Document id to metadata product id dictionary. We will also create a Document id to document feature vector indexing. Then we will save these dictionaries and index objects for later use.

Step 5: UAT Testing

Wrap the model inference engine in API for client testing. We will receive a text document from the user, encode it with our text encoder, find TopK similar vectors using Indexing object, and retrieve the text documents (and metadata) using dictionaries. We send these documents (and metadata) back to the user.

Step 6: Deployment

Deploy the model on cloud or edge as per the requirement.

Step 7: Documentation

Prepare the documentation and transfer all assets to the client.

### Use Cases

#### Semantic Relation Estimation

To maintain a level of coherence and similarity among various letters and speeches, a model was built that will help in assessing this document similarity. In approach 1, TF-IDF with Latent semantic indexing was used to extract features and cosine similarity as the distance metric. In approach 2, BERT with PCA was used for feature extraction and 3 distance measures - L1, L2, and cosine, for similarity calculation. Check out [this](https://www.notion.so/Semantic-Similarity-085a0be7e70f4dec99a06c07cca3b12c) notion.

#### Finding Hardware Parts in Warehouse

There are millions of hardware items (e.g. 0.5mm steel wire grade q195) in the warehouse and customer generally asks for items in natural language (e.g. grade195 steel wire with 0.5mm thickness). A text similarity system was built using an ensemble of 3 Bag-of-words based Count vectorizer model with different types of tokenization process and n-gram range. Check out [this](https://www.notion.so/Finding-Hardware-Parts-in-Warehouse-922EE-fa28cf6931a94fa89ad2d4d2183f6bcc) notion.

#### Image + Text Similarity

Use the textual details and images of products, find the exact similar product among different groups. Around 35 GB of retail product images was scraped and used to build the system. Checkout the notion [here](https://www.notion.so/Image-Text-Similarity-fe5130324ae14ab48a30c93444348f4a).

#### Text Recommendation

For the given BRM text, recommend top-5 GAO text. We used universal sentence encoder to encode the text and calculated cosine similarity within group. Then an item-based recommender model was used to find most suitable top-K candidates in GAO based on the interaction history. Check out [this](https://www.notion.so/Text-Recommendation-System-351c57bdb60e40da8531bf19c867314a) notion.


## Topic Modeling

![content-concepts-raw-nlp-topic-modeling-img](https://user-images.githubusercontent.com/62965911/216823108-f57ec710-01e0-4f24-9696-d9c2dcb32cc8.png)

### **Introduction**

- **Definition:** Topic modeling is an unsupervised machine learning technique that’s capable of scanning a set of documents, detecting word and phrase patterns within them, and automatically clustering word groups and similar expressions that best characterize a set of documents.
- **Applications:** Identify emerging themes and topics
- **Scope:** No scope decided yet
- **Tools:** Gensim

### Models

#### LSA

The core idea is to take a matrix of what we have — documents and terms — and decompose it into a separate document-topic matrix and a topic-term matrix.

#### Process flow

Step 1: Collect Text Data

Fetch from database, scrap from the internet or use public datasets. Setup the database connection and fetch the data into python environment.

Step 2: Data Preparation

Explore the data, validate it and create preprocessing strategy. Clean the data and make it ready for modeling.

Step 3: Model Building

Start the training process and track the progress and experiments. Validate the final set of models and select/assemble the final model.

Step 4: UAT Testing

Wrap the model inference engine in API for client testing

Step 5: Deployment

Deploy the model on cloud or edge as per the requirement

Step 6: Documentation

Prepare the documentation and transfer all assets to the client

### Use Cases

#### Identify Themes and Emerging Issues in ServiceNow Incident Tickets

Extracted key phrases from the incident ticket descriptions and trained an LSA topic model on these phrases to identify emerging themes and incident topics. This enabled a proactive approach to manage and contain the issues and thus increasing CSAT. Check out [this](https://www.notion.so/ServiceNow-Advanced-Analytics-1D5F3-f35e7f17377544c8b11cdf624e5da800) notion.

#### IT Support Ticket Management

In Helpdesk, almost 30–40% of incident tickets are not routed to the right team and the tickets keep roaming around and around and by the time it reaches the right team, the issue might have widespread and reached the top management inviting a lot of trouble. To solve this issue, we built a system with 6 deliverables: Key Phrase Analysis, Topic Modeling, Ticket Classification, Trend, Seasonality and Outlier Analysis, PowerBI Dashboard to visually represent the KPIs and dividing tickets into standard vs. non-standard template responses. Check out [this](https://www.notion.so/ESMCafe-IT-Support-Ticket-Management-69965830d39d486194f9a2f1222a81d8) notion.


## Chatbot

![content-concepts-raw-nlp-chatbot-img](https://user-images.githubusercontent.com/62965911/216823087-2286659a-d2fd-4b8c-a6a2-f4bf512f2e74.png)

### **Introduction**

- **Definition:** This product will automate tasks and handle conversations with the user.
- **Applications:** Customer support, Product suggestion, Interactive FAQ, Form filling, Question Answering
- **Scope:** Chat and Voice Support, FAQ, Knowledge-based and Contextual bot
- **Tools:** DialogFlow, RASA, DeepPavlov, Alexa Skill, HuggingFace, ParlAI

### **Models**

#### RASA Chatbot

RASA supports contextual conversational AI. It provided an integrated framework for Natural language understanding, dialogue generation and management. It also supprots multiple endpoints (e.g. Facebook messenger, WhatsApp) for easy deployment.

#### DialogFlow Chatbot

It is an API to easily create and deploy chatbots. It also supports Voice interaction via Google cloud Voice API.

#### Alexa Skill

This API enable us to create an alexa skill that can be used via alexa services. This also supports voice interaction via Alexa Voice API.

### **Process flow**

Step 1: Create As-Is Process

Create the current process

Step 2: Propose To-Be Process

Creeate the to-be process in which chatbot will handle the conversations in collaboration with human in the loop or on fully automated basis

Step 3: Collect the training data

Collect or create the training data and example conversations for training the chatbot

Step 6: Chatbot Training

Train the chatbot model

Step 9: UAT Testing

Wrap the model inference engine in API for client testing

Step 10: Deployment

Deploy the model on cloud or edge as per the requirement

Step 11: Documentation

Prepare the documentation and transfer all assets to the client

### **Use Cases**

#### RASA Chatbot

Categorization of services and selected 4 most usable services for automation process. Development of a text-based chatbot application for this automation. RASA framework (python) was selected for implementation of this chatbot. Check out [this](https://www.notion.so/Insurance-Chatbot-d39fb9b575f5470d8be08cb7f2a12994) notion.

#### Insurance Voicebot

Automate the low-skill contact center services with the help of Voicebot AI technology. Context - Insurance Contact Centre, Role - A virtual customer care representative, Skills – Claim status, Language – English (US), Technology – Voice-enabled Goal-oriented Conversational AI Agents (Voicebots). Modules - Dialogflow Voicebot, Alexa Skill Voicebot, Rasa with 3rd-party Voice API, Rasa powered Alexa skill, Rasa powered Google assistant, Rasa voicebot with Mozilla tools, and DeepPavlov Voicebot. Check out [this](https://www.notion.so/Insurance-Voicebot-0F2A3-b8eaf980a04840a6945a076d878c107a) notion.

#### Wellness Tracker

A bot that logs daily wellness data to a spreadsheet (using the Airtable API), to help the user keep track of their health goals. Connect the assistant to a messaging channel—Twilio—so users can talk to the assistant via text message and Whatsapp. Check out [this](https://www.notion.so/Wellness-Tracker-Chatbot-c867f589d0f14ec98a7c0cd9e58fec2a) notion.

#### RASA Chatbot Experiments

Experiment with 4 chatbots in RASA: Financial Bot - A chatbot demonstrating how to build AI assistants for financial services and banking, Movie Bot - A bot to book movie tickets, Cricket Bot - A bot that will bring the live info about IPL cricket match as per user query, and Pokedex - This is a demonstration of a digital assistant that can answer questions about pokemon. Check out [this](https://www.notion.so/RASA-a698cb020e9e451f9200437586f1444e) notion.

## Named Entity Recognition

![content-concepts-raw-nlp-named-entity-recognition-img](https://user-images.githubusercontent.com/62965911/216823095-cb1f05c0-8d3e-49f5-888c-b3972bd741de.png)

### **Introduction**

- **Definition:** NER models classify each word/phrase in the document into a pre-defined category. In other words, these models identify named entities (classes/labels) in the given text document
- **Applications:** Opinion mining, Affinity towards brands
- **Scope:** No scope decided yet
- **Tools:** Doccano, Flair, Spacy, HuggingFace Transformer Library

### **Models**

#### Flair-NER

*[Pooled Contextualized Embeddings for Named Entity Recognition. ACL, 2019.](https://www.aclweb.org/anthology/N19-1078/)*

Contextual string embeddings are a recent type of contextualized word embedding that were shown to yield state-of-the-art results when utilized in a range of sequence labeling tasks. This model achieves an F1 score of 93.2 on the CoNLL-03 dataset.

#### Spacy-NER

*[Incremental parsing with bloom embeddings and residual CNNs.](https://spacy.io/universe/project/video-spacys-ner-model)*

spaCy v2.0's Named Entity Recognition system features a sophisticated word embedding strategy using subword features and "Bloom" embeddings, a deep convolutional neural network with residual connections, and a novel transition-based approach to named entity parsing.

#### Transformer-NER

Fine-tuning of transformer based models like BERT, Roberta and Electra.

### **Process flow**

Step 1: Collect Text Data

Fetch the raw text dataset into a directory.

Step 2: Create Labels

Use open-source tools like Doccano or paid tools like Prodigy to annotate the entities.

Step 3: Model Training & Validation

Train the NER model and validate it.

Step 4: UAT Testing

Wrap the model inference engine in API for client testing. We will receive a text document from the user, encode it with our text encoder, find TopK similar vectors using Indexing object, and retrieve the text documents (and metadata) using dictionaries. We send these documents (and metadata) back to the user.

Step 5: Deployment

Deploy the model on cloud or edge as per the requirement.

Step 6: Documentation

Prepare the documentation and transfer all assets to the client.

### **Use Cases**

#### Name and Address Parsing

Parse names (person [first, middle and last name], household or corporation) and address (street, city, state, country, zip) from the given text. We used Doccano for annotation and trained a Flair NER model on GPU. Check out this [notion](https://www.notion.so/Name-Address-Parsing-209653cc37d2413f9b6e902712338ed4).

#### NER Methods Experiment

Data is extracted from GMB(Groningen Meaning Bank) corpus and annotated using BIO scheme. 10 different NER models were trained and compared on this dataset. Frequency based tagging model was taken as the baseline. Classification, CRF, LSTM, LSTM-CRF, Char-LSTM, Residual-LSTM-ELMo, BERT tagger, Spacy tagger and an interpretable tagger with keras and LIME were trained. Checkout [this](https://www.notion.so/Multiple-methods-NER-319c0e2cc2b74008a931b849377557d1) notion.

## Text Summarization

![content-concepts-raw-nlp-text-summarization-untitled](https://user-images.githubusercontent.com/62965911/216823104-f5413836-8502-4cc1-9924-9b391e1677c6.png)

Automatic Text Summarization gained attention as early as the 1950’s. A [research paper](http://courses.ischool.berkeley.edu/i256/f06/papers/luhn58.pdf), published by Hans Peter Luhn in the late 1950s, titled “The automatic creation of literature abstracts”, used features such as word frequency and phrase frequency to extract important sentences from the text for summarization purposes.

Another important [research](http://courses.ischool.berkeley.edu/i256/f06/papers/edmonson69.pdf), done by Harold P Edmundson in the late 1960’s, used methods like the presence of cue words, words used in the title appearing in the text, and the location of sentences, to extract significant sentences for text summarization. Since then, many important and exciting studies have been published to address the challenge of automatic text summarization.

Text summarization can broadly be divided into two categories — **Extractive Summarization** and **Abstractive Summarization**.

1. **Extractive Summarization:** These methods rely on extracting several parts, such as phrases and sentences, from a piece of text and stack them together to create a summary. Therefore, identifying the right sentences for summarization is of utmost importance in an extractive method.
2. **Abstractive Summarization:** These methods use advanced NLP techniques to generate an entirely new summary. Some parts of this summary may not even appear in the original text.

### Introduction

- **Definition:** *To take the appropriate action, we need the latest information, but on the contrary, the amount of information is more and more growing. Making an automatic & accurate summaries feature will helps us to understand the topics and shorten the time to do it.*
- **Applications:** News Summarization, Social media Summarization, Entity timelines, Storylines of event, Domain specific summaries, Sentence Compression, Event understanding, Summarization of user-generated content
- **Scope:** Extractive and Abstractive summary
  - Single document summarization: summary = summarize(document)
  - Multi-document summarization: summary = summarize(document_1, document_2, ...)
  - Query focused summarization: summary = summarize(document, query)
  - Update summarization: summary = summarize(document, previous_document_or_summary)
- **Tools:** HuggingFace Transformer Library

### Scheduled sampling

In the inference (testing) phase, the model only depends on the previous step, which means that it totally depends on itself. The problem actually arises when the model results in a bad output in (t-1) (i.e. the previous time step results in a bad output). This would actually affect all the coming sequences. It would lead the model to an entirely different state space from where it has seen and trained on in the training phase, so it simply won’t be able to know what to do. A solution to this problem that has been suggested by [bengio et ai](https://arxiv.org/abs/1506.03099) from google research, was to gradually change the reliance of the model from being totally dependent on the ground truth being supplied to it to depending on itself (i.e. depend on only its previous tokens generated from previous time steps in the decoder). The concept of making the learning path difficult through time (i.e. making the model depends on only itself) is called curriculum learning. Their technique to implement this was truly genius. They call it ‘**scheduled sampling’.**

![content-concepts-raw-nlp-text-summarization-image_(4)](https://user-images.githubusercontent.com/62965911/216823101-094f1ba6-cb4f-477d-b968-ccaa83c2cb0a.png)

Landscape of seq2seq models for neural abstractive text summarization

### Models

#### ProphetNet

*[ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training. arXiv, 2020.](https://arxiv.org/abs/2001.04063)*

#### PEGASUS

*[PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization. arXiv, 2019.](https://arxiv.org/abs/1912.08777)*

#### BERTSum

*[Fine-tune BERT for Extractive Summarization. arXiv, 2019.](https://arxiv.org/pdf/1903.10318.pdf)*

#### Seq2Seq PointerGenerator

*[Get To The Point: Summarization with Pointer-Generator Networks. arXiv, 2017.](https://arxiv.org/abs/1704.04368v2)*

### Process flow

Step 1: Collect Text Data

Fetch the raw text dataset into a directory.

Step 2: Create Labels

Step 3: Model Training & Validation

Step 4: UAT Testing

Wrap the model inference engine in API for client testing. We will receive a text document from the user, encode it with our text encoder, find TopK similar vectors using Indexing object, and retrieve the text documents (and metadata) using dictionaries. We send these documents (and metadata) back to the user.

Step 5: Deployment

Deploy the model on cloud or edge as per the requirement.

Step 6: Documentation

Prepare the documentation and transfer all assets to the client.

### Use Cases

#### Enron Email Summarization

Email overload can be a difficult problem to manage for both work and personal email inboxes. With the average office worker receiving between 40 to 90 emails a day, it has become difficult to extract the most important information in an optimal amount of time. A system that can create concise and coherent summaries of all emails received within a timeframe can reclaim a large amount of time. Check out [this](https://www.notion.so/Enron-Email-Summarization-d137f618b4c5445fb595714fdc30c68d) notion.

#### PDF Summarization over mail

Built a system that will receive a pdf over outlook mail and create a word cloud for this pdf. Then, send this word cloud back as an attachment to that email. Check out [this](https://www.notion.so/PDF-to-Wordcloud-via-Mail-b7ae38d0e95e439eb68194b66bdcb889) notion.

#### BART Text Summarization

Document text summarization using the BART transformer model and visual API using the Plotly Dash app. Check out [this](https://www.notion.so/BART-Text-Summarization-on-Plotly-Dash-f023de73b80c43bf9856a5ecbf24398b) notion.

#### Transformers Summarization Experiment

Experiment with various transformers for text summarization using HuggingFace library. Summarization of 4 books. Check out [this](https://www.notion.so/HuggingFace-Transformers-based-Summarization-082d7af9c97944188f735c761cd27b9b) notion.

#### CNN-DailyMail and InShorts News Summarization

Check out [this](https://www.notion.so/CNN-DailyMail-News-Summarization-f831bc810195478985aa6356bd43465a) notion for CNN-DailyMail and [this](https://www.notion.so/InShorts-News-Summarization-daeb6fe3aa924a24a88657937ab43145) one for InShorts.

#### Transformers Summarization Experiment

Experiment with various transformers for text summarization using HuggingFace library. Summarization of 4 books. Check out [this](https://www.notion.so/HuggingFace-Transformers-based-Summarization-082d7af9c97944188f735c761cd27b9b) notion.

#### Covid-19 article summarization

Used BERT and GPT-2 for article summarization related to covid-19. Check out [this](https://www.notion.so/Text-Summarization-of-Articles-ec756ff596614f29b6896927e87609b1) notion.

### Common Applications

- News Summarization: The summarization systems leverage the power of multi-document
  summarization techniques in order to summarize the news coming from various sources.
  It generates a compact summary that is informative and non-redundant. Methods
  used can be extractive or abstractive. For example, the ’Inshort’ application generates a sixty-word summary of news articles.
- Social media Summarization: deals with the summarization of social media text such as:
  tweets, blogs, community forums, etc. These summarization systems are built keeping in
  mind the needs of the user and are dependent on the genre of social media text. Tweets
  summarization system will be different from blog summarization systems as tweets have
  a short text (140 characters) and are often noisy. While the blog has considerably longer
  length text with a different writing style.
- Entity timelines: The system generates the summary of most salient events related to
  an entity within a given timeline. The news collections from various news sources are
  collected over a period of time. Each of these news collections define a main event. For
  a given entity, these news collection are identified and ranked in order of importance.
  Most salient sentences with respect to the given entity is selected from each of these news
  cluster to finally generate an entity timeline.
- Storylines of event: deals with identifying and summarization of events that leads
  to event of interest. It helps in providing background information about an event and
  structured timeline for an entity. The news collections from various news sources are
  collected over a period of time. Each of these news collections define a main even. A
  graph of events (news collection) is defined using similarity, then heaviest path ending in
  a given event is identified and finally, the events on this path related to salient entities in
  target event are summarized to obtain storylines of the event.
- Domain specific summaries: Summarization systems are often used in generating
  domain specific summaries. These systems are designed in accordance with the needs of
  the user for a specific domain. For example: legal document summarization deals with
  generating summary out of a legal/law documents, medical report summarization has aim
  of generating a summary form a patient report history such that it includes all important
  clinical events in order of timeline.
- Sentence Compression: generates a short version of a longer sentence. The system
  is trained using a parallel corpus containing headlines of news articles and first sentence
  of the same article. The headline is assumed to be shorter version of the first sentence.
  Recent works based on abstractive neural network approaches has proven to generate high
  quality compressed sentences.
- Event understanding: is understanding the way events are referred to in the text and
  representing these event mentioning text in predicate argument structure. For example:
  Michael marries Sara is represented as [actor] marries [actor]. It is very helpful for semiautomatically updation of knowledge graphs and also for the task of generating headlines
  (abstractive summarization).
- Summarization of usergenerated content: deals with summarizing user generated
  contents like youtube comments, reviews of products, opinions etc. compact version of
  reviews and comment are very helpful in identifying overall sentiment of mass towards
  a particular product or topic. Which are often used by the consumers as well as the
  platform itself in recommending products.

### Variations

- Single document summarization: *summary = summarize(document)*
- Multi-document summarization: *summary = summarize(document_1, document_2, ...)*
- Query focused summarization: *summary = summarize(document, query)*
- Update summarization: *summary = summarize(document, previous_document_or_summary)*

Basically, we can regard the "summarization" as the "function" its input is document and output is summary. And its input & output type helps us to categorize the multiple summarization tasks.

- Single document summarization
  - *summary = summarize(document)*
- Multi-document summarization
  - *summary = summarize(document_1, document_2, ...)*

We can take the query to add the viewpoint of summarization.

- Query focused summarization
  - *summary = summarize(document, query)*

This type of summarization is called "Query focused summarization" on the contrary to the "Generic summarization". Especially, a type that set the viewpoint to the "difference" (update) is called "Update summarization".

- Update summarization
  - *summary = summarize(document, previous_document_or_summary)*

And the *"summary"* itself has some variety.

- Indicative summary
  - It looks like a summary of the book. This summary describes what kinds of the story, but not tell all of the stories especially its ends (so indicative summary has only partial information).
- Informative summary
  - In contrast to the indicative summary, the informative summary includes full information of the document.
- Keyword summary
  - Not the text, but the words or phrases from the input document.
- Headline summary
  - Only one line summary.

### Summary Variations

- Indicative summary: It looks like a summary of the book. This summary describes what kinds of the story, but not tell all of the stories especially its ends (so indicative summary has only partial information).
- Informative summary: In contrast to the indicative summary, the informative summary includes full information of the document.
- Keyword summary: Not the text, but the words or phrases from the input document.
- Headline summary: Only one line summary.

### Seq2Seq

![content-concepts-raw-nlp-text-summarization-untitled-1](https://user-images.githubusercontent.com/62965911/216823103-14b70635-485d-43fa-b08c-b2dbb99dff04.png)

- Seq2seq - mainly bi-LSTM for encoder and attention mechanism for decoder network

### Pointer Generator

![content-concepts-raw-nlp-text-summarization-image_(3)](https://user-images.githubusercontent.com/62965911/216823099-408a7f2f-f929-402d-9110-4e90f545b665.png)

![https://miro.medium.com/max/1400/0*vJgFcKRJpdN1sO2Z.png](https://miro.medium.com/max/1400/0*vJgFcKRJpdN1sO2Z.png)

Researchers found 2 main problems with the seq2seq model, as discussed in this truly [amazing blog](http://www.abigailsee.com/2017/04/16/taming-rnns-for-better-summarization.html), which is 1) the inability of the network to copy facts and 2) repetition of words. The pointer generator network (with coverage mechanism) tried to address these problems.

### Experiments

[theamrzaki/text_summurization_abstractive_methods](https://github.com/theamrzaki/text_summurization_abstractive_methods)

[dongjun-Lee/text-summarization-tensorflow](https://github.com/dongjun-Lee/text-summarization-tensorflow)

[nikhilcss97/Text-Summarization](https://github.com/nikhilcss97/Text-Summarization)

[glopasso/text-summarization](https://github.com/glopasso/text-summarization)

[How to Summarize Amazon Reviews with Tensorflow](https://www.dlology.com/blog/tutorial-summarizing-text-with-amazon-reviews/)

[pytorch/fairseq](https://github.com/pytorch/fairseq)

[tshi04/LeafNATS](https://github.com/tshi04/LeafNATS)

- [Text summarisation with BART &amp; T5 using HuggingFace](https://colab.research.google.com/drive/1iAIFX1QQiFm1F01vMmnAgFh4oH1H-K8W)
- [TextRank, Summy and BERT Summarizer](https://colab.research.google.com/drive/1PlWjOQ9IV-MAtoZuAFfgccLKg_Uu-ufo#scrollTo=m85bgroRzV3_)
- [TED Talk Tag Generator and Summarizer](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/755dfc1a-4752-44a5-bc21-49aa5c80adb7/TED_Talk_Tag_Generator_and_Summarizer___by_Qi_Haodi___Jul_2020___Medium.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201014T060921Z&X-Amz-Expires=86400&X-Amz-Signature=82cab92ef127ef9a6122b243ef2f050e3db4282f524c9eaea9f8307af8699624&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22TED%2520Talk%2520Tag%2520Generator%2520and%2520Summarizer%2520_%2520by%2520Qi%2520Haodi%2520_%2520Jul%252C%25202020%2520_%2520Medium.html%22)

### Benchmark datasets

#### BigPatent

[](https://arxiv.org/pdf/1906.03741.pdf)

Most existing text summarization datasets are compiled from the news domain, where summaries have a flattened discourse structure. In such datasets, summary-worthy content often appears in the beginning of input articles. Moreover, large segments from input articles are present verbatim in their respective summaries. These issues impede the learning and evaluation of systems that can understand an article’s global content structure as well as produce abstractive summaries with high compression ratio. In this work, we present a novel dataset, BIGPATENT, consisting of 1.3 million records of U.S. patent documents along with human written abstractive summaries.

Compared to existing summarization datasets, BigPatent has the following properties:

1. summaries contain richer discourse structure with more recurring entities,
2. salient content is evenly distributed in the input, and
3. lesser and shorter extractive fragments present in the summaries.

We train and evaluate baselines and popular learning models on BIGPATENT to shed light on new challenges and motivate future directions for summarization research.

#### CNN and DailyMail

[DMQA](https://cs.nyu.edu/~kcho/DMQA/)

CNN daily mail dataset consists of long news articles(an average of ~800 words). It consists of both articles and summaries of those articles. Some of the articles have multi line summaries also. We have used this dataset in our Pointer Generator model.

CNN dataset contains the documents from the news articles of CNN. There are approximately 90k documents/stories. DM dataset contains the documents from the news articles of Daily Mail. There are approximately 197k documents/stories. OTHR contains a few thousands stories scraped from 4 news websites.

- CNN/DM - the news body is used as the input for our model , while the header would be used as the summary target output.
- Data can be acquired from this [gdrive](https://drive.google.com/drive/folders/1Izsbg_p1s52dFNh8NmSG5jmDtRgHcLUN).

#### Amazon Fine Food Reviews

[https://www.kaggle.com/snap/amazon-fine-food-reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews)

#### DUC-2014

- [DUC-2014 dataset](http://duc.nist.gov/data.html) that involves generating approximately 14-word summaries for 500 news articles. The data for this task consists of 500 news articles from the New York Times and Associated Press Wire services each paired with 4 different human-generated reference summaries (not actually headlines), capped at 75 bytes.

#### Gigaword

[Annotated English Gigaword](https://catalog.ldc.upenn.edu/LDC2012T21)

It is popularly known as GIGAWORLD dataset and contains nearly ten million documents (over four billion words) of the original English Gigaword Fifth Edition. It consists of articles and their headlines. We have used this dataset to train our Abstractive summarization model.

#### Cornell Newsroom

[Cornell Newsroom Summarization Dataset](http://lil.nlp.cornell.edu/newsroom/)

#### Opinosis

[Opinosis Dataset - Topic related review sentences | Kavita Ganesan](http://kavita-ganesan.com/opinosis-opinion-dataset/#.Xs0trf8za01)

This dataset contains sentences extracted from user reviews on a given topic. Example topics are “performance of Toyota Camry” and “sound quality of ipod nano”, etc. The reviews were obtained from various sources — Tripadvisor (hotels), Edmunds.com (cars) and amazon.com (various electronics).Each article in the dataset has 5 manually written “gold” summaries. This dataset was used to score the results of the abstractive summarization model.

### Evaluation metrics

#### ROGUE

[](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/was2004.pdf)

[](https://arxiv.org/pdf/1803.01937v1.pdf)

Rouge-N is a word N-gram count that matche between the model and the gold summary. It is similart to the "recall" because it evaluates the covering rate of gold summary, and not consider the not included n-gram in it.

ROUGE-1 and ROUGE-2 is usually used. The ROUGE-1 means word base, so its order is not regarded. So "apple pen" and "pen apple" is same ROUGE-1 score. But if ROUGE-2, "apple pen" becomes single entity so "apple pen" and "pen apple" does not match. If you increase the ROUGE-"N" count, finally evaluates completely match or not.

#### BLEU

[](https://www.aclweb.org/anthology/P02-1040.pdf)

BLEU is a modified form of "precision", that used in machine translation evaluation usually. BLEU is basically calculated on the n-gram co-occerance between the generated summary and the gold (You don't need to specify the "n" unlike ROUGE).

### Library

[chakki-works/sumeval](https://github.com/chakki-works/sumeval)

### Awesome List

[mathsyouth/awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization)

### References

[Neural Abstractive Text Summarization with Sequence-to-Sequence Models: A Survey](https://arxiv.org/abs/1812.02303v3)

[A Survey on Neural Network-Based Summarization Methods](https://arxiv.org/abs/1804.04589)

[Papers with Code - A Neural Attention Model for Abstractive Sentence Summarization](https://paperswithcode.com/paper/a-neural-attention-model-for-abstractive)

[Text summarization with TensorFlow](https://ai.googleblog.com/2016/08/text-summarization-with-tensorflow.html)

[Papers with Code - Get To The Point: Summarization with Pointer-Generator Networks](https://paperswithcode.com/paper/get-to-the-point-summarization-with-pointer)

[Abstractive Text Summarization Using Sequence-to-Sequence RNNs and Beyond](https://arxiv.org/abs/1602.06023)

[A Deep Reinforced Model for Abstractive Summarization](https://arxiv.org/abs/1705.04304)

[Actor-Critic based Training Framework for Abstractive Summarization](https://arxiv.org/abs/1803.11070v1)

[Papers with Code - Unified Language Model Pre-training for Natural Language Understanding and Generation](https://paperswithcode.com/paper/unified-language-model-pre-training-for)

[Papers with Code - MASS: Masked Sequence to Sequence Pre-training for Language Generation](https://paperswithcode.com/paper/mass-masked-sequence-to-sequence-pre-training)

[Papers with Code - Deep Reinforcement Learning For Sequence to Sequence Models](https://paperswithcode.com/paper/deep-reinforcement-learning-for-sequence-to)

[Papers with Code - Text Summarization with Pretrained Encoders](https://paperswithcode.com/paper/text-summarization-with-pretrained-encoders)

[Papers with Code - ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training](https://paperswithcode.com/paper/prophetnet-predicting-future-n-gram-for)

[](https://arxiv.org/pdf/1911.02247v2.pdf)

- [Taming Recurrent Neural Networks for Better Summarization](http://www.abigailsee.com/2017/04/16/taming-rnns-for-better-summarization.html) [⭐]
- [Awesome Text Summarization](https://github.com/mathsyouth/awesome-text-summarization)
- [Text summarization with TensorFlow, Google AI Blog 2016](https://ai.googleblog.com/2016/08/text-summarization-with-tensorflow.html)

[sourcecode369/deep-natural-language-processing](https://github.com/sourcecode369/deep-natural-language-processing/blob/master/text%20summarization/summarization.md)


## Text Generation

Natural language generation (NLG) can actually tell a story – exactly like that of a human analyst – by writing the sentences and paragraphs for you. It can also summarize reports. 

*“Conversations with systems that have access to data about our world will allow us to understand the status of our jobs, our businesses, our health, our homes, our families, our devices, and our neighborhoods — all through the power of NLG. It will be the difference between getting a report and having a conversation. The information is the same but the interaction will be more natural"*.  **

### Algorithms

#### Text Generation with Markov Chain

Markov chains are a stochastic process that are used to describe the next event in a sequence given the previous event only. In our case the state will be the previous word (unigram) or 2 words (bigram) or 3 (trigram). These are more generally known as ngrams since we will be using the last n words to generate the next possible word in the sequence. A Markov chain usually picks the next state via a probabilistic weighting but in our case that would just create text that would be too deterministic in structure and word choice. You could play with the weighting of the probabilities, but really having a random choice helps make the generated text feel original.

**Corpus**: The dog jumped over the moon. The dog is funny.

**Language model:**

```
(The, dog)     -> [jumped, is]
(dog, jumped)  -> [over]
(jumped, over) -> [the]
(over, the)    -> [moon]
(the, moon)    -> [#END#]
(dog, is)      -> [funny]
(is, funny)    -> [#END#]
```

```python
import random
import string

class MarkovModel:

    def __init__(self):
        self.model = None

    def learn(self,tokens,n=2):
        model = {}

        for i in range(0,len(tokens)-n):
            gram = tuple(tokens[i:i+n])
            token = tokens[i+n]

            if gram in model:
                model[gram].append(token)
            else:
                model[gram] = [token]

        final_gram = tuple(tokens[len(tokens) - n:])
        if final_gram in model:
            model[final_gram].append(None)
        else:
            model[final_gram] = [None]
        self.model = model
        return model

    def generate(self,n=2,seed=None, max_tokens=100):
        if seed == None:
            seed = random.choice(self.model.keys())

        output = list(seed)
        output[0] = output[0].capitalize()
        current = seed

        for i in range(n, max_tokens):
            ## get next possible set of words from the seed word
            if current in self.model:
                possible_transitions = self.model[current]
                choice = random.choice(possible_transitions)
                if choice is None: break

                ## check if choice is period and if so append to previous element
                if choice == '.':
                    output[-1] = output[-1] + choice
                else:
                    output.append(choice)
                current = tuple(output[-n:])
            else:
                ## should return ending punctuation of some sort
                if current not in string.punctuation:
                    output.append('.')
        return output
```

- [Natural Language Generation Part 1: Back to Basics](https://towardsdatascience.com/natural-language-generation-part-1-back-to-basics-2f0b2654624f)
- [MaskGAN](https://paperswithcode.com/paper/maskgan-better-text-generation-via-filling-in) - Fill in the blank technique
- RankGAN
- LeakGAN
- [BART](https://paperswithcode.com/paper/bart-denoising-sequence-to-sequence-pre)
- [CTRL: A Conditional Transformer Language Model for Controllable Generation](https://paperswithcode.com/paper/ctrl-a-conditional-transformer-language-model)
- [Neural Assistant: Joint Action Prediction, Response Generation, and Latent Knowledge Reasoning](https://paperswithcode.com/paper/neural-assistant-joint-action-prediction)

### Important Papers

The survey: Text generation models in deep learning [[2020](https://reader.elsevier.com/reader/sd/pii/S1319157820303360?token=AF608DFD534B46032B10D2F3DFD1B74CE0D3DC436E536660C856B15C296B929524171B9064D8772BA4762DCC57DAA69E)]

Survey of the State of the Art in Natural Language Generation: Core tasks, applications [[2017](https://arxiv.org/pdf/1703.09902.pdf)]

Neural Text Generation: A Practical Guide [[2017](https://arxiv.org/pdf/1711.09534.pdf)]

Neural Text Generation: Past, Present and Beyond [[2018](https://arxiv.org/pdf/1803.07133.pdf)]

### Experiments

- [Do Massively Pretrained Language Models Make Better Storytellers?](https://github.com/abisee/story-generation-eval)
- [Build your own WhatsApp text generator](https://mc.ai/build-your-own-whatsapp-text-generator-and-learn-all-about-language-models/)
- [A beginner’s guide to training and generating text using GPT2](https://medium.com/@stasinopoulos.dimitrios/a-beginners-guide-to-training-and-generating-text-using-gpt2-c2f2e1fbd10a)
- [How to Build a Twitter Text-Generating AI Bot With GPT-2](https://minimaxir.com/2020/01/twitter-gpt2-bot/)
- [Tensorflow guide on Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation)
- [Generating Text with TensorFlow 2.0](https://towardsdatascience.com/generating-text-with-tensorflow-2-0-6a65c7bdc568)
- [Accelerated Text](https://github.com/tokenmill/accelerated-text)
- [Texygen: A text generation benchmarking platform](https://github.com/geek-ai/Texygen)
- [How to create a poet / writer using Deep Learning (Text Generation using Python)](https://www.analyticsvidhya.com/blog/2018/03/text-generation-using-python-nlp/)
- [Text generation with LSTM](https://nbviewer.jupyter.org/github/fchollet/deep-learning-with-python-notebooks/blob/master/8.1-text-generation-with-lstm.ipynb)
- [Title Generation using Recurrent Neural Networks](https://github.com/AngusTheMack/title-generator)
- [Pun Generation with Surprise](https://arxiv.org/pdf/1904.06828.pdf)
- [Neural text generation: How to generate text using conditional language models](https://medium.com/phrasee/neural-text-generation-generating-text-using-conditional-language-models-a37b69c7cd4b)
- [Encode, Tag and Realize: A Controllable and Efficient Approach for Text Generation](https://ai.googleblog.com/2020/01/encode-tag-and-realize-controllable-and.html)

### Text Generation with char-RNNs

[The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

- [How to Quickly Train a Text-Generating Neural Network for Free](https://minimaxir.com/2018/05/text-neural-networks/)
- [Natural Language Generation using LSTM-Keras](https://github.com/shashank-bhatt-07/Natural-Language-Generation-using-LSTM-Keras)

### References

[BoredHumans.com - Fun AI Programs You Can Use Online](https://boredhumans.com/)

[eaglenlp/Text-Generation](https://github.com/eaglenlp/Text-Generation)

[tokenmill/awesome-nlg](https://github.com/tokenmill/awesome-nlg)

[ChenChengKuan/awesome-text-generation](https://github.com/ChenChengKuan/awesome-text-generation)

[Tianwei-She/awesome-natural-language-generation](https://github.com/Tianwei-She/awesome-natural-language-generation)

[Papers with Code - Text Generation](https://paperswithcode.com/task/text-generation)

[Eulring/Text-Generation-Papers](https://github.com/Eulring/Text-Generation-Papers)

[Arxiv Sanity Preserver](http://www.arxiv-sanity.com/search?q=natural+language+generation)

---

#### Decoding techniques - Greedy search, Beam search, Top-K sampling and Top-p sampling with Transformer

[How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)

[Google Colaboratory](https://colab.research.google.com/drive/1Wf9HT2JjW-g_7UKLk2jmlN_K3SVkL9-i#scrollTo=lzaVvvIXMGOx)

#### Controlling Text Generation with Plug and Play Language Models (PPLM)

PPLM lets users combine small attribute models with an LM to steer its generation. Attribute model scan be 100,000 times smaller than the LM and still be effective insteering it, like a mouse sitting atop our wooly mammoth friend and telling it where to go.The mouse tells the mammoth where to go using gradients.

[Controlling Text Generation with Plug and Play Language Models](https://eng.uber.com/pplm/)

[uber-research/PPLM](https://github.com/uber-research/PPLM)

[Plug and Play Language Models: A Simple Approach to Controlled Text Generation](https://paperswithcode.com/paper/plug-and-play-language-models-a-simple)

[Google Colaboratory](https://colab.research.google.com/drive/1DXBs1w_yyBbXsfRnFW98k_iZ3AYHhITS#scrollTo=fN-oIcZNo4xD)

#### GPT-2 Fine Tuning

- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)

#### Autoregressive Language Generation

It based on the assumption that the probability distribution of a word sequence can be decomposed into the product of conditional next word distributions. The way these models actually work is that after each token is produced, that token is added to the sequence of inputs. And that new sequence becomes the input to the model in its next step.

#### **Word-Level Generation vs Character-Level Generation**

In general, word-level language models tend to display higher accuracy than character-level language models. This is because they can form shorter representations of sentences and preserve the context between words easier than character-level language models. However, large corpora are needed to sufficiently train word-level language models, and one-hot encoding isn't very feasible for word-level models. In contrast, character-level language models are often quicker to train, requiring less memory and having faster inference than word-based models. This is because the "vocabulary" (the number of training features) for the model is likely to be much smaller overall, limited to hundreds of characters rather than hundreds of thousands of words.

## Transformers

The old, obsolete, 1980 architecture of Recurrent Neural Networks(RNNs) including the LSTMs were simply not producing good results anymore. In less than two years, transformer models wiped RNNs off the map and even outperformed human baselines for many tasks.

Here’s what the transformer block looks like in PyTorch:

```python
class TransformerBlock(nn.Module):
  def __init__(self, k, heads):
    super().__init__()

    self.attention = SelfAttention(k, heads=heads)

    self.norm1 = nn.LayerNorm(k)
    self.norm2 = nn.LayerNorm(k)

    self.ff = nn.Sequential(
      nn.Linear(k, 4 * k),
      nn.ReLU(),
      nn.Linear(4 * k, k))

  def forward(self, x):
    attended = self.attention(x)
    x = self.norm1(attended + x)
  
    fedforward = self.ff(x)
    return self.norm2(fedforward + x)
```

Normalization and residual connections are standard tricks used to help deep neural networks train faster and more accurately. The layer normalization is applied over the embedding dimension only.

That is, the block applies, in sequence: a self attention layer, layer normalization, a feed forward layer (a single MLP applied independently to each vector), and another layer normalization. Residual connections are added around both, before the normalization. The order of the various components is not set in stone; the important thing is to combine self-attention with a local feedforward, and to add normalization and residual connections.

![content-concepts-raw-nlp-transformers-untitled](https://user-images.githubusercontent.com/62965911/216823120-90db30f9-41ee-496e-b6f1-cca0f90df433.png)

### The transformer block

1. Multi-head attention
2. Scaling the dot product
3. Queries, keys and values

The actual self-attention used in modern transformers relies on three additional tricks.

#### Additional tricks

```python
import torch
import torch.nn.functional as F

## assume we have some tensor x with size (b, t, k)
x = ...

raw_weights = torch.bmm(x, x.transpose(1, 2))
## - torch.bmm is a batched matrix multiplication. It 
##   applies matrix multiplication over batches of 
##   matrices.

weights = F.softmax(raw_weights, dim=2)

y = torch.bmm(weights, x)
```

We’ll represent the input, a sequence of t vectors of dimension k as a t by k matrix 𝐗. Including a minibatch dimension b, gives us an input tensor of size (b,t,k). The set of all raw dot products w′ij forms a matrix, which we can compute simply by multiplying 𝐗 by its transpose. Then, to turn the raw weights w′ij into positive values that sum to one, we apply a row-wise softmax. Finally, to compute the output sequence, we just multiply the weight matrix by 𝐗. This results in a batch of output matrices 𝐘 of size (b, t, k) whose rows are weighted sums over the rows of 𝐗. That’s all. Two matrix multiplications and one softmax gives us a basic self-attention.

#### In Pytorch: basic self-attention

Let's understand with RecSys analogy. The tokens are both users and items. In movie recommenders e.g., to know a user's interest in different movies, we take a dot product of his embedding vector with movies' embedding vectors. Here in self-attention, we take a dot of the given token with all other tokens to know how much the given token is connected to other tokens.

[Transformers from scratch](http://peterbloem.nl/blog/transformers)

In effect, there are five processes we need to understand to implement this model:

- Embedding the inputs
- The Positional Encodings
- Creating Masks
- The Multi-Head Attention layer
- The Feed-Forward layer

#### Embedding

Embedding is handled simply in PyTorch:

```python
class Embedder(nn.Module):
    def __init__(self, vocab_size, d_model):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
    def forward(self, x):
        return self.embed(x)
```

When each word is fed into the network, this code will perform a look-up and retrieve its embedding vector. These vectors will then be learnt as a parameters by the model, adjusted with each iteration of gradient descent.

#### Giving our words context: The Positional Encodings

In order for the model to make sense of a sentence, it needs to know two things about each word: what does the word mean? And what is its position in the sentence?

The embedding vector for each word will learn the meaning, so now we need to input something that tells the network about the word’s position.

*Vasmani et al* answered this problem by using these functions to create a constant of position-specific values:

$$
PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}})
$$

$$
PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

![cbimage](https://user-images.githubusercontent.com/62965911/216824749-ff74e78e-e69e-4b87-b76b-d805dda8095b.png)

![content-concepts-raw-nlp-transformers-untitled-1](https://user-images.githubusercontent.com/62965911/216823110-6e0dd58f-234d-4ae1-804f-f076e00e2903.png)

The positional encoding matrix is a constant whose values are defined by the above equations. When added to the embedding matrix, each word embedding is altered in a way specific to its position.

An intuitive way of coding our Positional Encoder looks like this:

```python
class PositionalEncoder(nn.Module):
    def __init__(self, d_model, max_seq_len = 80):
        super().__init__()
        self.d_model = d_model
      
        ## create constant 'pe' matrix with values dependant on 
        ## pos and i
        pe = torch.zeros(max_seq_len, d_model)
        for pos in range(max_seq_len):
            for i in range(0, d_model, 2):
                pe[pos, i] = \
                math.sin(pos / (10000 ** ((2 * i)/d_model)))
                pe[pos, i + 1] = \
                math.cos(pos / (10000 ** ((2 * (i + 1))/d_model)))
              
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)
 
  
    def forward(self, x):
        ## make embeddings relatively larger
        x = x * math.sqrt(self.d_model)
        #add constant to embedding
        seq_len = x.size(1)
        x = x + Variable(self.pe[:,:seq_len], \
        requires_grad=False).cuda()
        return x
```

The above module lets us add the positional encoding to the embedding vector, providing information about structure to the model.

#### **Creating Our Masks**

Masking plays an important role in the transformer. It serves two purposes:

- In the encoder and decoder: To zero attention outputs wherever there is just padding in the input sentences.
- In the decoder: To prevent the decoder ‘peaking’ ahead at the rest of the translated sentence when predicting the next word.

Creating the mask for the input is simple:

```python
batch = next(iter(train_iter))
input_seq = batch.English.transpose(0,1)
input_pad = EN_TEXT.vocab.stoi['<pad>']## creates mask with 0s wherever there is padding in the input
input_msk = (input_seq != input_pad).unsqueeze(1)
```

For the target_seq we do the same, but then create an additional step:

```python
## create mask as beforetarget_seq = batch.French.transpose(0,1)
target_pad = FR_TEXT.vocab.stoi['<pad>']
target_msk = (target_seq != target_pad).unsqueeze(1)size = target_seq.size(1) ## get seq_len for matrixnopeak_mask= np.triu(np.ones(1, size, size),
k=1).astype('uint8')
nopeak_mask = Variable(torch.from_numpy(nopeak_mask)== 0)target_msk = target_msk & nopeak_mask
```

#### **Multi-Headed Attention**

Once we have our embedded values (with positional encodings) and our masks, we can start building the layers of our model.

Here is an overview of the multi-headed attention layer:

![content-concepts-raw-nlp-transformers-untitled-2](https://user-images.githubusercontent.com/62965911/216823111-f1364a42-3cd3-447b-aa9a-17438528c84f.png)

Multi-headed attention layer, each input is split into multiple heads which allows the network to simultaneously attend to different subsections of each embedding.

A scaled dot-product attention mechanism is very similar to a self-attention (dot-product) mechanism except it uses a scaling factor. The multi-head part, on the other hand, ensures the model is capable of looking at various aspects of input at all levels. Transformer models attend to encoder annotations and the hidden values from past layers. The architecture of the Transformer model does not have a recurrent step-by-step flow; instead, it uses positional encoding in order to have information about the position of each token in the input sequence. The concatenated values of the embeddings (randomly initialized) and the fixed values of positional encoding are the input fed into the layers in the first encoder part and are propagated through the architecture.

In the case of the Encoder, *V, K* and *G* will simply be identical copies of the embedding vector (plus positional encoding). They will have the dimensions Batch_size * seq_len * d_model.

In multi-head attention we split the embedding vector into *N* heads, so they will then have the dimensions $batch\_size * N * seq\_len * (d\_model / N).$

This final dimension $(d\_model / N )$ we will refer to as $d\_k$.

Let’s see the code for the decoder module:

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, heads, d_model, dropout = 0.1):
        super().__init__()
      
        self.d_model = d_model
        self.d_k = d_model // heads
        self.h = heads
      
        self.q_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)
        self.out = nn.Linear(d_model, d_model)
  
    def forward(self, q, k, v, mask=None):
      
        bs = q.size(0)
      
        ## perform linear operation and split into h heads
      
        k = self.k_linear(k).view(bs, -1, self.h, self.d_k)
        q = self.q_linear(q).view(bs, -1, self.h, self.d_k)
        v = self.v_linear(v).view(bs, -1, self.h, self.d_k)
      
        ## transpose to get dimensions bs * h * sl * d_model
     
        k = k.transpose(1,2)
        q = q.transpose(1,2)
        v = v.transpose(1,2)
				## calculate attention using function we will define next
        scores = attention(q, k, v, self.d_k, mask, self.dropout)
      
        ## concatenate heads and put through final linear layer
        concat = scores.transpose(1,2).contiguous()\
        .view(bs, -1, self.d_model)
      
        output = self.out(concat)
  
        return output
```

#### Calculating Attention

![content-concepts-raw-nlp-transformers-untitled-3](https://user-images.githubusercontent.com/62965911/216823113-928794b0-a9fe-40c5-9611-5bda8dc27e63.png)

$$
Attention(Q,K,V) = \mathrm{softmax}\left(\frac{\mathbf Q \mathbf K^\top }{\sqrt{d}}\right) \mathbf V \in \mathbb{R}^{n\times v}
$$

Initially we must multiply Q by the transpose of K. This is then ‘scaled’ by dividing the output by the square root of $d\_k$. Before we perform Softmax, we apply our mask and hence reduce values where the input is padding (or in the decoder, also where the input is ahead of the current word). Finally, the last step is doing a dot product between the result so far and V.

Here is the code for the attention function:

```python
def attention(q, k, v, d_k, mask=None, dropout=None):
    scores = torch.matmul(q, k.transpose(-2, -1)) /  math.sqrt(d_k)

		if mask is not None:
        mask = mask.unsqueeze(1)
        scores = scores.masked_fill(mask == 0, -1e9)

		scores = F.softmax(scores, dim=-1)
  
    if dropout is not None:
        scores = dropout(scores)
      
    output = torch.matmul(scores, v)
    return output
```

In PyTorch, it looks like this:

```python
from torch import Tensor
import torch.nn.functional as f

def scaled_dot_product_attention(query: Tensor, key: Tensor, value: Tensor) -> Tensor:
    temp = query.bmm(key.transpose(1, 2))
    scale = query.size(-1) ** 0.5
    softmax = f.softmax(temp / scale, dim=-1)
    return softmax.bmm(value)
```

Note that MatMul operations are translated to `torch.bmm` in PyTorch. That’s because Q, K, and V (query, key, and value arrays) are batches of matrices, each with shape `(batch_size, sequence_length, num_features)`. Batch matrix multiplication is only performed over the last two dimensions.

The attention head will then become:

```python
import torch
from torch import nn

class AttentionHead(nn.Module):
    def __init__(self, dim_in: int, dim_k: int, dim_v: int):
        super().__init__()
        self.q = nn.Linear(dim_in, dim_k)
        self.k = nn.Linear(dim_in, dim_k)
        self.v = nn.Linear(dim_in, dim_v)

    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        return scaled_dot_product_attention(self.q(query), self.k(key), self.v(value))
```

Now, it’s very easy to build the multi-head attention layer. Just combine `num_heads` different attention heads and a Linear layer for the output.

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, num_heads: int, dim_in: int, dim_k: int, dim_v: int):
        super().__init__()
        self.heads = nn.ModuleList(
            [AttentionHead(dim_in, dim_k, dim_v) for _ in range(num_heads)]
        )
        self.linear = nn.Linear(num_heads * dim_v, dim_in)

    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        return self.linear(
            torch.cat([h(query, key, value) for h in self.heads], dim=-1)
        )
```

Let’s pause again to examine what’s going on in the `MultiHeadAttention` layer. Each attention head computes its own query, key, and value arrays, and then applies scaled dot-product attention. Conceptually, this means each head can attend to a different part of the input sequence, independent of the others. Increasing the number of attention heads allows us to “pay attention” to more parts of the sequence at once, which makes the model more powerful.

#### **The Feed-Forward Network**

This layer just consists of two linear operations, with a relu and dropout operation in between them.

```python
class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff=2048, dropout = 0.1):
        super().__init__() 
        ## We set d_ff as a default to 2048
        self.linear_1 = nn.Linear(d_model, d_ff)
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(d_ff, d_model)
    def forward(self, x):
        x = self.dropout(F.relu(self.linear_1(x)))
        x = self.linear_2(x)
        return x
```

The feed-forward layer simply deepens our network, employing linear layers to analyze patterns in the attention layers output.

#### **One Last Thing : Normalization**

Normalisation is highly important in deep neural networks. It prevents the range of values in the layers changing too much, meaning the model trains faster and has better ability to generalise.

![content-concepts-raw-nlp-transformers-untitled-4](https://user-images.githubusercontent.com/62965911/216823115-b6dec0a3-49cb-49c6-870f-b97ffbe135fa.png)

We will be normalizing our results between each layer in the encoder/decoder, so before building our model let’s define that function:

```python
class Norm(nn.Module):
    def __init__(self, d_model, eps = 1e-6):
        super().__init__()
  
        self.size = d_model
        ## create two learnable parameters to calibrate normalisation
        self.alpha = nn.Parameter(torch.ones(self.size))
        self.bias = nn.Parameter(torch.zeros(self.size))
        self.eps = eps
    def forward(self, x):
        norm = self.alpha * (x - x.mean(dim=-1, keepdim=True)) \
        / (x.std(dim=-1, keepdim=True) + self.eps) + self.bias
        return norm
```

#### Putting it all together!

Let’s have another look at the over-all architecture and start building:

![content-concepts-raw-nlp-transformers-untitled-5](https://user-images.githubusercontent.com/62965911/216823117-03997de3-387a-4efd-a4c5-92e5b2116264.png)

**One last Variable:** If you look at the diagram closely you can see a ‘Nx’ next to the encoder and decoder architectures. In reality, the encoder and decoder in the diagram above represent one layer of an encoder and one of the decoder. N is the variable for the number of layers there will be. Eg. if N=6, the data goes through six encoder layers (with the architecture seen above), then these outputs are passed to the decoder which also consists of six repeating decoder layers.

We will now build EncoderLayer and DecoderLayer modules with the architecture shown in the model above. Then when we build the encoder and decoder we can define how many of these layers to have.

```python
## build an encoder layer with one multi-head attention layer and one ## feed-forward layer
class EncoderLayer(nn.Module):
    def __init__(self, d_model, heads, dropout = 0.1):
        super().__init__()
        self.norm_1 = Norm(d_model)
        self.norm_2 = Norm(d_model)
        self.attn = MultiHeadAttention(heads, d_model)
        self.ff = FeedForward(d_model)
        self.dropout_1 = nn.Dropout(dropout)
        self.dropout_2 = nn.Dropout(dropout)
      
    def forward(self, x, mask):
        x2 = self.norm_1(x)
        x = x + self.dropout_1(self.attn(x2,x2,x2,mask))
        x2 = self.norm_2(x)
        x = x + self.dropout_2(self.ff(x2))
        return x
  
## build a decoder layer with two multi-head attention layers and
## one feed-forward layer
class DecoderLayer(nn.Module):
    def __init__(self, d_model, heads, dropout=0.1):
        super().__init__()
        self.norm_1 = Norm(d_model)
        self.norm_2 = Norm(d_model)
        self.norm_3 = Norm(d_model)
      
        self.dropout_1 = nn.Dropout(dropout)
        self.dropout_2 = nn.Dropout(dropout)
        self.dropout_3 = nn.Dropout(dropout)
      
        self.attn_1 = MultiHeadAttention(heads, d_model)
        self.attn_2 = MultiHeadAttention(heads, d_model)
        self.ff = FeedForward(d_model).cuda()

		def forward(self, x, e_outputs, src_mask, trg_mask):
        x2 = self.norm_1(x)
        x = x + self.dropout_1(self.attn_1(x2, x2, x2, trg_mask))
        x2 = self.norm_2(x)
        x = x + self.dropout_2(self.attn_2(x2, e_outputs, e_outputs,
        src_mask))
        x2 = self.norm_3(x)
        x = x + self.dropout_3(self.ff(x2))
        return x

		## We can then build a convenient cloning function that can generate multiple layers:
		def get_clones(module, N):
		    return nn.ModuleList([copy.deepcopy(module) for i in range(N)])
```

We’re now ready to build the encoder and decoder:

```python
class Encoder(nn.Module):
    def __init__(self, vocab_size, d_model, N, heads):
        super().__init__()
        self.N = N
        self.embed = Embedder(vocab_size, d_model)
        self.pe = PositionalEncoder(d_model)
        self.layers = get_clones(EncoderLayer(d_model, heads), N)
        self.norm = Norm(d_model)
    def forward(self, src, mask):
        x = self.embed(src)
        x = self.pe(x)
        for i in range(N):
            x = self.layers[i](x, mask)
        return self.norm(x)
  
class Decoder(nn.Module):
    def __init__(self, vocab_size, d_model, N, heads):
        super().__init__()
        self.N = N
        self.embed = Embedder(vocab_size, d_model)
        self.pe = PositionalEncoder(d_model)
        self.layers = get_clones(DecoderLayer(d_model, heads), N)
        self.norm = Norm(d_model)
    def forward(self, trg, e_outputs, src_mask, trg_mask):
        x = self.embed(trg)
        x = self.pe(x)
        for i in range(self.N):
            x = self.layers[i](x, e_outputs, src_mask, trg_mask)
        return self.norm(x)
```

And finally… The transformer!

```python
class Transformer(nn.Module):
    def __init__(self, src_vocab, trg_vocab, d_model, N, heads):
        super().__init__()
        self.encoder = Encoder(src_vocab, d_model, N, heads)
        self.decoder = Decoder(trg_vocab, d_model, N, heads)
        self.out = nn.Linear(d_model, trg_vocab)
    def forward(self, src, trg, src_mask, trg_mask):
        e_outputs = self.encoder(src, src_mask)
        d_output = self.decoder(trg, e_outputs, src_mask, trg_mask)
        output = self.out(d_output)
        return output
## we don't perform softmax on the output as this will be handled 
## automatically by our loss function
```

The original Transformer model is a stack of 6 layers. The output of layer l is the input of layer l+1 until the final prediction is reached. There is a 6-layer encoder stack on the left and a 6-layer decoder stack on the right:

![content-concepts-raw-nlp-transformers-untitled-6](https://user-images.githubusercontent.com/62965911/216823118-ce558916-d199-430d-8b8b-9f4dcd037e2a.png)

The architecture of the Transformer

On the left, the inputs enter the encoder side of the Transformer through an attention sub-layer and FeedForward Network (FFN) sub-layer. On the right, the target outputs go into the decoder side of the Transformer through two attention sub-layers and an FFN sub-layer. We immediately notice that there is no RNN, LSTM, or CNN. Recurrence has been abandoned. Attention has replaced recurrence, which requires an increasing number of operations as the distance between two words increases.

> The attention mechanism is a "word-to-word" operation. The attention mechanism will find how each word is related to all other words in a sequence, including the word being analyzed itself.

## Language Modeling

Language Models (LMs) estimate the probability of different linguistic units: symbols, tokens, token sequences.

We see language models in action every day - look at some examples. Usually models in large commercial services are a bit more complicated than the ones we will discuss today, but the idea is the same: if we can estimate probabilities of words/sentences/etc, we can use them in various, sometimes even unexpected, ways.

We, humans, already have some feeling of "probability" when it comes to natural language. For example, when we talk, usually we understand each other quite well (at least, what's being said). We disambiguate between different options which sound similar without even realizing it!

But how a machine is supposed to understand this? A machine needs a language model, which estimates the probabilities of sentences. If a language model is good, it will assign a larger probability to a correct option.

Read [this](https://lena-voita.github.io/nlp_course/language_modeling.html) article to understand the concept of `language models` in depth.

### **Masked language modeling**

**Masked language modeling** is the task of training a model on input (a sentence with some masked tokens) and obtaining the output as the whole sentence with the masked tokens filled. But how and why does it help a model to obtain better results on downstream tasks such as classification? The answer is simple: if the model can do a cloze test (a linguistic test for evaluating language understanding by filling in blanks), then it has a general understanding of the language itself. For other tasks, it has been pretrained (by language modeling) and will perform better.

![content-concepts-raw-nlp-language-modeling-untitled](https://user-images.githubusercontent.com/62965911/216823093-700825ee-7f47-42c8-8a47-ba2a5bfb544f.png)

Here's an example of a cloze test:

*George Washington was the first President of the ___ States.*

It is expected that *United* should fill in the blank. For a masked language model, the same task is applied, and it is required to fill in the masked tokens. However, masked tokens are selected randomly from a sentence.

In BERT4Rec, authors used Cloze task technique (also known as “Masked Language Model) to train the bi-directional model. In this, we randomly mask some items (i.e., replace them with a special token [mask]) in the input sequences, and then predict the ids of those masked items based on their surrounding context.

$$
\begin{align} Input: [v_1, v_2, v_3, v_4, v_5] \xrightarrow{\text{randomly mask}} [v_1, [mask]_1, v_3, [mask]_2, v_5]\\ Labels: [mask]_1 = v_2, [mask]_2 = v_4 \end{align}
$$

Let's take another example:

In Autumn the ______ fall from the trees.

Do you know the answer? Most likely you do, and you do because you have considered the context of the sentence.

We see the words *fall* and *trees* — we know that the missing word is something that *falls from trees*.

A lot of things fall from trees, acorns, branches, leaves — but we have another condition, *in Autumn* — that narrows down our search, the most probable thing to fall from a tree in Autumn are *leaves*.

As humans, we use a mix of general world knowledge, and linguistic understanding to come to that conclusion. For BERT, this guess will come from reading *a lot* — and learning linguistic patterns incredibly well.

BERT may not know what Autumn, trees, and leaves are — but it does know that given linguistic patterns, and the context of these words, the answer is most likely to be *leaves*.

The outcome of this process — for BERT — is an improved comprehension of the style of language being used.

### Causal language modeling

Causal language modeling is the task of predicting the token following a sequence of tokens. In this situation, the model only attends to the left context (tokens on the left of the mask). Such a training is particularly interesting for generation tasks.

<aside>
👌🏼 I think it's because pre-BERT, causal language modeling was actually just called language modeling. When the BERT paper arrived they coined the task of predicting random masked tokens as masked language modeling, which led to subsequent papers presenting transformer-like models for translation or generation to use the term causal language modeling for clarity. ~ [https://www.reddit.com/user/keramitas/](https://www.reddit.com/user/keramitas/)

</aside>

### Permutation language modeling

PLM is the idea of capturing bidirectional context by training an autoregressive model on all possible permutation of words in a sentence. Instead of fixed left-right or right-left modeling, XLNET maximizes expected log likelihood over all possible permutations of the sequence. In expectation, each position learns to utilize contextual information from all positions thereby capturing bidirectional context. No [MASK] is needed and input data need not be corrupted.

![content-concepts-raw-nlp-language-modeling-untitled-1](https://user-images.githubusercontent.com/62965911/216823090-cb38a865-e721-42ac-a5d5-23c1e288e69e.png)

The above diagram illustrates PLM. Let us consider that we are learning x3 (the token at the 3rd position in the sentence). PLM trains an autoregressive model with various permutations of the tokens in the sentence, so that in the end of all such permutations, we would have learnt x3, given all other words in the sentence. In the above illustration, we can see that the next layer takes as inputs only the tokens preceding x3 in the permutation sequence. This way, autoregression is also achieved.


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

## Labs

1. [Natural Language Processing 101](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2021-07-09-concept-nlp-basics.ipynb)
2. [Training Embeddings Using Gensim and FastText](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2021-07-10-concept-embedding-gensim-fasttext.ipynb)
3. [NLP Playground](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/2022-01-29-nlp.ipynb)
4. [Email Classification](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-02-email-classification.ipynb)