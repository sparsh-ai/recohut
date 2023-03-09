# Apache Beam

## Steps

1. [Lab: Getting Started with Apache Beam](./getting-started/)
2. [Lab: MapReduce in Beam (Python)](./lab-gcp-beam-mapreduce.md)

## Note

### What is apache beam?

Apache Beam is a library for parallel data processing. Beam is commonly used for Extract, Transform, and Load (ETL), batch, and stream processing. It does particularly well with large amounts of data since it can use mutliple machines to process everything at the same time.

Apache Beam comprises four basic features:

1. Pipeline - Pipeline is responsible for reading, processing, and saving the data. This whole cycle is a pipeline starting from the input until its entire circle to output. Every Beam program is capable of generating a Pipeline.
2. PCollection - It is equivalent to RDD or DataFrames in Spark. The pipeline creates a PCollection by reading data from a data source, and after that, more PCollections keep on developing as PTransforms are applied to it.
3. PTransform - Each PTransform on PCollection results in a new PCollection making it immutable. Once constructed, you will not be able to configure individual items in a PCollection. A transformation onPCollection will result in a new PCollection. The features in a PCollection can be of any type, but all must be of the same kind. However, to maintain disseminated processing, Beam encodes each element as a byte string so that Beam can pass around items to distributed workers.
4. Runner - It determines where this pipeline will operate.

In Beam, your data lives in a **`PCollection`**, which stands for *Parallel Collection*. A `PCollection` is like a **list of elements**, but without any order guarantees. This allows Beam to easily parallelize and distribute the `PCollection`'s elements.

