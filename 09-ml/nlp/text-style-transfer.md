# Text Style Transfer

How to adapt the text to different situations, audiences and purposes by making some changes? The style of the text usually includes many aspects such as morphology, grammar, emotion, complexity, fluency, tense, tone and so on.

With this technology, the sentences can be converted according to the required style, such as the emotion from positive to negative, writing style from normal to shakepeare style and tone style from formal to informal. 

Challenges:

1. Lack of a large number of parallel corpora
2. Uncertainty of the evaluation indicators

### Literature review

- Jhamtani (2017) used parallel data to train a seq2seq model to convert style of text to Shakespeare style. The data set used in this study is a line-by-line modern interpretation of 16 of 36 Shakespeare’s plays, of which the training set contains 18,395 sentences in 14 plays, and the last play, “Romeo and Juliet,” which contains 1,462 sentences, is the test set.  In order to solve the problem of insufficient parallel data, the author combined with additional text to pre-train an external dictionary representation (embeddings) from Shakespeare English to modern English and explained that the shared dictionary table on the source language side and the target language side is beneficial to improve performance. After experiments, the method achieved a BLEU score of 31+, which is about 6 points higher than the strongest benchmark MOSES.
- Carlson (2018) pointed out that the style of an article that can be perceived is composed of many characteristics, including the length of the sentence, the active or passive voice, the level of vocabulary, the degree of tone, and the formality of the language. He collected a large, undeveloped parallel text data set - the Bible translation corpus. The study shows that its data set is conducive to the model's generalization of style learning, because each version of the Bible reflects A unique style. Each version exceeds 31,000 sessions and can generate more than 1.5 million unique parallel training data.
- Harnessing (2019) mainly focused on the study of the formality of text (Formality), and proposed a method to transfer the style from informal text to formal text. The study shows that when the current parallel corpus is very small, using a large neural network model that has been pre-trained on a large-scale corpus and has learned general language knowledge will be effective, and the introduction of rules effectively reduces the complexity of the data.
- Shang (2019) pointed out that the method based on the standard S2S (sequence-to-sequence) proposed latent space cross prediction method (Cross Projection in Latent Space) realized the function of style conversion between different style data sets. By inputting from the Encoder module of Style A and outputting from the Decoder module of Style B through the cross prediction function, the text style transfer is realized.
- Keith (2018) proposed Zero-Shot Style Transfer in which the zero-sample style transfer is converted into a single machine translation problem, and based on this, a recurrent neural network (RNN) model based on S2S (sequence-to-sequence) architecture is created.

### Papers

1. [Survey Paper (2020)](https://arxiv.org/ftp/arxiv/papers/2005/2005.02914.pdf)