# Logistic Regression

The logistic function first appeared in Pierre Francois Verhulst’s publication “Correspondance mathmematique et physique” in 1838. Then later in 1845, a more detailed version of the logistic function was published by him. However, the first practical application of such a function wasn’t apparent until 1943 when Wilson and Worcester used the logistic function in bioassay. In the following years, various advances were made toward the function, but the original logistic function is used for Logistic Regression. The Logistic Regression model found its use not only in areas related to biology but also widely in social science.

Among many variants, the general goal of Logistic Regression remains the same: classification based on explanatory variables or features provided. It utilizes the sample principles of Linear Regression.

The logistic function is a broad term referring to a function with various adjustable parameters. However, Logistic Regression only uses one set of parameters, turning the function into what’s referred to as a sigmoid function. The sigmoid function is known to have an “S”-shaped curve with two horizontal asymptotes at y = 1 and y = 0. In other words, any value inputted to the function will be “squished” between 1 and 0.

![525591_1_En_1_Fig51_HTML](https://user-images.githubusercontent.com/62965911/230723774-187d4577-01f3-4974-b4a3-f31e9c27f34b.png)

Although there are other variants of the sigmoid function that restrain the output at different values, such as the hyperbolic tangent function in which the output values are restrained between –1 and 1, binary classification on Logistic Regression uses the sigmoid function.

Logistic Regression operates on the same principles as those of Linear Regression, finding an equation that graphs a “line of best fit” of the data. In this case, the “line of best fit” will take the shape of the sigmoid function, while the labels are binary labels sitting either at y = 0 or y = 1.

Although the process of gradient descent for Logistic Regression is the same as that of Linear Regression, the cost function would be different. MSE calculates the difference between two values in a regression-like situation. While it may be able to learn under classification situations, there are better cost functions where it suits the problem. The output of this function is probability values ranging from 0 to 1, while our labels are discrete binary values. Instead of MSE, our cost function will be the log loss or sometimes called the binary cross-entropy (BCE).