# Batch vs Incremental Data Processing

The idea behind incremental processing is quite simple. Incremental processing extends the semantics of processing streaming data to batch processing pipelines by processing only new data each run and then incrementally updating the new results. This unlocks great cost savings due to much shorter batch pipelines as well as data freshness speedups due to being able to run them much more frequently as well. 

> :eyeglasses: Case Study: <a href="https://www.uber.com/en-IN/blog/ubers-lakehouse-architecture/" target="_blank">Setting Uber’s Transactional Data Lake in Motion with Incremental ETL Using Apache Hudi</a>
