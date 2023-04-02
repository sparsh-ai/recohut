# Map Reduce

Knowing that answering the *how* question is what is important to understanding big data, the first question we need to answer is how does it actually store the data? What makes it different from non-big data storage?

The word *big* in big data is relative. For example, say you analyze Twitter data and then download the data as JSON files with a size of 5 GB, and your laptop storage is 1 TB with 16 GB memory.

I don't think that's big data. But if the Twitter data is 5 PB, then it becomes big data because you need a special way to store it and a special way to process it. So, the key is not about whether it is social media data or not, or unstructured or not, which sometimes many people still get confused by. It's more about the size of the data relative to your system.

Big data technology needs to be able to distribute the data in multiple servers. The common terminology for multiple servers working together is a cluster. I'll give an illustration to show you how a very large file can be distributed into multiple chunks of file parts on multiple machines:

![B16851_01_10](https://user-images.githubusercontent.com/62965911/219039802-98a7e299-d0cc-49d0-bd49-878490df57cc.jpeg)

*Figure - Distributed filesystem*

In a distributed filesystem, a large file will be split into multiple small parts. In the preceding example, it is split into nine parts, and each file is a small 128 MB file. Then, the multiple file parts are distributed into three machines randomly. On top of the file parts, there will be metadata to store information about how the file parts formed the original file, for example, a large file is a combination of file part 1 located in machine 1, file part 2 located in machine 2, and more.

The distributed parts can be stored in any format that isn't necessarily a file format; for example, it can be in the form of data blocks, byte arrays in memory, or some other data format. But for simplicity, what you need to be aware of is that in a big data system, data can be stored in multiple machines and in order to optimize performance, sometimes you need to think about how you want to distribute the parts. 

After we know data can be split into small parts on different machines, it leads to further questions:

- How do I process the files?
- What if I want to aggregate some numbers from the files?
- How does each part know the records value from other parts while it is stored in different machines?

There are many approaches to answer these three questions. But one of the most famous concepts is MapReduce. 

***A quick look at how to process multiple files using MapReduce***

Historically speaking, **MapReduce** is a framework that was published as a white paper by Google and is widely used in the Hadoop ecosystem. There is an actual open source project called MapReduce mainly written in Java that still has a large user base, but slowly people have started to change to other distributed processing engine alternatives, such as **Spark**, **Tez**, and **Dataflow**. But MapReduce as a concept itself is still relevant regardless of the technology. 

In a short summary, the word MapReduce can refer to two definitions: 

- MapReduce as a technology
- MapReduce as a concept

What is important for us to understand is MapReduce as a concept. MapReduce is a combination of two words: map and reduce. 

Let's take a look at an example, if you have a file that's divided into two file parts:

![B16851_01_11](https://user-images.githubusercontent.com/62965911/219039818-28f03250-b0e9-410d-ba13-f7786f45fc23.jpeg)

*Figure - File parts*

Each of the parts contains one or more words, which in this example are fruit. The file parts are stored on different machines. So, each machine will have these three file parts:

- File **Part 1** contains two words: **Banana** and **Apple**.
- File **Part 2** contains three words: **Melon**, **Apple**, and **Banana**.
- File **Part 3** contains one word: **Apple**.

How can you write a program to calculate a word count that produces these results?

- **Apple** = 3 
- **Banana** = 2
- **Melon** = 1

Since the file parts are separated in different machines, we cannot just count the words directly. We need MapReduce. Let's take a look at the following diagram, where file parts are *mapped*, *shuffled*, and lastly *reduced* to get the final result:

![B16851_01_12](https://user-images.githubusercontent.com/62965911/219039824-8c15e566-84a1-4c88-98dd-3607a5c07f46.jpeg)

*Figure - MapReduce step diagram*

There are four main steps in the diagram:

1. **Map**: Add to each individual record a static value of 1. This will transform the word into a key-value pair when the value is always 1.
2. **Shuffle**: At this point, we need to move the fruit words between machines. We want to group each word and store it in the same machine for each group.
3. **Reduce**: Because each fruit group is already in the same machine, we can count them together. The **Reduce** step will sum up the static value 1 to produce the count results.
4. **Result**: Store the final results back in the single machine. 

The key idea here is to process any possible process in a distributed manner. Looking back at the diagram, you can imagine each box on each step is a different machine. 

Each step, **Map**, **Shuffle**, and **Reduce**, always maintains three parallel boxes. What does this mean? It means that the processes happened in parallel on three machines. This paradigm is different from calculating all processes in a single machine. For example, we can simply download all the file parts into a pandas DataFrame in Python and do a count using the pandas DataFrame. In this case, the process will happen in one machine.

MapReduce is a complex concept. The concept is explained in a 13-page-long document by Google. You can find the document easily on the public internet. In this book, I haven't added much deeper explanation about MapReduce. In most cases, you don't need to really think about it; for example, if you use BigQuery to process 1 PB of data, you will only need to run a SQL query and BigQuery will process it in a distributed manner in the background.

As a matter of fact, all technologies in cloud that we generally use are highly scalable and without question able to handle big data out of the box. But understanding the underlying concepts helps you as a data engineer in many ways, for example, choosing the right technologies, designing data pipeline architecture, troubleshooting, and improving performance.