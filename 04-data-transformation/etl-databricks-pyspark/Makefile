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