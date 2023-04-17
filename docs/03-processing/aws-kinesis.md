# Amazon Kinesis

> Easily collect, process, and analyze video and data streams in real time

### Kinesis Data Streams

Amazon Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized needs. You can continuously add various types of data to an Amazon Kinesis data stream from hundreds of thousands of sources. Within seconds, the data will be available for the Glue streaming job to read and process from the stream.

The Kinesis data stream serves as a buffer that decouples the producers from the consumers. It is a common pattern for architectures that are analyzing streaming data to separate producers from consumers by means of a streaming store. In this way, the architecture becomes more robust. Producers and consumers can be scaled independently and producers can still persist events into the data stream even if the consumers are currently experiencing operational problems or the consuming application needs to be updated.

This architecture also allows you to experiment and adopt new technologies in the future. Multiple independent applications can concurrently consume the data stored in the Kinesis data stream. You can then test how a new version of an existing application performs with a copy of the production traffic. But you can also introduce a different tool and technology stack to analyze the data, again without affecting the existing production application.

### Kinesis Data Firehose

![firehose1](https://user-images.githubusercontent.com/62965911/214809905-73d9a39f-b54d-4a69-8de7-533caba92a27.png)

![firehose2](https://user-images.githubusercontent.com/62965911/214809918-e1f3a09a-98e4-45d6-aaf1-691fbc38d7f3.png)

![firehose3](https://user-images.githubusercontent.com/62965911/214809922-442e7c57-e696-4b0e-9655-63fcecaf53cf.png)

#### Why Kinesis Data Firehose?

- Ease of Use: With just a few clicks, create your delivery stream. Connect to your destination in under a minute
- No Code Required: Handles data delivery failures, Built-in transformations, 30+ sources and destinations
- Serverless with Elastic Scale: Firehose automatically provisions, manages and scales resources with no on-going administration required
- Low Cost: Data can be prepared and delivered at pennies per delivered GB with any scale

#### In-transit Dynamic Partitioning

![dynamic_partitioning](https://user-images.githubusercontent.com/62965911/214809877-fddd4ead-90ce-4714-b99c-4a87e9eb8dc7.png)

Traditionally, customers use Kinesis Data Firehose delivery streams to capture and load their data into Amazon S3 based data lakes for analytics. Partitioning the data while storing on Amazon Simple Storage Service(S3) is a best practice for optimizing performance and reducing the cost of analytics queries because partitions minimize the amount of data scanned. By default, Kinesis Firehose creates a static Universal Coordinated Time (UTC) based folder structure in the format of YYYY/MM/dd/HH. It is then appended it to the provided prefix before writing objects to Amazon S3.

With Dynamic Partitioning, Kinesis Data Firehose will continuously group data in-transit by dynamically or statically defined data keys, and deliver to individual Amazon S3 prefixes by key. This will reduce time-to-insight by minutes or hours, reducing costs and simplifying architectures. This feature combined with Kinesis Data Firehose's Apache Parquet and Apache ORC format conversion feature makes Kinesis Data Firehose an ideal option for capturing, preparing, and loading data that is ready for analytic queries and data processing. Review Kinesis Data Firehose [documentation](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)  for additional details on Kinesis Data Firehose dynamic partitioning feature.

#### Use Cases

![use_cases](https://user-images.githubusercontent.com/62965911/214809928-eccb3817-0415-4792-a62b-5c66e3d91f99.png)

#### Best Practices

Consider the following best practices when deploying Kinesis Firehose:

- **Record Size Limit**: The maximum size of a record sent to Kinesis Data Firehose is 1,000 KB. If your message size is greater than this value, compressing the message before it is sent to Kinesis Data Firehose is the best approach.
- **Buffering hints**: Buffering hint options are treated as hints. As a result, Kinesis Data Firehose might choose to use different values to optimize the buffering.
- **Permissions**: Kinesis Data Firehose uses IAM roles for all the permissions that the delivery stream needs. You can choose to create a new role where required permissions are assigned automatically, or choose an existing role created for Kinesis Data Firehose. If you are creating a new role, ensure that you are granting only the permissions that are required to perform a task.
- **Encryption**: Data at rest and data in transit can be encrypted in Kinesis Data Firehose. Refer to the Kinesis Firehose [Documentation](https://docs.aws.amazon.com/firehose/latest/dev/encryption.html) .
- **Tags**: You can add tags to organize your AWS resources, track costs, and control access.
- **Costs**: Amazon Kinesis Data Firehose uses simple pay as you go pricing. There is neither upfront cost nor minimum fees and you only pay for the resources you use. Amazon Kinesis Data Firehose pricing is based on the data volume (GB) ingested by Firehose, with each record rounded up to the nearest 5KB. The 5KB roundup is calculated at the record level rather than the API operation level. For example, if your PutRecordBatch call contains two 1KB records, the data volume from that call is metered as 10KB. (2 times 5KB per record).

### Amazon Kinesis Data Generator (KDG)

The KDG simplifies the task of generating data and sending it to Amazon Kinesis. The tool provides a user-friendly UI that runs directly in your browser. With the KDG, you can do the following tasks:

- Create templates that represent records for your specific use cases
- Populate the templates with fixed data or random data
- Save the templates for future use
- Continuously send thousands of records per second to your Amazon Kinesis data stream or Firehose delivery stream

## Explore further

1. [Kinesis Data Firehose](https://knowledgetree.notion.site/Amazon-Kinesis-Data-Firehose-Shared-62cfabe200004bcf8a92db6d814aba9c)
2. [Kinesis Data Generator](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html)
3. [Delivering data in real-time via auto scaling Kinesis streams at Disney](https://medium.com/disney-streaming/delivering-data-in-real-time-via-auto-scaling-kinesis-streams-72a0236b2cd9)
4. [Streaming Terabytes of Real Time Data with Serverless Amazon Kinesis Services](https://www.youtube.com/watch?v=ZWyYHgtu67I)
5. [https://youtu.be/MbEfiX4sMXc](https://youtu.be/MbEfiX4sMXc)
6. [https://youtu.be/hLLgkTUmwOU](https://youtu.be/hLLgkTUmwOU)
7. [https://youtu.be/SC_oajk02BM](https://youtu.be/SC_oajk02BM)
