# Data Splits

## Training and Validation sets

The ecommerce platform randomly splits the customer data into a train dataset and a validation dataset (in this example, with a 0.6 “train split,” meaning that 60% of the original dataset with labels is placed in the training set). They train the model on the training set and evaluate it on the validation data to obtain an honest report of its performance. If they’re not satisfied with the model’s validation performance, they can tweak the modeling system.

![525591_1_En_1_Fig11_HTML](https://user-images.githubusercontent.com/62965911/230721324-c2616c84-f8af-4b79-a674-9556e4a352af.png)

## K-fold Evaluation

In this evaluation schema, the dataset is randomly split into k folds (equally sized sets). For each of the k folds, we train a model from scratch on the other k – 1 folds and evaluate it on that fold. Then, we average (or aggregate through some other method) the validation performance for each of the k-folds.

![525591_1_En_1_Fig19_HTML](https://user-images.githubusercontent.com/62965911/230721452-10c15eff-69c5-49c8-a2e5-526e6f30b9ba.png)

This method allows us to obtain model validation performance on the “entire” dataset. However, note that it may be expensive to train k models – an alternative is simply to randomly split into training and validation sets without a random seed a given number of times without regard for which specific parts of data are allocated into either set.

This approach is also known as k-fold cross-validation, because it allows us to validate our model across the entire dataset.