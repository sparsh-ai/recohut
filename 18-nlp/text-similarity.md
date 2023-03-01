# Text Similarity

![content-concepts-raw-nlp-text-similarity-img](https://user-images.githubusercontent.com/62965911/216823098-80abfe58-bb80-40a1-bced-7e144a61b042.png)

## **Introduction**

- **Definition:** Text similarity has to determine how 'close' two pieces of text are both in surface closeness (lexical similarity) and meaning (semantic similarity)
- **Applications:** Duplicate document detection, text clustering, product recommendations
- **Scope:** No scope decided yet
- **Tools:** Sentence Transformer Library, Universal Sentence Encoder Model (TFHub), Scikit-learn

## **Models**

### BERT

Use transfer learning to fine-tune a BERT encoder. This encoder will work as a feature extractor. e.g.  the most common version of BERT convert any given text into a numeric vector of length 768 (this vector is also known as contextual embedding).

### Bag-of-words

Extract features using models like TF-IDF, CountVectorizer.

### DeepRank

*[DeepRank: A New Deep Architecture for Relevance Ranking in Information Retrieval. arXiv, 2017.](https://arxiv.org/abs/1710.05649)*

### FAISS

*[Billion-scale similarity search with GPUs. arXiv, 2017.](https://arxiv.org/abs/1702.08734)*

Faiss is a library for efficient similarity search and clustering of dense vectors.

### Similarity Measures

L1 (Manhatten distance), L2 (Euclidean distance), Hinge Loss for Triplets.

## **Process flow**

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

## Use Cases

### Semantic Relation Estimation

To maintain a level of coherence and similarity among various letters and speeches, a model was built that will help in assessing this document similarity. In approach 1, TF-IDF with Latent semantic indexing was used to extract features and cosine similarity as the distance metric. In approach 2, BERT with PCA was used for feature extraction and 3 distance measures - L1, L2, and cosine, for similarity calculation. Check out [this](https://www.notion.so/Semantic-Similarity-085a0be7e70f4dec99a06c07cca3b12c) notion.

### Finding Hardware Parts in Warehouse

There are millions of hardware items (e.g. 0.5mm steel wire grade q195) in the warehouse and customer generally asks for items in natural language (e.g. grade195 steel wire with 0.5mm thickness). A text similarity system was built using an ensemble of 3 Bag-of-words based Count vectorizer model with different types of tokenization process and n-gram range. Check out [this](https://www.notion.so/Finding-Hardware-Parts-in-Warehouse-922EE-fa28cf6931a94fa89ad2d4d2183f6bcc) notion.

### Image + Text Similarity

Use the textual details and images of products, find the exact similar product among different groups. Around 35 GB of retail product images was scraped and used to build the system. Checkout the notion [here](https://www.notion.so/Image-Text-Similarity-fe5130324ae14ab48a30c93444348f4a).

### Text Recommendation

For the given BRM text, recommend top-5 GAO text. We used universal sentence encoder to encode the text and calculated cosine similarity within group. Then an item-based recommender model was used to find most suitable top-K candidates in GAO based on the interaction history. Check out [this](https://www.notion.so/Text-Recommendation-System-351c57bdb60e40da8531bf19c867314a) notion.
