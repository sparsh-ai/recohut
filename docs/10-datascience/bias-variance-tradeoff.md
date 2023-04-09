# Bias-Variance Trade-Off

Bias is a model’s ability to identify general trends and ideas in the dataset, whereas variance is the ability to model data with high precision. Since we think of bias and variance in terms of error, a lower bias or variance is better. The bias-variance relationship is often visualized as a set of dart throws on a bull’s-eye. The ideal set of throws is a cluster of hits all around the center ring, which is low bias (the general “center” of the throws is not shifted off/biased) and low variance (the collection of hits are clustered together rather than far out, indicating consistently good performance).

![525591_1_En_1_Fig22_HTML](https://user-images.githubusercontent.com/62965911/230721537-ed3988e5-349c-48c6-8ad6-7ed334d8a237.png)

The bias-variance relationship lends itself to the concept of underfitting vs. overfitting. A model underfits when its bias is too high, while its variance is too low; the model doesn’t adapt/bend too much at all toward specific data instances of the dataset and thus poorly models the training dataset. On the other hand, a model overfits when its bias is too low and the variance is too high; the model is incredibly sensitive to the specific data instances it is presented with, passing through every point.

Models that overfit perform exceedingly well on the training set but very poorly on the validation dataset, since they “memorize” the training dataset without generalizing.

Generally, as model complexity increases (can be measured roughly as number of parameters – although other factors are important), bias error decreases, and variance error increases. This is because the increased number of parameters allows the model greater “movement” or “freedom” to fit to the specifics of the given training dataset. (Thus, higher-degree polynomials with a larger number of coefficients are generally associated with higher-variance overfitting behavior, and lower-degree polynomials with a smaller number of coefficients are generally associated with higher-bias underfitting behavior.)

The ideal model for a problem is one that minimizes the overall error by balancing the bias and variance errors:

![525591_1_En_1_Fig23_HTML](https://user-images.githubusercontent.com/62965911/230721610-f89759cd-b67a-4a06-ae7a-1a50e45ad025.png)