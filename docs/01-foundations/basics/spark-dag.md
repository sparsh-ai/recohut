# Interpreting a Spark DAG

A DAG is just a regular graph with nodes and edges but with no cycles or loops. In order to understand a Spark DAG, we first have to understand where a DAG comes into the picture during the execution of a Spark job.

When a user submits a Spark job, the Spark driver first identifies all the tasks involved in accomplishing the job. It then figures out which of these tasks can be run in parallel and which tasks depend on other tasks. Based on this information, it converts the Spark job into a graph of tasks. The nodes at the same level indicate jobs that can be run in parallel, and the nodes at different levels indicate tasks that need to be run after the previous nodes. This graph is acyclic, as denoted by *A* in DAG. This DAG is then converted into a physical execution plan. In the physical execution plan, nodes that are at the same level are segregated into stages. Once all the tasks and stages are complete, the Spark job is termed as completed.

Let's look at what a DAG looks like. You can access a Spark DAG from the Spark UI. Just click on any of the job links and then click on the **DAG Visualization** link.

Here is a DAG for a simple word count problem:

![B17525_13_024](https://user-images.githubusercontent.com/62965911/218313245-4835191c-3363-48ec-a246-97b85b434a52.jpg)

In the first stage, we see that the word count has three steps and a reduce step in the next stage. Ignore the stage numbers, as Spark assigns consecutive numbers for all jobs that are run in that Spark session. So, if you have run any other job before this job, the number gets sequentially incremented. Here is some further information about each task:

- The **textFile** task corresponds to the reading of the file from the storage.
- The **flatMap** task corresponds to the splitting of the words.
- The **map** task corresponds to the formation of (**word**, **1**) pairs.
- The **reduceByKey** task corresponds to the aggregation of all the (word, 1) pairs together to get the sum of each distinct word.

You can get more details about each step by clicking on the **Stage** boxes. Here is an example of a detailed view of **Stage 12** from the previous screenshot:

![B17525_13_025](https://user-images.githubusercontent.com/62965911/218313250-cb765fa4-f16f-4cbe-aaf1-16233287c00c.jpg)

The main advantage of learning to read Spark DAGs is that they help you identify bottlenecks in your Spark queries. You can identify how much data movement is happening between stages (also known as **data shuffle**), if there are too many sequential stages, if there are slow stages in the critical path, and so on.

You can learn more about Spark DAGs here: [https://spark.apache.org/docs/3.0.0/web-ui.html](https://spark.apache.org/docs/3.0.0/web-ui.html).