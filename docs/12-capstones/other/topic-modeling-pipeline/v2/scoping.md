# Scoping

## Objective
The JWST mission team would like to explore the feasibility of using machine learning to identify tweets related to the mission with a negative sentiment, so that team members can review them manually and respond if needed. Tracking brand sentiment allows mission management to detect misleading or inaccurate information posted to social and have the distributed mission team members respond to negative posts as soon as possible.

## Ste 0: Problem Understanding
### What is the problem?
Public perception of a mission could be harshly influenced by invalid or mis-information on social media. The brand of the mission, its core management and operations teams could be negatively impacted by unfairly critical or inaccurate tweets posted to Twitter. Team members are well-versed in the details of the mission and have clarity around its scientific goals. They are best equipped to respond to such posts to clarify or correct discrepencies related to the topic being discussed.

With access to such tweets on Twitter, the mission team can make these clarifications faster and more efficient. Indeed brand monitoring and customer support are two of the business use-cases of sentiment analysis ([1](https://monkeylearn.com/blog/sentiment-analysis-examples/#:~:text=Expressions%20can%20be%20classified%20as%20positive%2C%20negative%2C%20or,which%20can%20be%20used%20across%20industries%20and%20teams.)).

### Who does it impact and how much?
It impacts everyone involved in planning and running the mission. It undermines efforts made to
- mitigate even minor failures by the mission engineering team
- ensure useful science experiments are being conducted by the mission

It is difficult to estimate the cost of having negative sentiment about a mission pervasive on social media. However, negative [public sentiment about any aspect of a space mission](https://www.encyclopedia.com/reference/culture-magazines/public-opinion-about-space-exploration) incorrectly undermines the mission managers and space agencies (NASA, ESA, CSA) involved in laying out robust scientific objectives for the mission. This subsequently undermines the ability to fund future missions.

### How is it being solved today and what are some of the gaps?
Tweets with a negative sentiment can be identified by a human reading them and interpreting the text. Without reading all tweets related to the mission (eg. tweets containing a well-defined set of keywords), it is impossible to identify such tweets.

The current approach to pick out negative sentiment tweets involves randomly guessing at the sentiment of a tweet. This picks up some positive sentiment tweets as well. Unfortunately, when the randomly guessed twets are flagged to mission team members for review, they have to read the positive sentiment tweets (that are actually not of a concern), which slows them down when responding to the harmful or inaccurate tweets and is time-consuming.

Therefore, a more accurate approach to identifying tweets that
- contain text from a well-defined set of mission-related keywords
- have a negative sentiment

is required in order to respond to them faster and more effectively than being done currently.

We should note that the mission team may wish to spend time reading a sampling or (depending on the number of tweets) all of the positive sentiment tweets, but these are a lower priority than reading (and responding to) the negative sentiment tweets. Moving forward through this project, we will assume that positive sentiment tweets will not be read.

## Step 1: Goals
### What are the goals of the project?
The objective of this project is to minimize harmful sentiment on Twitter about the mission in the public domain.

### How will we know if our project is successful?
The project will be successful if the ML-based approach to predicting if support is needed is more accurate than a naive approach (random guessing). The metric used to assess accuracy is discussed in the **Choice of Evaluation Metric** sub-section below.

## Step 2: Actions
### What actions or interventions will this work inform?
Mission management can identify potentially harmful tweets about the mission and have team members review and respond to these tweets. Neutral or negative sentiment tweets can then be reviewed, and responded to, while positive sentiment tweets do not beed to be reviewed.

Rather than reading all relevant tweets (containing mission-related terms), machine learning can be used to identify the harmful ones and only those can be read/reviewed in order to be most efficient with time spent by team members.

Actions
1. Identify potentially harmful tweets (those with a negative or neutral sentiment) from all mission-related tweets that were posted. By focusing on these tweets, this will help mitigate the presence of harmful misinformation about the mission on the platform.

## Step 3: Data
### What data do you have access to internally?
1. Tweets containing terms related to the mission were streamed using the Twitter API and Amazon Kinesis Firehose. Metadata was extracted from the tweets, including user location, number of user followers, etc. The dataset is not labelled with the sentiment of the text in the tweet.

### What data do you need?
Sentiment labels for the tweets are needed. A NLP (transformer) model will be trained on approximately 7,500 randomly selected tweets and used to predict these labels on the entire corpus.

### What can you augment from external and/or public sources?
None.

## Step 4: Analysis
### What analysis needs to be done?
A binary classification ML model will be trained on all available (labeled) tweets up to but not including 2022-01-10 00:00:00. The trained model will be used on-demand to predict whether a tweet needs support from a mission team member (negative or neutral sentiment) or not (positive sentiment).

### Does it involve description, detection, prediction, or behavior change?
Prediction.

### How will the analysis be validated?
The ML model will be validated against 12.5% of randomly selected tweets currently available. These tweets will not be available for use in ML model development.

Predictions will be scored against true labels for tweets obtained from one of
- hand labeling
- NLP (transformer) model

ML model development will be performed using one of the following validation strategies
- a single validation split consisting of 12.5% of data available for use in ML model development
- multiple validation folds in K-Fold cross-validation, where each fold is 12.5% of data available for use in ML model development

A simple (naive) approach to predicting the tweet label will also be scored for comparison.
Both approaches will be compared to eachother to determine if the ML-based approach is outperforming the simple (naive) approach and thereby delivering value.

#### Choice of Evaluation Metric
False negatives (tweets that should have been responded to but were predicted to not need a response) and false positives (tweets that did not need review by a team member but were predicted as requiring a review) are the most important types of errors. So the [candidate metrics to be used to assess ML model performance](https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/) are
- F1-score (if false negatives and false positives are equally important)
- F2-score (if false negatives are more important)
- F0.5-score (if false positives are more important)

The four possible ML prediction scenarios are listed below for the prediction of the outcome of a hypothetical tweet's review status
1. TP: actual = needs support, predicted = needs support
   - sentiment is negative/neutral (needs support)
   - prediction is negative/neutral (needs support)
   - all such tweets will correctly be flagged for review by the mission team
   - there is no loss/harm incurred by this scenario
2. TN: actual = does not need support, predicted = does not need support
   - sentiment is positive (does not need support)
   - prediction is positive (does not need support)
   - all such tweets will correctly not be flagged for review by the mission team
   - there is no loss/harm incurred by this scenario
3. FN: actual = needs support, predicted = does not need support
   - sentiment is negative/neutral (needs support)
   - prediction is not negative/neutral (does not need support)
   - the loss/harm is that tweets that are potentially harmful to public image of the mission are not responded to by a mission team member, even though they should have been addressed
     - this scenario must be avoided
     - potentially harmful tweets that slip through without review by team members must be minimized
4. FP: actual = does not need support, predicted = needs support
   - sentiment is not negative/neutral (does not need support)
   - prediction is negative/neutral (needs support)
   - the loss/harm incurred is that team members unnecessarily spend time reading through tweets that are potentially not harmful to public image of the mission
     - avoiding time wasted on reading non-harmful tweets would be preferred but, with a distribued mission team, it is not the top priority
     - it would be better to spend more time reading tweets, including potentially harmless and harmful ones, than not spend the time and allow harmful ones to slip through and lead to mis-information about the mission to enter the public domain

Since FN (false negatives) are more costly than FP (false positives), the scoring metric chosen to evaluate predictions made using the ML model is [F2-score](https://machinelearningmastery.com/fbeta-measure-for-machine-learning/).

## Ethical Considerations
### What are the privacy, transparency, discrimination/equity, and accountability issues around this project and how will you tackle them?
1. No personally identifying demographic data was intentionally collected. So, demographic data will not be factor for predicting tweet sentiment.
2. User location data is missing in many tweets and so can't be used as a predictive feature during ML model development.

## Additional Considerations
### How will you deploy your analysis as a new system so that it can be updated and integrated into the organization’s operations?
If the project is a success, then an AWS Sagemaker Pipeline will be created to operationalize
- ML model training (development)
- deployment to an endpoint which can be called on-demand to make predictions

The pipeline will consist of the following steps (similar to [this official Sagemaker example](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform_outputs.ipynb))
- combine and process all existing (original run) **new** (subsequent runs) raw data (same as notebooks `3_*.ipynb` `4_process_data.ipynb`)
- create training and testing splits from all available (see `5_*.ipynb`)
- add labels using previously trained NLP model (`6_*.ipynb`)
  - this model was trained during original development and does not need to be trained again
- train a ML classification model using training data
- evaluate ML approach against naive (currently used) model using testing data
  - if ML evaluation metric indicates a success, then
    - register model
    - deploy
  - if not a success
    - fail
    - no model registration
    - no deployment
    - human intervention is needed

During each model training run that is a success, a new model will be registered in Sagemaker's model registry and this will be used by the endpoint.

### How will you evaluate the new system in the field to make sure it accomplishes your goals?
If the project is a success, then the deployed model will make inference predictions. Since the ML model would be validated during development, over an out-of-sample fraction of 12.5%, the deployed model will also be evaluated on the same fraction of new tweets (where this fraction is calcluated relative to the total - train + validation + test - length of all three data splits used during model development).

The same ML evaluation metrics used during model development (described above) will be used for evaluation in production.

### How will you monitor your system to make sure it continues to perform well over time?
By logging the model's evaluation metric (see above) on sentiment predicted during inference. If the metric is
- within a specific threshold of the metric found during development (no drift has occurred)
  - it will continue to serve inference with no changes
- not within a specific threshold of the metric found during development (drift has occurred)
  - the previously trained NLP (transformer) model will make inference predictions and these will be served to the customer
  - all available data (including the new data used to make inference) will be used to re-train a new ML model
  - a new ML model will be deployed to production
