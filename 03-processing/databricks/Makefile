config_partitions:
	print(f"Executor cores: {sc.defaultParallelism}")
	spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

databricks_aws:
	import os
	!mkdir -p ~/.aws

	%%writefile ~/.aws/credentials
	[default]
	aws_access_key_id=
	aws_secret_access_key=
	region=us-east-1
	output=json

	import boto3
	session = boto3.Session(profile_name='default')
	credentials = session.get_credentials()

	sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", credentials.access_key)
	sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", credentials.secret_key)
	aws_region = "us-east-1"
	sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3." + aws_region + ".amazonaws.com")

databricks_cp_s3:
	%fs cp /mnt/training/ecommerce/sales/sales.parquet s3a://wysde-datasets/bedbricks/sales.parquet

Optimization Part:
	spark.conf.set("spark.sql.sources.bucketing.enabled", True)
	spark.conf.set("spark.sql.adaptive.enabled", True)

Write on Apache Hive:
	seasonal_statistics.write \
		.format("orc") \ # source format type
		.mode("overwrite") \ # save mode type
		.partitionBy("SEASON") # Optimization part
		.bucketBy(15, "ORIGIN") # Optimization part
		.saveAsTable("thy.season_origin_orc")

Write on PostgreSQL:
	jdbcUrl = "jdbc:postgresql://localhost:5432/thy?user=postgres&password=password"
	seasonal_statistics.write \
		.mode("overwrite") \
		.jdbc(url=jdbcUrl, # PostgreSQL server url
			table="seasonal_statistics",
			mode="overwrite",
			properties={"driver": "org.postgresql.Driver"})

Write on Delta Lake:
	from delta.tables import * 
	deltaPath = "/user/talha/delta_db/thy_season"
	seasonal_statistics.write.format("delta").mode("overwrite").save(deltaPath)

Read Table from Apache Hive:
	spark.sql("Select * from thy.season_origin_orc").limit(5).toPandas()

Read Table from PostgreSQL:
	spark.read.jdbc(url=jdbcUrl,
					table="seasonal_statistics",
					properties={"driver": "org.postgresql.Driver"}).limit(5).toPandas()

Read Table from Delta Lake:
	season_origin_delta = DeltaTable.forPath(spark, deltaPath)