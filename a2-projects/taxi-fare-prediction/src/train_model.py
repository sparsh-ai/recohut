from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator

import pandas as pd



MAX_MEMORY="5g"
spark = SparkSession.builder.appName("taxi-fare-prediciton")\
                .config("spark.executor.memory", MAX_MEMORY)\
                .config("spark.driver.memory", MAX_MEMORY)\
                .getOrCreate()

data_dir = "/Users/keon/fastcampus/data-engineering/02-airflow/data/"
train_df = spark.read.parquet(f"{data_dir}/train/")
test_df = spark.read.parquet(f"{data_dir}/test/")


hyper_df = pd.read_csv(f"{data_dir}hyperparameter.csv")
alpha = float(hyper_df.iloc[0]['alpha'])
reg_param = float(hyper_df.iloc[0]['reg_param'])


cat_feats = [
    "pickup_location_id",
    "dropoff_location_id",
    "day_of_week"
]

stages = []

for c in cat_feats:
    cat_indexer = StringIndexer(inputCol=c, outputCol= c + "_idx").setHandleInvalid("keep")
    onehot_encoder = OneHotEncoder(inputCols=[cat_indexer.getOutputCol()], outputCols=[c + "_onehot"])
    stages += [cat_indexer, onehot_encoder]

num_feats = [
    "passenger_count",
    "trip_distance",
    "pickup_time"
]

for n in num_feats:
    num_assembler = VectorAssembler(inputCols=[n], outputCol= n + "_vecotr")
    num_scaler = StandardScaler(inputCol=num_assembler.getOutputCol(), outputCol= n + "_scaled")
    stages += [num_assembler, num_scaler]

assembler_inputs = [c + "_onehot" for c in cat_feats] + [n + "_scaled" for n in num_feats]
assembler = VectorAssembler(inputCols=assembler_inputs, outputCol="feature_vector")
stages += [assembler]


# Training
transform_stages = stages
pipeline = Pipeline(stages=transform_stages)
fitted_transformer = pipeline.fit(train_df)

vtrain_df = fitted_transformer.transform(train_df)
lr = LinearRegression(
    maxIter=50,
    solver="normal",
    labelCol="total_amount",
    featuresCol="feature_vector",
    elasticNetParam=alpha,
    regParam=reg_param,
)

model = lr.fit(vtrain_df)
vtest_df = fitted_transformer.transform(test_df)
predictions = model.transform(vtest_df)
predictions.cache()
predictions.select(["trip_distance", "day_of_week", "total_amount", "prediction"]).show()

model_dir = "/Users/keon/fastcampus/data-engineering/02-airflow/data/model"
model.write().overwrite().save(model_dir)