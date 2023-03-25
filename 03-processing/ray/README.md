# Ray

## What is Ray?

Ray is a great computing framework for the Python data science community because it is flexible and distributed, making it easy to use and understand. It allows you to efficiently parallelize Python programs on your own computer and run them on a cluster without much modification. Additionally, its high-level libraries are easy to set up and can be used together smoothly, and some of them, such as the reinforcement learning library, have a promising future as standalone projects. Even though its core is written in C++, Ray has always been focused on Python and integrates well with many important data science tools. It also has a expanding ecosystem.

Ray is not the first framework for distributed Python, nor will it be the last, but it stands out for its ability to handle custom machine learning tasks with ease. Its various modules work well together, allowing for the flexible execution of complex workloads using familiar Python tools. This book aims to teach how to use Ray to effectively utilize distributed Python for machine learning purposes.

Programming distributed systems can be challenging because it requires specific skills and experience. While these systems are designed to be efficient and allow users to focus on their tasks, they often have "leaky abstractions" that can make it difficult to get clusters of computers to work as desired. In addition, many software systems require more resources than a single server can provide, and modern systems need to be able to handle failures and offer high availability. This means that applications may need to run on multiple machines or even in different data centers in order to function reliably.

Even if you are not very familiar with machine learning (ML) or artificial intelligence (AI), you have probably heard about recent advances in these fields. Some examples of these advances include Deepmind's Alpha-Fold, which is a system for solving the protein folding problem, and OpenAI's Codex, which helps software developers with the tedious parts of their job. It is commonly known that ML systems require a lot of data to be trained and that ML models tend to become larger. OpenAI has demonstrated that the amount of computing power needed to train AI models has been increasing exponentially, as shown in their paper "AI and Compute." In their study, the operations needed for AI systems were measured in petaflops (thousands of trillion operations per second) and have doubled every 3.4 months since 2012.

While Moore's Law suggests that computer transistors will double every two years, the use of distributed computing in machine learning can significantly increase the speed at which tasks are completed. While distributed computing may be seen as challenging, it would be beneficial to develop abstractions that allow for code to run on clusters without constantly considering individual machines and their interactions. By focusing specifically on AI workloads, it may be possible to make distributed computing more accessible and efficient.

## Core, Libraries and Ecosystem

![1](https://user-images.githubusercontent.com/62965911/226094436-823ccc97-832e-4069-b232-52bb61ca3930.png)

## Ray AIR and the Data Science Workflow

Ray has dedicated libraries for each of the four ML-specific steps. Specifically, you can take care of your data processing needs with _Ray Datasets_, run distributed model training with _Ray Train_, run your reinforcement learning workloads with _Ray RLlib_, tune your hyperparameters efficiently with _Ray Tune_, and serve your models with _Ray Serve_. And the way Ray is built, all these libraries are _distributed by design_.

What’s more is that all of these steps are part of a process and are rarely tackled in isolation. Not only do you want all the libraries involved to seamlessly interoperate, it can also be a decisive advantage if you can work with a consistent API throughout the whole data science process. This is exactly what Ray AIR was built for: having a common runtime and API for your experiments and the ability to scale your workloads when you’re ready.

### Data Processing with Ray Datasets

The first high-level library of Ray we’ll talk about is Ray Datasets. This library contains a data structure aptly called Dataset, a multitude of connectors for loading data from various formats and systems, an API for transforming such datasets, a way to build data processing pipelines with them, and many integrations with other data processing frameworks. The Dataset abstraction builds on the powerful Arrow framework.

### Reinforcement learning with Ray RLlib

Let’s start with _Ray RLlib_ for reinforcement learning (RL). This library is powered by the modern ML frameworks TensorFlow and PyTorch, and you can choose which one to use. Both frameworks seem to converge more and more conceptually, so you can pick the one you like most without losing much in the process.

### Distributed training with Ray Train

Ray RLlib is dedicated to reinforcement learning, but what do you do if you need to train models for other types of machine learning, like supervised learning? You can use another Ray library for distributed training in this case: _Ray Train_.

### Hyperparameter tuning with Ray Tune

Naming things is hard, but _Ray Tune_, which you can use to tune all sorts of parameters, hits the spot. It was built specifically to find good hyperparameters for machine learning models. The typical setup is as follows:

- You want to run an extremely computationally expensive training function. In ML, it’s not uncommon to run training procedures that take days, if not weeks, but let’s say you’re dealing with just a couple of minutes.
- As a result of training, you compute a so-called objective function. Usually you want to either maximize your gains or minimize your losses in terms of performance of your experiment.
- The tricky bit is that your training function might depend on certain parameters, called hyperparameters, that influence the value of your objective function.
- You may have a hunch what individual hyperparameters should be, but tuning them all can be difficult. Even if you can restrict these parameters to a sensible range, it’s usually prohibitive to test a wide range of combinations. Your training function is simply too expensive.
    
What can you do to efficiently sample hyperparameters and get “good enough” results on your objective? The field concerned with solving this problem is called _hyperparameter optimization_ (HPO), and Ray Tune has an enormous suite of algorithms for tackling it.

### Model Serving with Ray Serve

The last of Ray’s high-level libraries we’ll discuss specializes in model serving and is simply called Ray Serve.

### :microscope: Lab: Ray AIR Basics

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/03-processing/ray/lab-ray-air-basics.ipynb)

In this lab, we are learning all 4 high-level APIs of Ray AIR with some examples.

## Ray Core

### Ray Core Major API methods

| API call      | Description                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| `ray.init()`  | Initializes your Ray Cluster. Pass in an `address` to connect to an existing cluster.                              |
| `@ray.remote` | Turns functions into tasks and classes into actors.                                                                |
| `ray.put()`   | Puts values into Ray’s object store.                                                                               |
| `ray.get()`   | Gets values from the object store. Returns the values you’ve `put` there or that were computed by a task or actor. |
| `.remote()`   | Runs actor methods or tasks on your Ray Cluster and is used to instantiate actors.                                 |
| `ray.wait()`  | Returns two lists of object references, one with finished tasks we’re waiting for and one with unfinished tasks.   |

### Ray Core API System Components

![3](https://user-images.githubusercontent.com/62965911/226097632-1ab3c123-7c91-470e-a7fe-ea89e4aca0a7.png)

### :microscope: Lab: Ray Core Basics

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/03-processing/ray/lab-ray-api-basics.ipynb)

- Recipe 1: Your first Ray API example
- Recipe 2: Running A MapReduce Example