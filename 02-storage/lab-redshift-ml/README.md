# Amazon Redshift ML

In this Lab, we will Create, Train and Deploy Multi Layer Perceptron (MLP) models using Amazon Redshift ML.

Here we use the Credit Card Fraud detection data available at https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud to create, train and deploy MLP model which
can be used further to identify fraudulent transactions from the newly captured transaction records.

For that, we have downloaded the dataset from the mentioned URL and identified the schema of the CSV file that comes with the downloaded content.

We first create a table in Amazon Redshift which should hold the data.
One can even keep this CSV file in S3, crawl it using AWS Glue and/or catalog it using Amazon Athena to prepare an external table which can be queried for training the MLP model.

Here we choose the option to create a table inside the Amazon Redshift cluster (or Amazon Redshift serverless endpoint).

This is the code we use for training the fraud-detection MLP model:

```sh
CREATE model creditcardsfrauds_mlp
FROM (select * from creditcardsfrauds where txtime < 120954)
TARGET class 
FUNCTION creditcardsfrauds_mlp_fn
IAM_ROLE DEFAULT
MODEL_TYPE MLP
SETTINGS (
      S3_BUCKET '<<your-amazon-s3-bucket>>'',
      MAX_RUNTIME 54000
);
```