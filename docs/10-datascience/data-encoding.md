# Data Encoding

## Discrete Data

### Label Encoding

Label encoding is perhaps the simplest and most direct method of encoding discrete data – each unique category is associated with a single integer label. This is almost always not the final encoding that you should use for categorical variables, since attaching encodings in this way forces us to make arbitrary decisions that lead to meaningful outcomes. If we associate a category value “Dog” with 1 but “Snake” with 2, the model has access to the explicitly coded quantitative relationship that “Snake” is two times “Dog” in magnitude or that “Snake” is larger than “Dog.” Moreover, there is no good reason “Dog” should be labeled 1 and “Snake” should be labeled 2 instead of vice versa. However, label encoding is the basis/primary step upon which many other encodings can be applied. Thus, it is useful to understand how to implement it.

![label_encoding](https://user-images.githubusercontent.com/62965911/230728515-0bcd376f-f8ad-465b-abfb-6c0e86995d88.png)

### One-Hot Encoding

In cases of categorical variables in which no definitive quantitative label can be attached, the simplest satisfactory choice is generally one-hot encoding. If there are n unique classes, we create n binary columns, each representing whether the item belongs to that class or not. Thus, there will be one “1” across each of the n columns for every row (and all others as “0”).

![onehot-encoding](https://user-images.githubusercontent.com/62965911/230728517-dc3be36c-a669-42a5-8052-daeaea45ebaa.png)

One problem that may arise from using one-hot encoding, however, is multicollinearity. Multicollinearity occurs when several features are highly correlated such that one can reliably be predicted as a linear relationship of the others. In a one-hot encoding, the sum of feature values across each row is always 1; if we know the values of all other features for some row, we also know the value of the remaining feature.

This can become problematic because each feature is no longer independent, whereas many machine learning algorithms like K-Nearest Neighbors (KNN) and regression assume that each dimension of the dataset is not correlated with any other. While multicollinearity may only have a marginal negative effect on model performance, the larger problem is the effect on parameter interpretation. If two independent variables in a Linear Regression model are highly correlated, their resulting parameters after training become almost meaningless because the model could have performed just as well with another set of parameters (e.g., switching the two parameters, ambiguous multiplicity of solutions). Highly correlated features act as approximate duplicates, which means that the corresponding coefficients are halved as well.

One simple method to address multicollinearity in one-hot encoding is to randomly drop one (or several) of the features in the encoded feature set. This has the effect of disrupting a uniform sum of 1 across each row while still retaining a unique combination of values for each item (one of the categories will be defined by all zeros, since the feature that would have been marked as “1” was dropped). The disadvantage is that the equality of representation across classes of the encoding is now unbalanced, which may disrupt certain machine learning models – especially ones that utilize regularization. The take-away for best performance: choose either regularization + feature selection or column dropping, but not both.

### Binary Encoding

Two weaknesses of one-hot encoding – sparsity and multicollinearity – can be addressed, or at least improved, with binary encoding. The categorical feature is label encoded (i.e., each unique category is associated with an integer); the labels are converted to binary form and transferred to a set of features in which each column is one place value. That is, a column is created for each digit place of the binary representation.

![binary-encoding](https://user-images.githubusercontent.com/62965911/230728572-d774acbd-89cf-4cce-89aa-8d885ccff95e.png)

Because we use binary representations rather than allocating one column per unique class, we more compactly represent the same information (i.e., the same class has the same combination of “1”s and “0”s across the features) at the cost of decreased interpretability (i.e., it’s not clear what each column represents). Moreover, there is no reliable multicollinearity between each of the features used to represent the categorical information.

### Frequency Encoding

Label encoding, one-hot encoding, and binary encoding each offer methods of encoding that reflect the “pure identity” of each unique class; that is, we devise quantitative methods to assign a unique identity to each class.

However, we can both assign unique values to each class and communicate additional information about each class at once. To frequency-encode a feature, we replace each categorical value with the proportion of how often that class appears in the dataset. With frequency encoding, we communicate how often that class appears in the dataset, which may be of value to whatever algorithm is processing it.

![frequency-encoding](https://user-images.githubusercontent.com/62965911/230728632-f5ed3606-ede0-4846-b51e-67c6bfd09076.png)

Like one-hot encoding and binary encoding, we attach a unique quantitative representation to each class (although frequency encoding does not guarantee a unique quantitative representation, especially in small datasets). With this encoding scheme, however, the actual value of the representation lies on a continuous scale, and quantitative relationships between the encodings are not arbitrary but instead communicate some piece of information. In the preceding example, “Denver” is “three times” Miami because it appears three times as often in the dataset.

Frequency encoding is the most powerful when the dataset is representative and free of bias. If this is not the case, the actual quantitative encodings may be meaningless in the sense of not providing relevant and truthful/representative information for the purposes of modeling.

### Target Encoding

Frequency encoding is often unsatisfactory because it often doesn’t directly reflect information in a class that is directly relevant to a model that uses it. Target encoding is an attempt to model the relationship more directly between the categorical class x and the dependent variable y to be predicted by replacing each class with the mean or median (respectively) value of y for that class. It is assumed that the target class is already in quantitative form, although the target does not necessarily need to be continuous (i.e. a regression problem) to be used in target encoding. For instance, taking the mean of binary classification labels, which are either 0 or 1, gives insight into the proportion of items in the dataset with that class that were associated with class 0. This can be interpreted as the probability the item belongs to a target class given only one independent feature.

![525591_1_En_2_Fig12_HTML](https://user-images.githubusercontent.com/62965911/230728947-2e21e162-0a82-4747-8bd9-240d143e136c.png)

Figure: Target encoding using the mean

![525591_1_En_2_Fig13_HTML](https://user-images.githubusercontent.com/62965911/230728948-7dd2208a-5b83-4c32-bf91-33c77ca2f189.png)

Figure: Target encoding using the median

Note that target encoding can lead to data leakage if encoding is performed before the training and validation sets are split, since the averaging function incorporates information from both the training and validation sets. In order to prevent this, encode the training and validation sets separately after splitting. If the validation dataset is too small, target-encoding the set independently may yield skewed, unrepresentative encodings. In this case, you can use averages per class from the training dataset. This form of “data leakage” is not inherently problematic, since we are using training data to inform operation on the validation set rather than using validation data to inform operation on the training set.

### Leave-One-Out Encoding

Mean-based target encoding can be quite powerful, but it suffers from the presence of outliers. If outliers are present that skew the mean, their effects are imprinted across the entire dataset. Leave-one-out encoding is a variation on the target encoding scheme by leaving the “current” item/row out of consideration when calculating the mean for all items of that class. Like target encoding, encoding should be performed separately on training and validation sets to prevent data leakage.

![525591_1_En_2_Fig15_HTML](https://user-images.githubusercontent.com/62965911/230729170-913e381b-941d-451a-99c8-f3e9e2aece07.png)

### James-Stein Encoding

Target encoding and leave-one-out encoding assume that each categorical feature is directly and linearly related to the dependent variable. We can take a more sophisticated approach to encoding with James-Stein encoding by incorporating both the overall mean for a feature and the individual mean per class for a feature into an encoding (Figure 2-17). This is achieved by defining the encoding for a category as a weighted sum of the overall mean and individual mean per class via a parameter β, which is bounded by 0 ≤ β ≤ 1.

![525591_1_En_2_Fig17_HTML](https://user-images.githubusercontent.com/62965911/230729233-a7cfcf61-0db4-413b-8235-55243b45b0b0.png)

When β = 0, James-Stein encoding is the same as mean-based target encoding. On the other hand, when β = 1, James-Stein encoding replaces all values in a column with the average dependent variable value, regardless of individual class values.

### Weight of Evidence

The weight of evidence (WoE) technique originated from credit scoring; it was used to measure how “separable” good customers (paid back a loan) were from bad customers (defaulted on a loan) across a group i (this could be something like customer location, history, etc.)

Weight of evidence is often presented as representing how much the evidence undermines or supports the hypothesis. In the context of categorical encoding, the “hypothesis” is that the selected categorical feature can cleanly divide classes such that we can reliably predict which class an item falls in given only information about its inclusion or exclusion from the group i. The “evidence” is the actual distribution of target values within a certain group i.

We can also generalize this to multiclass problems by finding the WoE for each class, in which “class 0” is “in class” and “class 1” is “not in class”; the weight of evidence of the complete dataset can then be found by somehow aggregating the individual class-specific WoE calculation, for example, by taking the mean.

## Continuous Data

### Min-Max Scaling

Min-max scaling generally refers to the scaling of the range of a dataset such that it is between 0 and 1 – the minimum value of the dataset is 0, and the maximum is 1, but the relative distances between points remain the same.

### Robust Scaling

From the formula for min-max scaling, we see that each scaled value of the dataset is directly impacted by the maximum and minimum values. Hence, outliers significantly impact the scaling operation. Robust scaling subtracts the median value from all values in the dataset and divides by the interquartile range.

### Standardization

More commonly, machine learning algorithms assume that data is standardized – that is, in the form of a normal distribution with unit variance (standard deviation of 1) and zero mean (centered at 0). Assuming the input data is already somewhat normally distributed, standardization subtracts the dataset’s mean and divides by the dataset’s standard deviation. This has the effect of shifting the dataset mean to 0 and scaling the standard deviation to 1.

## Text Data

### Raw Vectorization

Raw vectorization can be thought of as “one-hot encoding” for text: it is an explicit quantitative representation of the information contained within text. Rather than assigning each text a unique class, texts are generally vectorized as a sequence of language units, like characters or words. These are also referred to as tokens. Each of these words or characters is considered to be a unique class, which can be one-hot encoded. Then, a passage of text is a sequence of one-hot encodings.

![525591_1_En_2_Fig28_HTML](https://user-images.githubusercontent.com/62965911/230732506-ccfe1770-c289-4702-a652-73ffb8abdc97.png)

### Bag of Words

In order to reduce the sheer dimensionality/size of a raw vectorization text representation, we can use the Bag of Words (BoW) model to “collapse” raw vectorizations. In Bag of Words, we count how many times each language unit appears in a text sample while ignoring the specific order and context in which the language units were used.

![525591_1_En_2_Fig29_HTML](https://user-images.githubusercontent.com/62965911/230732553-d1e7cec3-760f-4f8d-9e8c-0c5a153572db.png)

### N-Grams

We can be more sophisticated than the Bag of Words model by counting the number of unique two-word combinations, or bigrams. This can help reveal context and multiplicity of word meaning; for instance, the Paris in the stripped (no punctuation, no capitalization) text except “paris france” is very different from the Paris in “paris hilton.” We can consider each bigram to be its own term and encode it as such.

![525591_1_En_2_Fig30_HTML](https://user-images.githubusercontent.com/62965911/230732621-0c4d3fd4-f080-4647-b7ad-62cfbcb51011.png)

### TF-IDF

Another weakness of the Bag of Words model is that the number of times a word appears in the text may not be a good indicator of how important or relevant it is. For instance, the word “the” appears seven times in this paragraph, more than any other. Does this mean that the word “the” is the most significant or holds the most meaning?

No, the word “the” is primarily an artifact of grammar/syntactic structure and reflects little semantic meaning, at least in contexts we are generally concerned with. We usually address the problem of text-saturating syntactic tokens by removing so-called “stop words” from a corpus before encoding it.

However, there are many words left over from stop word screening that hold semantic value but suffer from another problem that the word “the” creates: Because of the structure of the corpus, certain words inherently appear very often throughout the text. This does not mean that they are more important. Consider a corpus of customer reviews for a jacket: naturally, the word “jacket” will appear very often (e.g., “I bought this jacket…,” “This jacket arrived at my house…”), but in actuality it is not very relevant to our analysis. We know that the corpus is about the jacket and care instead about words that may occur less but mean more, like “bad” (e.g., “This jacket is bad”), “durable” (e.g., “Such a durable jacket!”), or “good” (e.g., “This was a good buy”).

We can formalize this intuition by using TF-IDF, or Term Frequency–Inverse Document Frequency, encoding. The logic behind TF-IDF encoding is that we care more about terms that appear often in one document (Term Frequency) but not very often across the entire corpus (Inverse Document Frequency). TF-IDF is calculated by weighting these two effects against each other.

### Word2Vec

Previous discussion on encoding methods focused on relatively simplistic attempts to capture a text sample’s meaning by attempting to extract one “dimension” or perspective. The Bag of Words model, for instance, captures meaning simply by counting how often a word appears in the text. The Term Frequency–Inverse Document Frequency encoding method attempts to improve upon this scheme by defining a slightly more sophisticated level of meaning by balancing the occurrence of a word in a document with its occurrence in the complete corpus. In these encoding schemes, there is always one perspective or dimension of the text that we leave out and simply cannot capture.

With deep neural networks, however, we can capture more complex relationships between text samples – the nuances of word usage (e.g., “Paris,” “Hilton,” and “Paris Hilton” all mean very different things!), grammatical exceptions, conventions, cultural significance, etc. The Word2Vec family of algorithms associates each word with a fixed-length vector representing latent (“hidden”, “implicit”) features.

## Time Data

Time/temporal data often appears in practical tabular datasets. For instance, a tabular dataset of online customer reviews may have a timestamp down to the second indicating exactly when it was posted. Alternatively, a tabular dataset of medical data might be associated with the day it was collected, but not the exact time. A tabular dataset of quarterly company earnings reports will contain temporal data by quarter. Time is a dynamic and complex data type that takes on many different forms and sizes. Luckily, because time is both so rich with information and well-understood, it is relatively easy to encode time or temporal features.

There are several methods to convert time data into a quantitative representation to make it readable to machine learning and deep learning models. The simplest method is simply to assign a time unit as a base unit and represent each time value as a multiple of base units from a starting time. The base unit should generally be the most relevant unit of time to the prediction problem; for instance, if time is stored as a month, date, and year and the prediction task is to predict sales, the base unit is a day, and we would represent each date as the number of days since a starting date (a convenient starting position like January 1, 1900, or simply the earliest date in the dataset). On the other hand, in a physics lab, we may need a base unit of a nanosecond due to high required precision, and time may be represented as the number of nanoseconds since some determined starting time.

## Geographical Data

Many tabular datasets will contain geographical data, in which a location is somehow specified in the dataset. Similarly to temporal/time data, geographical data can exist in several different levels of scope – by continent, country, state/province, city, zip code, address, or longitude and latitude, to name a few. Because of the information-rich and highly context-dependent nature of geographical data, there aren’t well-established, sweeping guidelines on encoding geographical data. However, you can use many of the previously discussed encoding tools and strategies to your advantage here.

If your dataset contains geographical data in categorical form, like by country or state/province, you can use previously discussed categorical encoding methods, like one-hot encoding or target encoding.

Latitude and longitude are precise geospatial location indicators already in quantitative form, so there is no requirement for further encoding. However, you may find it valuable to add relevant abstract information derived from the latitude and longitude to the dataset, like which country the location falls in.

When working with specific addresses, you can extract multiple relevant features, like the country, state/province, zip code, and so on. You can also derive the exact longitude and latitude from the address and append both to the dataset as continuous quantitative representations of the address location.