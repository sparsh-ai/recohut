# Data Governance

## What is Data Governance?

Data governance refers to defining and implementing strategies that ensure the organizational data is consistent, reliable, and meets the business needs of the data consumers. To achieve this, an effective data governance strategy defines policies that specify where the data is stored, what data is stored, who can access what kind of data, how the data is processed, and the standards of an organizational dataset that enable data-driven decision-making.

## Pillars

### 1\. Data Usability

This policy requires the data to be in a usable format for business users meaning datasets must be clearly structured and easily accessible. Some of the duties that data engineers need to perform to ensure data usability are:

- Provide user documentation of datasets — specify how and where to access the data, mention the business value and when to use the dataset, and clearly describe the dataset attributes (metadata).
- Make data compatible with tools used by business users — this may require data engineers to push the final dataset into different platforms or business intelligence tools used by the downstream consumers.

### 2\. Data Quality

This policy ensures that the data is accurate, free of anomalies, and fits the purpose it is intended for. Poor data quality can lead to incorrect insights and negative impacts on business operations. Data engineers need to have data quality as their high priority in all stages (extract, transform, and load) of building a data pipeline, and here are some of the tips:

- Perform row-level count checks for source data.
- Have data transformation checks — ensure data integrity is maintained, attributes have appropriate data types, and there is no data loss.
- Perform data validation checks on the final dataset — threshold checks for null values allowed (if any), range of values, etc. You can use open-source libraries like [Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/) to perform unit tests for large datasets.
- Have anomaly detection checks in place for datasets.
- Set up alerts for data quality issues and work to fix them ASAP.

### 3\. Data Availability

This policy requires that the data is available at the RIGHT time for the business teams to ensure timely decision-making. Data availability is the main responsibility of data engineers, and here are some of the actions they can take to ensure it:

- Define Service Level Agreements (SLAs) for datasets — by having predefined SLAs for datasets, data engineers can decide on the frequency of running data pipelines and set clear expectations with the business teams for the availability of updated datasets.
- Be there for production support — Data pipelines will run into issues causing data errors. And in those cases, data engineers must inform the end users, analyze the issues, provide an ETA for resolving them, and work to fix them without majorly impacting the downstream activities.

### 4\. Data Security

This policy ensures that the data is classified based on its sensitivity, defines who should have access to what kind of data, and specifies security measures for preventing data breaches. Data engineers need to do these to comply with the data security policies:

- Restrict data access to specified users — this can be implemented in terms of database/table/row level access or in terms of the allowed operations (write/read/update) on the dataset.
- Follow high-level security practices for datasets containing personal identification information, and financial, and other confidential data.
- Data engineering teams are generally provided with access keys/secrets to deploy, test, and run data pipelines that need to be part of application code. Make sure not to commit them to GitHub repositories.

### 5\. Data Lineage

This policy provides transparency on data movement and depicts the sources and processes involved in moving data from its source to its destination. Data consumers tend to develop trust in the data they are using by looking at the data lineage.

- Data engineers can visually represent data sources (external or internal), transformations applied to the data, the job controlling the data flow, and the timeliness of the data.
- It is also recommended to provide the contact information of the source dataset owners in case the end users want to understand more about the data and the business value derived from the dataset.