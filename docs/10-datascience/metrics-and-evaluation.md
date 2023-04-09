# Metrics and Evaluation

In general terms, metrics are tools to set standards and evaluate the performance of models. In the field of machine learning and data science, obtaining a functional model is far from enough. We need to develop methods and assessment metrics to determine how well models perform on tasks that are given. Metrics used in machine learning are formulas and equations that provide specific quantitative measurements as to how well the developed methods perform on the data provided. Evaluation refers to the process of distinguishing between the better and the worse models by comparing metrics.

There are two general categories of problems that generally describe most datasets: regression and classification. Since for each type of problem the predictions produced by models vary greatly, there’s a clear distinction between classification metrics and regression metrics. Regression metrics evaluate continuous values, while classification deals with discrete ones. However, both types of evaluation methods require two types of inputs: the ground-truth value (the desired correct prediction) and the predicted value that the model outputs.

Similar to metrics, there are loss functions. Loss functions accomplish the same goals as those of metrics: they measure the performance or, in some cases, the error for certain model predictions. Although loss functions can be used as metrics, when we refer to loss functions, it usually represents a differentiable function that can be used to train gradient-based models. Gradient descent allows the model to converge to a local optimum by exploiting the differentiability of a loss function. The goal of a loss function is to provide an informative formula that can describe a model’s error that can be utilized by gradient descent. They are generally optimal for gradient descent but not necessarily wholly intuitive from our perspective. On the other hand, metrics prioritize an intuitive explanation of how effective the model performed on the given task instead of designing a formula targeted specifically to the optimization of gradient descent.

Some metrics simply cannot act as loss functions due to their undifferentiability. While sometimes loss functions are easily interpretable on a human scale and some metrics can be considered loss functions due to their differentiability, loss functions and metrics are generally seen as different tools with somewhat similar functionality.

## Mean Absolute Error

One of the most common regression metrics is the Mean Absolute Error (MAE). In simple terms, it calculates the difference between the ground-truth labels and the predictions of the model, averaged across all predictions.

For example, imagine a class of 50 students taking an exam that is scored out of 100 points. The teacher makes assumptions about each student’s expected score based on their classwork in the past. After grading the exams, the teacher realizes that their predictions aren’t exactly correct. They want to know how much they’re off from the ground-truth values, or the actual scores that the students received. Guided by intuition, they simply calculate the difference in scores between the prediction and the students’ results. The teacher finds it helpful to see how off they were for each student, but they also want a summative, aggregate-level idea of how generally wrong the predictions were. They do this by taking the average of each of the errors:

