# Experiments Tracking, Model Management, and Dataset Versioning

Training DL models is an iterative process that consumes a lot of time and resources. Therefore, keeping track of all experiments and consistently organizing them can prevent us from wasting our time on unnecessary operations such as training similar models repeatedly on the same set of data. In other words, having well-documented records of all model architectures and their hyperparameter sets, as well as the version of data used during experiments, can help us derive the right conclusion from the experiments, which naturally leads to the project being successful.

The essential components of **DL project tracking** are **experiment tracking**, **model management**, and **dataset versioning**. Let’s look at each component in detail.

## **Experiment tracking**

The concept behind experiment tracking is simple: store the description and the motivations of each experiment so that we don’t run another set of experiments for the same purpose. Overall, effective experiment tracking will save us operational costs and allows us to derive the right conclusion from a minimal set of experimental results. One of the basic approaches for effective experiment tracking is adding a unique identifier to each experiment. The information we need to track for each experiment includes project dependencies, the definition of the model architecture, parameters used, and evaluation metrics. Experiment tracking also includes visualizing ongoing experiments in real time and being able to compare a set of experiments intuitively. For example, if we can check train and validation losses from every epoch as the model gets trained, we can identify overfitting quicker, saving some resources. Also, by comparing results and a set of changes made between two experiments, we can understand how the changes affect the model performance.

## **Model management**

Model management goes beyond experiment tracking as it covers the full life cycle of a model: dataset information, artifacts (any data generated from training a model), the implementation of the model, evaluation metrics, and pipeline information (such as development, testing, staging, and production). Model management allows us to quickly pick up the model of interest and efficiently set up the environment in which the model can be used.

## **Dataset versioning**

The last component of DL project tracking is dataset versioning. In many projects, datasets change over time. Changes can come from data schemas (blueprints of how the data is organized), file locations, or even from filters applied to the dataset manipulating the meaning of the underlying data. Many datasets found in the industry are structured in a complex way and often stored in multiple locations in various data formats. Therefore, changes can be more dramatic and harder to track than you anticipated. As a result, keeping a record of the changes is critical in reproducing consistent results throughout the project.

Dataset tracking can be summarized as follows: a set of data stored as an artifact should become a new version of the artifact whenever the underlying data is modified. Having said that, every artifact should have metadata that consists of important information about the dataset: when it is created, who created it, and how it is different from the previous version.

We introduce a set of useful tools for experiments tracking, model management, and dataset versioning which enables effective management of DL projects. The tools we will be discussing help us in tracking a large number of experiments and interpreting the results more efficiently which naturally leads to a reduction in operational costs and boost the development cycle.

*	[Weights & Biases](https://wandb.ai/site/experiment-tracking)
*	[MLflow](https://mlflow.org/docs/latest/tracking.html)
*	[SageMaker Studio](https://aws.amazon.com/sagemaker/studio/)
*	[Kubeflow](https://www.kubeflow.org/)
*	[Neptune](https://neptune.ai/product)
*	[Comet](https://www.comet.ml/site/data-scientists/)
*	[Polyaxon](https://polyaxon.com/)
*	[Valohai](https://valohai.com/product/)

## DL project tracking with Weights & Biases

[Weights & Biases (W&B)](https://wandb.ai/site/experiment-tracking) is an experiment management platform that provides versioning on models and data. One of the key advantages of W&B comes from its interactive dashboard. It is available as a stand-alone webpage, but you can also embed it into your Jupyter notebook.

In order to use W&B, you need to install and link your account. The details can be found [here](https://docs.wandb.ai/quickstart)
```
pip install wandb
wandb login
```

In the notebook, [W&B.ipynb](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/blob/main/Chapter_4/W%26B.ipynb), we describe how to use W&B for tracking a model training.

## DL project tracking with MLflow and DVC

Mlflow is a popular framework that supports tracking technical dependencies, model parameters, metrics, and artifacts. The key components of Mlflow include
*	Tracking – keeping track of results changes every time model is run
*	Projects – packaging model code in a reproducible way
*	Models – packaging model artifacts for future convenient deployment
*	Model Registry – managing a full lifecycle of an Mlflow Model
*	Plugins – API allowing writing integration plugins with different DL frameworks and backends

#### Experiments tracking with MLFlow

The following command will download mlflow

```
pip install mlflow
```

To start UI locally simply type:

```
mlflow ui
```

and navigate to the address displayed in the row "Listening at:

```
[INFO] Listening at: http://127.0.0.1:5000
```

if you are doing this for a first time, you will see UI with default page without any experiments. 

![](mlflow_ui.png)

A few examples of basics of experiment tracking with MLflow are presented [here](mlflow.ipynb) 

#### Experiments tracking with MLFlow and DVC

Installing dvc can be achived by running the following commands

```
pip install dvc
```

In the notebook, [mlflow.ipynb](dvc_mlflow.ipynb), we first introduce common dvc operations. Then, we describe how to use MLFlow and DVC together for tracking a model training.
