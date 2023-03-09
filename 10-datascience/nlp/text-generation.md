# Text Generation

Natural language generation (NLG) can actually tell a story – exactly like that of a human analyst – by writing the sentences and paragraphs for you. It can also summarize reports. 

*“Conversations with systems that have access to data about our world will allow us to understand the status of our jobs, our businesses, our health, our homes, our families, our devices, and our neighborhoods — all through the power of NLG. It will be the difference between getting a report and having a conversation. The information is the same but the interaction will be more natural"*.  **

## Algorithms

### Text Generation with Markov Chain

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
            # get next possible set of words from the seed word
            if current in self.model:
                possible_transitions = self.model[current]
                choice = random.choice(possible_transitions)
                if choice is None: break

                # check if choice is period and if so append to previous element
                if choice == '.':
                    output[-1] = output[-1] + choice
                else:
                    output.append(choice)
                current = tuple(output[-n:])
            else:
                # should return ending punctuation of some sort
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

## Important Papers

The survey: Text generation models in deep learning [[2020](https://reader.elsevier.com/reader/sd/pii/S1319157820303360?token=AF608DFD534B46032B10D2F3DFD1B74CE0D3DC436E536660C856B15C296B929524171B9064D8772BA4762DCC57DAA69E)]

Survey of the State of the Art in Natural Language Generation: Core tasks, applications [[2017](https://arxiv.org/pdf/1703.09902.pdf)]

Neural Text Generation: A Practical Guide [[2017](https://arxiv.org/pdf/1711.09534.pdf)]

Neural Text Generation: Past, Present and Beyond [[2018](https://arxiv.org/pdf/1803.07133.pdf)]

## Experiments

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

## Text Generation with char-RNNs

[The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

- [How to Quickly Train a Text-Generating Neural Network for Free](https://minimaxir.com/2018/05/text-neural-networks/)
- [Natural Language Generation using LSTM-Keras](https://github.com/shashank-bhatt-07/Natural-Language-Generation-using-LSTM-Keras)

## References

[BoredHumans.com - Fun AI Programs You Can Use Online](https://boredhumans.com/)

[eaglenlp/Text-Generation](https://github.com/eaglenlp/Text-Generation)

[tokenmill/awesome-nlg](https://github.com/tokenmill/awesome-nlg)

[ChenChengKuan/awesome-text-generation](https://github.com/ChenChengKuan/awesome-text-generation)

[Tianwei-She/awesome-natural-language-generation](https://github.com/Tianwei-She/awesome-natural-language-generation)

[Papers with Code - Text Generation](https://paperswithcode.com/task/text-generation)

[Eulring/Text-Generation-Papers](https://github.com/Eulring/Text-Generation-Papers)

[Arxiv Sanity Preserver](http://www.arxiv-sanity.com/search?q=natural+language+generation)

---

### Decoding techniques - Greedy search, Beam search, Top-K sampling and Top-p sampling with Transformer

[How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)

[Google Colaboratory](https://colab.research.google.com/drive/1Wf9HT2JjW-g_7UKLk2jmlN_K3SVkL9-i#scrollTo=lzaVvvIXMGOx)

### Controlling Text Generation with Plug and Play Language Models (PPLM)

PPLM lets users combine small attribute models with an LM to steer its generation. Attribute model scan be 100,000 times smaller than the LM and still be effective insteering it, like a mouse sitting atop our wooly mammoth friend and telling it where to go.The mouse tells the mammoth where to go using gradients.

[Controlling Text Generation with Plug and Play Language Models](https://eng.uber.com/pplm/)

[uber-research/PPLM](https://github.com/uber-research/PPLM)

[Plug and Play Language Models: A Simple Approach to Controlled Text Generation](https://paperswithcode.com/paper/plug-and-play-language-models-a-simple)

[Google Colaboratory](https://colab.research.google.com/drive/1DXBs1w_yyBbXsfRnFW98k_iZ3AYHhITS#scrollTo=fN-oIcZNo4xD)

### GPT-2 Fine Tuning

- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)

### Autoregressive Language Generation

It based on the assumption that the probability distribution of a word sequence can be decomposed into the product of conditional next word distributions. The way these models actually work is that after each token is produced, that token is added to the sequence of inputs. And that new sequence becomes the input to the model in its next step.

### **Word-Level Generation vs Character-Level Generation**

In general, word-level language models tend to display higher accuracy than character-level language models. This is because they can form shorter representations of sentences and preserve the context between words easier than character-level language models. However, large corpora are needed to sufficiently train word-level language models, and one-hot encoding isn't very feasible for word-level models. In contrast, character-level language models are often quicker to train, requiring less memory and having faster inference than word-based models. This is because the "vocabulary" (the number of training features) for the model is likely to be much smaller overall, limited to hundreds of characters rather than hundreds of thousands of words.