# Developing batch processing solutions by using Data Factory, Data Lake, Spark, Azure Synapse Pipelines, PolyBase, and Azure Databricks

![B17525_09_001](https://user-images.githubusercontent.com/62965911/218307988-ac4d682d-4250-48a7-9a05-67d1173d1b0e.jpeg)

A batch processing solution typically consists of five major components:

- Storage systems such as Azure Blob storage, ADLS Gen2, HDFS, or similar
- Transformation/batch processing systems such as Spark, SQL, or Hive (via Azure HDInsight)
- Analytical data stores such as Synapse Dedicated SQL pool, Cosmos DB, and HBase (via Azure HDInsight)
- Orchestration systems such as ADF and Oozie (via Azure HDInsight)
- Business Intelligence (BI) reporting systems such as Power BI

Let's assume that we are continuously getting trip data from different regions (zip codes), which is stored in Azure Blob storage, and the trip fares are stored in an Azure SQL Server. We have a requirement to merge these two datasets and generate daily revenue reports for each region.

In order to take care of this requirement, we can build a pipeline as shown in the following diagram:

![B17525_09_002](https://user-images.githubusercontent.com/62965911/218308144-c76f7039-a1b0-4e72-abbd-2b21f008e0a7.jpeg)

The preceding pipeline, when translated into an ADF pipeline, would look like the following figure:

![B17525_09_003](https://user-images.githubusercontent.com/62965911/218308190-7f6b7abc-c83b-40c4-8adb-e8d137441504.jpeg)

As you can see, the pipeline has four stages:

- **Data ingestion**: The first two stages, **FetchTripsFrmBlob** and **FetchFaresFrmSQL** get the data into the data lake.
- **Data cleansing**: The **DataCleansing** stage in the diagram cleans up the data.
- **Transformation**: The Spark Notebook **Transform** stage in the diagram transforms the data.
- **Loading into an analytical database**: The **PolyBaseCopySQLDW** stage to copies the data into a Synapse SQL pool.

The last stage would be BI tools reading from the analytical database and generating reports (which is not shown in the diagram as that is not an ADF activity).

Storage
-------

Let's consider ADLS Gen2 as our data lake storage. We can create the following folder structure to handle our batch pipeline:

- The **raw trips** data can be stored here: `iac/raw/trips/2022/01/01`
- The cleaned-up data can be copied over to the **transform/in** folder: `iac/transform/in/2022/01/01`
- The output of the transformed data can move into the **transform/out** folder: `iac/transform/out/2022/01/01`
- Finally, we can import the data from **transform/out** into Synapse SQL Dedicated pool using **PolyBase**.

Note that tools such as **ADF** and **PolyBase** also provide the ability to directly move data between Spark and Synapse SQL Dedicated pool. You can choose this direct approach instead of storing the intermediate data in the data lake if that works better for you in terms of performance and cost. But in most data lakes, more than one tool might access the intermediate data from the data lake and it will be useful to keep historical datasets for future analysis. Hence it might make sense to keep a copy in the data lake also.

## Transform

You can find the code (scala script as well as dbc file, that can be imported in databricks) in the assets folder. That data that is produced by this notebook can also be found in the data folder. I used AzCopy to download it from the ADLS2 container.

AzCopy command:

```bash
AzCopy copy 'https://sparshstorage1.blob.core.windows.net/databricks/dailytrips' './data/' --recursive
```

**Configuring an ADB notebook activity in ADF:**

From the Azure Data Factory Activities tab, choose Notebook under Databricks and add it to the pipeline by dragging the icon into the worksheet area as shown in the following screenshot.

![B17525_09_015](https://user-images.githubusercontent.com/62965911/218311436-8cc30531-9258-4907-be8a-4a491fb7eca6.jpeg)

You have to link this Notebook activity to the notebook that you created in the previous step. In order to link the notebook, you will have to first get the access token from Azure Databricks. You can generate the access token from the Azure Databricks portal from the User Settings tab. Click on the Generate New Token button to create a new access token.

Now, link the previously created ADB notebook using a linked service. You will have to fill in Databricks Workspace URL, the Access token field – with the access token, and select whether you want to spin up a New job cluster or point to an Existing interactive cluster, and so on.

Once you have created the linked service and entered those details into the ADF notebook activity, your sample transformation stage will be complete.

## Creating data pipelines

You can create a pipeline from the Pipeline tab of Azure Data Factory. All you need to do is to select the activities for your pipeline from the Activities tab and click and drag it into the canvas. You can link the activities using the green box (on the right side of each activity) and chain the blocks together either sequentially or parallelly to derive the required output. The following screenshot shows an example.

![B17525_09_025](https://user-images.githubusercontent.com/62965911/218311781-14233984-08bc-45e0-be4f-d7d7999488ce.jpeg)

Once you have the pipeline stitched together, you can trigger it using the Add trigger button. The trigger could be one-time, event-based, or recurring. I hope you now have an understanding of how to create and publish an end-to-end batch pipeline.
