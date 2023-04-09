# Gradient Boosting

Gradient Boosting describes a certain technique in modeling with a variety of different algorithms that are based upon it. The first successful algorithm that utilizes Gradient Boosting is AdaBoost (Adaptive Gradient Boosting) in 1998 formulated by Leo Breiman. In 1999, Jerome Friedman composed the generalization of boosting algorithms emerging at this time, such as AdaBoost, into a single method: Gradient Boosting Machines. Quickly, the idea of Gradient Boosting Machines became extremely popular and proved to be high performing in many real-life tabular datasets. To this day, various Gradient Boosting algorithms such as AdaBoost, XGBoost, and LightGBM are the first choice for many data scientists operating on large, difficult datasets.

Gradient Boosting operates on similar ideas to those of Random Forest, using an ensemble of weaker models to build one, strong prediction. What differentiates Gradient Boosting from Random Forest is that instead of having individual, uncorrelated models, Gradient Boosting constructs models that are based on others’ errors to continuously “boost” the performance.

Say you’re picking a team of five people to represent your school, organization, or country at a trivia tournament in which the team that can answer the most questions about music, history, literature, mathematics, science, etc. wins. What is your strategy? You could pick five people who each have broad and overlapping knowledge of most topics likely to be covered (a Random Forest–style ensembling approach). Perhaps a better approach is to pick a person A who’s really good in one area, then pick and train person B on the topics that person A isn’t a specialist in, then pick and train person C on the topics that person B isn’t a specialist in, and so on. By boosting learners on top of each other, we can build sophisticated and adaptive ensembles.

The concept of Gradient Boosting can be adapted to many different machine learning models such as Linear Regression, Decision Trees, and even deep learning methods. However, the most common use of Gradient Boosting is in conjunction with Decision Trees or tree-based methods in general. Although there have emerged various popular Gradient Boosting models, their initial and core intuition relies on the same algorithm; thus, we will be analyzing the original Gradient Boosting process while briefly going over the differences in each specific type of Boosting model.

Gradient Boosting naively adapts to both regression and classification. We can start by understanding the regression approach first as demonstrated in the following figure:

1. Assuming the target variable is continuous, create a leaf with the average of the targets, which represents our initial guess of the labels.
2. Build a Regression Tree based on the errors of the first leaf. More specifically
    - Calculate the error between our initial prediction and ground-truth labels for every sample, which we refer to as pseudo residuals.
    - Construct a Regression Tree to predict the pseudo residuals of samples with a restricted number of leaves. Replace leaves with more than one label with the average of all labels that are in the leaf, which will be the prediction for that leaf.
3. Predict the target variables with a trained Decision Tree as follows:
    - Start with the initial prediction, which is the average of all labels.
    - Predict pseudo residuals using the Decision Trees we trained.
    - Add predictions to the initial guess multiplied by a factor that we refer to as the learning rate, which becomes the final prediction.
4. Calculate new pseudo residuals based on the prediction of the previous model(s).
5. Construct a new tree to predict the new pseudo residuals, repeating steps 2–4. For step 3, we simply add the new tree’s prediction and multiply by the same learning rate along with other trees that were created in previous iterations.
6. Repeat steps 2–4 until the maximum specified models are reached or the predictions start to worsen.
    
![525591_1_En_1_Fig59_HTML](https://user-images.githubusercontent.com/62965911/230726029-f8fa6cc3-52f1-480c-9f61-cb19d97009f7.jpeg)

The approach for Gradient Boosting classification is extremely like regression. During our first initial “guess,” instead of the average across targets, we compute the log odds on the labels. In order to calculate the pseudo residuals, we convert the log odds to probability using the sigmoid function.

## AdaBoost

Adaptive Gradient Boosting, or AdaBoost, is one of the earliest forms of Gradient Boosting. It was published before the generalization of Gradient Boosting Machines was proposed. The main idea that drives AdaBoost lies in the fact it uses weighted stumps, which combine into the final prediction. A stump is a Decision Tree with a root and only two leaves.

## XGBoost

XGBoost, short for Extreme Gradient Boosting, was developed in the early 2010s as a regularized variation of Gradient Boosting Machines. The development of XGBoost began as a research project by Tianqi Chen as part of the Distributed Machine Learning Community. It was then later popularized to the Machine Learning and Data Science Community during the Higgs Boson Machine Learning competition in 2014. Compared with AdaBoost, XGBoost is a lot more optimized for speed and performance and closely resembles the original approach of Gradient Boosting Machines.

## LightGBM

LightGBM, short for Light Gradient Boosting Machines, is an optimized Gradient Boosting algorithm that aims for reduced memory usage and speed while keeping the performance high. Developed by Microsoft in 2016, LGBM quickly gained popularity due to the advantages stated above along with its capability of handling large-scale data with parallel computing on GPUs.

One major difference between LGBM and other similar Gradient Boosting algorithms is the fact that Decision Trees grow leaf-wise in LGBM, while in other cases they grow level-wise. Leaf-wise growth handles overfitting better than level-wise and is much faster when operating on large datasets. Additionally, level-wise growth produces many unnecessary leaves and nodes. In contrast, leaf-wise growth only expands on nodes with high performance, thus keeping the number of decision nodes constant.

Furthermore, LGBM samples the datasets using two novel techniques known as Gradient-Based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB), which reduce the size of the dataset without affecting performance.

GOSS samples the dataset aiming for the model to focus on data points where there’s a larger error. By the concept of gradient descent, samples with lower gradients produce lower training error and vice versa. GOSS selects samples with a greater absolute gradient. Note that GOSS also chooses samples that have relatively lower gradients as it keeps the distribution of the output data like before GOSS.

The goal of EFB is to eliminate, or more appropriately merge, features. The algorithm bundles features that are mutually exclusive, meaning that they could never be of the same value simultaneously. The bundled features are then converted to a single feature, reducing the size and dimensionality of the dataset.

Finally, LGBM performs binning on continuous features to decrease the number of possible splits during Decision Tree building, introducing another major speedup to the algorithm.
