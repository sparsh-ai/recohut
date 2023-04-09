# Google Cloud Storage (GCS)

**Google Cloud Storage** (**GCS**) is object storage. It's a service that is fully managed by GCP, which means we don't need to think about any underlying infrastructure for GCS. For example, we don't need to think about pre-sizing the storage, the network bandwidth, number of nodes, or any other infrastructure-related stuff.

What is object storage? **Object storage** is a highly scalable data storage architecture that can store very large amounts of data in any format. 

Because the technology can store data in almost any size and format, GCS is often used by developers to store any large files, for example, images, videos, and large CSV data. But, from the data engineering perspective, we will often use GCS for storing files, for example, as dump storage from databases, for exporting historical data from **BigQuery**, for storing machine learning model files, and for any other purpose related to storing files.