![525591_1_En_1_Fig37_HTML](https://user-images.githubusercontent.com/62965911/230722022-2a988ed5-46b7-4212-9124-6cabcabbde99.jpeg)

## Mean Squared Error (MSE)

The Mean Absolute Error may be simple, but there are a few drawbacks. One major issue regarding MAE is that it does not punish outlier predictions. Consider two samples A1 and A2 that the model is 1% and 6% off on (absolute error divided by total possible domain value). Using the Mean Absolute Error, A2 is weighted 5% worse than A1. Now, consider two additional samples B1 and B2 that the model is 50% and 55% off on. Using the Mean Absolute Error, B2 is weighted 5% worse than B1. We should ask ourselves: Is a model degradation from 1% to 6% error the same as a model degradation from 50% to 55% error? A 50–55% error change is a lot worse than a 1–6% error change since in the latter case the model still performs reasonably well.

We can use the Mean Squared Error to disproportionately punish larger mistakes.

As the name suggests, the Mean Squared Error raises the difference between model predictions and the ground-truth label to the second power instead of taking the absolute value.

To further demonstrate, continuing with the student test score example from earlier, the teacher predicts a score of 58 instead of 83 for the student Cameron. Using the formula for MSE, we obtain 107.8. However, we do not have an intuition of how exactly the model is incorrect. Since we squared the result instead of taking the absolute value, the score we obtain doesn’t scale to the range of test scores as an average error of 107.8 is impossible for a test that’s scored between 0 and 100. To counter such an issue, we can take the square root of the result to “reverse” the operation of raising to the second power, putting the error into contextual scale while still emphasizing any outlier predictions. This metric is the Root Mean Squared Error (RMSE):

![525591_1_En_1_Fig38_HTML](https://user-images.githubusercontent.com/62965911/230722211-5a0ddf07-3ef1-484a-b3fd-0ef555a2a5fa.jpeg)

## Confusion Matrix

Like regression metrics based on the concept of MAE, most classification metrics rely on the idea of a Confusion Matrix, which describes how much error is made and what type of error with a convenient visualization.

A Confusion Matrix has four components that describe model predictions compared against the ground-truth labels; they are true positives, false positives, true negatives, and false negatives. Let’s break down this terminology: the first word indicates whether the model prediction was correct or not (“true” if correct, “false” if not); the second indicates the ground-truth value (“positive” for the label 1 and “negative” for the label 0).

Let’s better understand these concepts with real-life examples. Say that a doctor is diagnosing possible cancerous patients based on their screening results. If the doctor deduces that an actual cancerous patient does in fact have cancer, it’s an example of a true positive. When the model, or in this case the doctor, predicts the positive class of being cancerous and the actual ground-truth label of whether the patient has cancer or not ends up positive too, it’s called a true positive. However, the doctor is not accurate every single time. When the doctor predicts the patient is not cancerous while the patient in fact has cancer, it’s an example of a false negative. When the doctor concludes that a patient is cancerous but in truth the patient is healthy, it’s an example of a false positive. If a patient is healthy and the doctor predicts healthy too, it’s an example of a true negative.

Let’s summarize these concepts into numeric language:
- When the model prediction is 1 and the ground truth is 1, it’s a true positive.
- When the model prediction is 1 and the ground truth is 0, it’s a false positive.
- When the model prediction is 0 and the ground truth is 0, it’s a true negative.
- When the model prediction is 0 and the ground truth is 1, it’s a false negative.

After we’ve identified all the cases of this within our model prediction against the ground-truth labels, we can conveniently organize these values into a matrix form, thus the name Confusion Matrix:

![525591_1_En_1_Fig39_HTML](https://user-images.githubusercontent.com/62965911/230722287-9be25aad-7666-4b55-9506-aa1b51c85c81.jpeg)

## Accuracy

One of the most straightforward ways to evaluate the performance of a classification model is accuracy. Accuracy is simply the percentage of values that the model predicted correctly. In more technical terms, it’s the number of true positives plus the number of true negatives divided by the number of all the prediction values.

## Precision

On the contrary, precision considers the issue of class imbalance in data. Precision calculates the accuracy only within all predicted positive classes, or the number of true positives divided by the sum of true positives and false positives. This will punish models that perform poorly on the positive class in an imbalanced dataset with a large number of negative values.

## Recall

Recall score, or the true positive rate, is slightly different from precision as instead of calculating the accuracy of when the model predicts positive, it returns the accuracy of the positive class as a whole. Recall cleverly solves the problem of accuracy by only calculating the correctness in the positive class or the percentage of true positives across all positive labels. The recall metric is useful when we only care about our model predicting the positive class accurately. For example, when diagnosing cancer and most diseases, avoiding having false negatives is much more crucial than avoiding having false positives when resources are limited to develop a perfect model. In cases like such, we would be optimizing for a higher recall as we want the model to be as accurate as possible, especially in predicting the positive class.

## F1 Score

The intuition behind the F1 score is creating a universal metric that measures the correctness of the positive class while having both the advantages of precision and recall. Thus, the F1 score is the harmonic mean between precision and recall. Note we used harmonic mean here since precision and recall are expressed as percentages/rates.

## Area Under the Receiver Operating Characteristics Curve (ROC-AUC)

Although the F1 score accounts for both the advantages of precision and recall, it only measures the positive class. Another major issue of the F1 score along with precision and recall is that we’re inputting binary values for evaluation. Those binary values are determined by a threshold, converting probabilities to binary targets usually during model predictions. In most cases, 0.5 is chosen as the threshold for converting probabilities to binary targets. This not only might not be the optimal threshold, but it also decreases the amount of information that we receive from the output as probabilities also show how confident the model is in its prediction. The Receiver Operating Characteristics (ROC) curve solves these issues cleverly: it plots the true positive rate against the false positive rate for various thresholds.

The true positive rate, or recall, gives us how many predictions are correct among all predicted positive labels, or the probability that the model will be correct when the prediction is positive. The false positive rate calculates the number of false negatives within the negative prediction. In sense, it gives a probability that the model will be incorrect when the prediction is negative. The ROC curve visualizes the values of both measurements on different thresholds, generating a plot where we can see what threshold gives the best values for true positive rate/false positive rate.

Furthermore, calculating the area under the curve (AUC) provides a measurement of how well the model distinguishes between classes. An area of 1 indicates a perfect distinction between classes, thus producing correct predictions. An area of 0 indicates complete opposite predictions, meaning that all predictions are reversed between 1 and 0 (labels – 1). An area of 0.5 represents complete random prediction where the model cannot distinguish between classes at all.