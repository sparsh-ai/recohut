// Databricks notebook source
import org.apache.log4j.Logger
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.Window

// COMMAND ----------

val invoices_data_path = "/FileStore/shared_uploads/sprsag@gmail.com/data.csv"
val summary_data_path = "/FileStore/shared_uploads/sprsag@gmail.com/summary.parquet"

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Aggregation

// COMMAND ----------

object AggDemo extends Serializable {
  @transient lazy val logger: Logger = Logger.getLogger(getClass.getName)

  def main() = {

    val invoiceDF = spark.read
      .format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load(invoices_data_path)

        invoiceDF.select(
          count("*").as("Count *"),
          sum("Quantity").as("TotalQuantity"),
          avg("UnitPrice").as("AvgPrice"),
          countDistinct("InvoiceNo").as("CountDistinct")
        ).show()


        invoiceDF.selectExpr(
          "count(1) as `count 1`",
          "count(StockCode) as `count field`",
          "sum(Quantity) as TotalQuantity",
          "avg(UnitPrice) as AvgPrice"
        ).show()

        invoiceDF.createOrReplaceTempView("sales")
        val summarySQL = spark.sql(
          """
            |SELECT Country, InvoiceNo,
            | sum(Quantity) as TotalQuantity,
            | round(sum(Quantity*UnitPrice),2) as InvoiceValue
            | FROM sales
            | GROUP BY Country, InvoiceNo
            |""".stripMargin)

        summarySQL.show()

    val summaryDF = invoiceDF.groupBy("Country", "InvoiceNo")
      .agg(sum("Quantity").as("TotalQuantity"),
        round(sum(expr("Quantity*UnitPrice")), 2).as("InvoiceValue"),
        expr("round(sum(Quantity*UnitPrice),2) as InvoiceValueExpr")
      )
    summaryDF.show()

  }

}


// COMMAND ----------

AggDemo.main()

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Grouping

// COMMAND ----------

object GroupingDemo extends Serializable {
  @transient lazy val logger: Logger = Logger.getLogger(getClass.getName)

  def main() = {

    val invoiceDF = spark.read
      .format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load(invoices_data_path)

    val NumInvoices = countDistinct("InvoiceNo").as("NumInvoices")
    val TotalQuantity = sum("Quantity").as("TotalQuantity")
    val InvoiceValue = expr("round(sum(Quantity * UnitPrice),2) as InvoiceValue")

    val exSummaryDF = invoiceDF
      .withColumn("InvoiceDate", to_date(col("InvoiceDate"), "dd-MM-yyyy H.mm"))
      .where("year(InvoiceDate) == 2010")
      .withColumn("WeekNumber", weekofyear(col("InvoiceDate")))
      .groupBy("Country", "WeekNumber")
      .agg(NumInvoices, TotalQuantity, InvoiceValue)

    exSummaryDF.coalesce(1)
      .write
      .format("parquet")
      .mode("overwrite")
      .save("output")

    exSummaryDF.sort("Country", "WeekNumber").show()
  }
}


// COMMAND ----------

GroupingDemo.main()

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Windowing

// COMMAND ----------

object WindowingDemo extends Serializable {
  @transient lazy val logger: Logger = Logger.getLogger(getClass.getName)

  def main() = {

    val summaryDF = spark.read.parquet(summary_data_path)

    val runningTotalWindow = Window.partitionBy("Country")
      .orderBy("WeekNumber")
      .rowsBetween(-2, Window.currentRow)

    summaryDF.withColumn("RunningTotal",
      sum("InvoiceValue").over(runningTotalWindow)
    ).show()

  }

}


// COMMAND ----------

WindowingDemo.main()

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Joins

// COMMAND ----------

object SparkJoinDemo extends Serializable {
  @transient lazy val logger: Logger = Logger.getLogger(getClass.getName)

  def main() = {

    val ordersList = List(
      ("01", "02", 350, 1),
      ("01", "04", 580, 1),
      ("01", "07", 320, 2),
      ("02", "03", 450, 1),
      ("02", "06", 220, 1),
      ("03", "01", 195, 1),
      ("04", "09", 270, 3),
      ("04", "08", 410, 2),
      ("05", "02", 350, 1)
    )
    val orderDF = spark.createDataFrame(ordersList).toDF("order_id", "prod_id", "unit_price", "qty")

    val productList = List(
      ("01", "Scroll Mouse", 250, 20),
      ("02", "Optical Mouse", 350, 20),
      ("03", "Wireless Mouse", 450, 50),
      ("04", "Wireless Keyboard", 580, 50),
      ("05", "Standard Keyboard", 360, 10),
      ("06", "16 GB Flash Storage", 240, 100),
      ("07", "32 GB Flash Storage", 320, 50),
      ("08", "64 GB Flash Storage", 430, 25)
    )
    val productDF = spark.createDataFrame(productList).toDF("prod_id", "prod_name", "list_price", "qty")

    productDF.show()
    orderDF.show()

    val joinExpr = orderDF.col("prod_id") === productDF.col("prod_id")
    val joinType = "inner"

    val productRenamedDF = productDF.withColumnRenamed("qty", "reorder_qty")

    orderDF.join(productRenamedDF, joinExpr, joinType)
      .drop(productRenamedDF.col("prod_id"))
      .select("order_id", "prod_id", "prod_name", "unit_price", "list_price", "qty")
      .show()
  }

}


// COMMAND ----------

SparkJoinDemo.main()

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Outer Join

// COMMAND ----------

object OuterJoinDemo extends Serializable{
  @transient lazy val logger: Logger = Logger.getLogger(getClass.getName)

  def main() = {

    val ordersList = List(
      ("01", "02", 350, 1),
      ("01", "04", 580, 1),
      ("01", "07", 320, 2),
      ("02", "03", 450, 1),
      ("02", "06", 220, 1),
      ("03", "01", 195, 1),
      ("04", "09", 270, 3),
      ("04", "08", 410, 2),
      ("05", "02", 350, 1)
    )
    val orderDF = spark.createDataFrame(ordersList).toDF("order_id", "prod_id", "unit_price", "qty")

    val productList = List(
      ("01", "Scroll Mouse", 250, 20),
      ("02", "Optical Mouse", 350, 20),
      ("03", "Wireless Mouse", 450, 50),
      ("04", "Wireless Keyboard", 580, 50),
      ("05", "Standard Keyboard", 360, 10),
      ("06", "16 GB Flash Storage", 240, 100),
      ("07", "32 GB Flash Storage", 320, 50),
      ("08", "64 GB Flash Storage", 430, 25)
    )
    val productDF = spark.createDataFrame(productList).toDF("prod_id", "prod_name", "list_price", "qty")

    val joinExpr = orderDF.col("prod_id") === productDF.col("prod_id")
    val joinType = "left"

    val productRenamedDF = productDF.withColumnRenamed("qty", "reorder_qty")

    orderDF.join(productRenamedDF, joinExpr, joinType)
      .drop(productDF.col("prod_id"))
      .select("order_id", "prod_id", "prod_name", "unit_price", "list_price", "qty")
      .withColumn("prod_name", expr("coalesce(prod_name, prod_id)"))
      .withColumn("list_price", expr("coalesce(list_price, unit_price)"))
      .sort("order_id")
      .show()
  }

}


// COMMAND ----------

OuterJoinDemo.main()