![](https://user-images.githubusercontent.com/62965911/214567888-83bb1b64-45dd-41fb-b1bf-ba59abf8ed08.png)

Once you have your data, the next step is to transform it. In Beam, you transform data using **`PTransform`**s, which stands for *Parallel Transform*. A `PTransform` is like a **function**, they take some inputs, transform them and create some outputs.

![](https://user-images.githubusercontent.com/62965911/214567899-4f8efbd8-2cc2-49b4-906f-dbc9045fc02e.png)

We pass the elements from step1 through step3 and save the results into `outputs`.

```py
outputs = pipeline | step1 | step2 | step3
```

This is equivalent to the example above.

```py
outputs = (
  pipeline
  | step1
  | step2
  | step3
)
```

Also, Beam expects each transform, or step, to have a unique *label*, or description. This makes it a lot easier to debug, and it's in general a good practice to start. You can use the *right shift operator* `>>` to add a label to your transforms, like `'My description' >> MyTransform`.

Try to give short but descriptive labels.

```py
outputs = (
  pipeline
  | 'First step' >> step1
  | 'Second step' >> step2
  | 'Third step' >> step3
)
```

### Python transform catalog overview

#### Element-wise

| Transform                                                                                         | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Filter](https://beam.apache.org/documentation/transforms/python/elementwise/filter)                 | Given a predicate, filter out all elements that don't satisfy the predicate.                                                                                                                                  |
| [FlatMap](https://beam.apache.org/documentation/transforms/python/elementwise/flatmap)               | Applies a function that returns a collection to every element in the input and outputs all resulting elements.                                                                                                |
| [Keys](https://beam.apache.org/documentation/transforms/python/elementwise/keys)                     | Extracts the key from each element in a collection of key-value pairs.                                                                                                                                        |
| [KvSwap](https://beam.apache.org/documentation/transforms/python/elementwise/kvswap)                 | Swaps the key and value of each element in a collection of key-value pairs.                                                                                                                                   |
| [Map](https://beam.apache.org/documentation/transforms/python/elementwise/map)                       | Applies a function to every element in the input and outputs the result.                                                                                                                                      |
| [ParDo](https://beam.apache.org/documentation/transforms/python/elementwise/pardo)                   | The most-general mechanism for applying a user-defined `DoFn` to every element in the input collection.                                                                                                    |
| [Partition](https://beam.apache.org/documentation/transforms/python/elementwise/partition)           | Routes each input element to a specific output collection based on some partition function.                                                                                                                   |
| [Regex](https://beam.apache.org/documentation/transforms/python/elementwise/regex)                   | Filters input string elements based on a regex. May also transform them based on the matching groups.                                                                                                         |
| [Reify](https://beam.apache.org/documentation/transforms/python/elementwise/reify)                   | Transforms for converting between explicit and implicit form of various Beam values.                                                                                                                          |
| [RunInference](https://beam.apache.org/documentation/transforms/python/elementwise/runinference)     | Uses machine learning (ML) models to do local and remote inference.                                                                                                                                           |
| [ToString](https://beam.apache.org/documentation/transforms/python/elementwise/tostring)             | Transforms every element in an input collection a string.                                                                                                                                                     |
| [WithTimestamps](https://beam.apache.org/documentation/transforms/python/elementwise/withtimestamps) | Applies a function to determine a timestamp to each element in the output collection, and updates the implicit timestamp associated with each input. Note that it is only safe to adjust timestamps forwards. |
| [Values](https://beam.apache.org/documentation/transforms/python/elementwise/values)                 | Extracts the value from each element in a collection of key-value pairs.                                                                                                                                      |

#### Aggregation

| Transform                                                                                             | Description                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ApproximateQuantiles                                                                                  | Not available. See[BEAM-6694](https://issues.apache.org/jira/browse/BEAM-6694) for updates.                                                                                          |
| ApproximateUnique                                                                                     | Not available. See[BEAM-6693](https://issues.apache.org/jira/browse/BEAM-6693) for updates.                                                                                          |
| [CoGroupByKey](https://beam.apache.org/documentation/transforms/python/aggregation/cogroupbykey)         | Takes several keyed collections of elements and produces a collection where each element consists of a key and all values associated with that key.                                |
| [CombineGlobally](https://beam.apache.org/documentation/transforms/python/aggregation/combineglobally)   | Transforms to combine elements.                                                                                                                                                    |
| [CombinePerKey](https://beam.apache.org/documentation/transforms/python/aggregation/combineperkey)       | Transforms to combine elements for each key.                                                                                                                                       |
| [CombineValues](https://beam.apache.org/documentation/transforms/python/aggregation/combinevalues)       | Transforms to combine keyed iterables.                                                                                                                                             |
| CombineWithContext                                                                                    | Not available.                                                                                                                                                                     |
| [Count](https://beam.apache.org/documentation/transforms/python/aggregation/count)                       | Counts the number of elements within each aggregation.                                                                                                                             |
| [Distinct](https://beam.apache.org/documentation/transforms/python/aggregation/distinct)                 | Produces a collection containing distinct elements from the input collection.                                                                                                      |
| [GroupByKey](https://beam.apache.org/documentation/transforms/python/aggregation/groupbykey)             | Takes a keyed collection of elements and produces a collection where each element consists of a key and all values associated with that key.                                       |
| [GroupBy](https://beam.apache.org/documentation/transforms/python/aggregation/groupby)                   | Takes a collection of elements and produces a collection grouped, by properties of those elements. Unlike GroupByKey, the key is dynamically created from the elements themselves. |
| [GroupIntoBatches](https://beam.apache.org/documentation/transforms/python/aggregation/groupintobatches) | Batches the input into desired batch size.                                                                                                                                         |
| [Latest](https://beam.apache.org/documentation/transforms/python/aggregation/latest)                     | Gets the element with the latest timestamp.                                                                                                                                        |
| [Max](https://beam.apache.org/documentation/transforms/python/aggregation/max)                           | Gets the element with the maximum value within each aggregation.                                                                                                                   |
| [Mean](https://beam.apache.org/documentation/transforms/python/aggregation/mean)                         | Computes the average within each aggregation.                                                                                                                                      |
| [Min](https://beam.apache.org/documentation/transforms/python/aggregation/min)                           | Gets the element with the minimum value within each aggregation.                                                                                                                   |
| [Sample](https://beam.apache.org/documentation/transforms/python/aggregation/sample)                     | Randomly select some number of elements from each aggregation.                                                                                                                     |
| [Sum](https://beam.apache.org/documentation/transforms/python/aggregation/sum)                           | Sums all the elements within each aggregation.                                                                                                                                     |
| [Top](https://beam.apache.org/documentation/transforms/python/aggregation/top)                           | Compute the largest element(s) in each aggregation.                                                                                                                                |

#### Other

| Transform                                                                           | Description                                                                                                                                          |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create](https://beam.apache.org/documentation/transforms/python/other/create)         | Creates a collection from an in-memory list.                                                                                                         |
| [Flatten](https://beam.apache.org/documentation/transforms/python/other/flatten)       | Given multiple input collections, produces a single output collection containing all elements from all of the input collections.                     |
| PAssert                                                                             | Not available.                                                                                                                                       |
| [Reshuffle](https://beam.apache.org/documentation/transforms/python/other/reshuffle)   | Given an input collection, redistributes the elements between workers. This is most useful for adjusting parallelism or preventing coupled failures. |
| View                                                                                | Not available.                                                                                                                                       |
| [WindowInto](https://beam.apache.org/documentation/transforms/python/other/windowinto) | Logically divides up or groups the elements of a collection into finite windows according to a function.                                             |

Refer to [this](https://beam.apache.org/documentation/transforms/python/overview/) documentation for up-to-date list.

## Labs

1. Getting started with Apache Beam [[source code](03-processing/beam/lab-getting-started-with-beam/)]
2. MapReduce in Beam using Python [[source code](03-processing/beam/lab-gcp-beam-mapreduce/)]
