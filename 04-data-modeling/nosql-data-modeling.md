# NoSQL Data Modeling

## What is a NoSQL data model?

It’s a model that is not reinforced by a Relational Database Management System (RDBMS). Therefore, the model isn’t explicit about how the data relates – how it all connects together.

The primary difference is that NoSQL does not use a relational data modeling technique and it emphasizes flexible design. The lack of requirement for a schema makes designing a much simpler and cheaper process. That isn’t to say that you can’t use a schema altogether, but rather that schema design is very flexible.

Another useful feature of NoSQL data models is that they are built for high efficiency and speed in terms of creating up to millions of queries a second. This is achieved through having all the data contained within one table, and so JOINS and cross-referencing is not as performance heavy. 

NoSQL is also unique in that it is horizontally scalable, compared to SQL which is only vertically scalable. With NoSQL you can simply use another shard, which is cheap, rather than buying more hardware, which is not.

## How is data stored in NoSQL?

In one of the main non-relational database models, such as a key-value store, document store, graph data model, time series store, column-oriented. Data can be stored on disk, in-memory, or both.

## Does NoSQL have a schema?

Yes, it does. When people say NoSQL is “schemaless,” they really mean the schema is flexible and determined by the developer and application needs over time. . A schema is eventually settled upon – it doesn’t exist at the onset, as is the case with a SQL database.

Since NoSQL databases don’t really have a set structure, development and schema design tends to be focused around the physical data model. That means developing for large, horizontally expansive environments, something that NoSQL excels at. Therefore, the specific quirks and problems that come with scalability are at the forefront.

As such, the first step is to define business requirements, as optimizing data access is a must, and can only be achieved by knowing what the business wants to do with the data. Your schema design should complement the workflows tied to your use case.

There are several ways to select the primary key, and ultimately that depends on the users themselves. That being said, some data might suggest a more efficient schema, especially in terms of how often that data is queried. 

## What data model does NoSQL use?

NoSQL databases fall into four main categories or types. One thing they have in common is that they do not use the rigid tabular row-and-column data model that traditional relational databases (sometimes called SQL databases) use.

Instead, NoSQL databases have a data model that reflects their particular category. Document databases can store a great deal of information in a single document and can nest documents. Key-value stores have a simple data model, just as their name implies. Wide column stores feature more variation in data types and the number of columns in use than row-oriented relational databases. Graph databases have data models based on graph theory, with data models made up of nodes and edges that relate those nodes.

## NoSQL Data Modeling Techniques

All NoSQL data modeling techniques are grouped into three major groups:

- **Conceptual techniques**
- **General modeling techniques**
- **Hierarchy modeling techniques**

Below, we will briefly discuss all NoSQL data modeling techniques.

### Conceptual Techniques

There are a three conceptual techniques for NoSQL data modeling:

- **Denormalization**. Denormalization is a pretty common technique and entails copying the data into multiple tables or forms in order to simplify them. With denormalization, easily group all the data that needs to be queried in one place. Of course, this does mean that data volume does increase for different parameters, which increases the data volume considerably.
- **Aggregates**. This allows users to form nested entities with complex internal structures, as well as vary their particular structure. Ultimately, aggregation reduces joins by minimizing one-to-one relationships.  
    Most NoSQL data models have some form of this soft schema technique. For example, graph and key-value store databases have values that can be of any format, since those data models do not place constraints on value. Similarly, another example such as BigTable has aggregation through columns and column families.
- **Application Side Joins.** NoSQL doesn’t usually support joins, since NoSQL databases are question-oriented where joins are done during design time. This is compared to relational databases where are performed at query execution time. Of course, this tends to result in a performance penalty and is sometimes unavoidable.

### General Modeling Techniques

There are a five general techniques for NoSQL data modeling:

- **Enumerable Keys**. For the most part, unordered key values are very useful, since entries can be partitioned over several dedicated servers by just hashing the key. Even so, adding some form of sorting functionality through ordered keys is useful, even though it may add a bit more complexity and a performance hit.
- **Dimensionality Reduction**. Geographic information systems tend to use **R-Tree** indexes and need to be updated in-place, which can be expensive if dealing with large data volumes. Another traditional approach is to flatten the 2D structure into a plain list, such as what is done with Geohash.  
    With dimensionality reduction, you can map multidimensional data to a simple key-value or even non-multidimensional models.  
    Use dimensionality reduction to map multidimensional data to a Key-Value model or to another non-multidimensional model.
- **Index Table.** With an index table, take advantage of indexes in stores that don’t necessarily support them internally. Aim to create and then maintain a unique table with keys that follow a specific access pattern. For example, a master table to store user accounts for access by user ID.
- **Composite Key Index**. While somewhat of a generic technique, composite keys are incredibly useful when ordered keys are used. If you take it and combine it with secondary keys, you can create a multidimensional index that is pretty similar to the above-mentioned Dimensionality Reduction technique.
- **Inverted Search – Direct Aggregation.** The concept behind this technique is to use an index that meets a specific set of criteria, but then aggregate that data with full scans or some form of original representation.  
    This is more of a data processing pattern than data modeling, yet data models are certainly affected by using this type of processing pattern. Take into account that random retrieval of records required for this technique is inefficient. Use query processing in batches to mitigate this problem.

### Hierarchy Modeling Techniques

There are a seven hierarchy modeling techniques for NoSQL data:

- **Tree Aggregation.** Tree aggregation is essentially modeling data as a single document. This can be really efficient when it comes to any record that is always accessed at once, such as a Twitter thread or Reddit post. Of course, the problem then becomes that random access to any individual entry is inefficient.
- **Adjacency Lists.** This is a straightforward technique where nodes are modeled as independent records of arrays with direct ancestors. That’s a complicated way of saying that it allows you to search nodes by their parents or children. Much like tree aggregation though, it is also quite inefficient for retrieving an entire subtree for any given node.
- **Materialized Paths.** This technique is a sort of denormalization and is used to avoid recursive traversals in tree structures. Mainly, we want to attribute the parents or children to each node, which helps us determine any predecessors or descendants of the node without worrying about traversal. Incidentally, we can store materialized paths as IDs, either as a set or a single string.
- **Nested Sets**. A standard technique for tree-like structures in relational databases, it’s just as applicable to NoSQL and key-value or document databases. The goal is to store the tree leaves as an array and then map each non-leaf node to a range of leaves using start/end indexes.  
    Modeling it in this way is an efficient way to deal with immutable data as it only requires a small amount of memory, and doesn’t necessarily have to use traversals. That being said, updates are expensive because they require updates of indexes.
- **Nested Documents Flattening: Numbered Field Names.** Most search engines tend to work with documents that are a flat list of fields and values, rather than something with a complex internal structure. As such, this data modeling technique tries to map these complex structures to a plain document, for example, mapping documents with a hierarchical structure, a common difficulty you might encounter.  
    Of course, this type of work is pain-staking and not easily scalable, especially as the nested structures increase.
- **Nested Documents Flattening: Proximity Queries.** One way to solve the potential problems with the Numbered Field Names data modeling technique is to use a similar technique called **Proximity Queries.** These limit the distance between words in a document, which helps increase performance and decrease query speed impact.
- **Batch Graph Processing.** Batch graph processing is a great technique for exploring the relationships up or down for a node, within a few steps. It is an expensive process and doesn’t necessarily scale very well. By using Message Passing and MapReduce we can carry out this type of graph processing.
