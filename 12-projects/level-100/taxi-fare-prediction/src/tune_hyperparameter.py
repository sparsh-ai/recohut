from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
import numpy as np
import pandas as pd

MAX_MEMORY="5g"
spark = SparkSession.builder.appName("taxi-fare-prediciton")\
                .config("spark.executor.memory", MAX_MEMORY)\
                .config("spark.driver.memory", MAX_MEMORY)\
                .getOrCreate()

data_dir = "/Users/keon/fastcampus/data-engineering/02-airflow/data/"

train_df = spark.read.parquet(f"{data_dir}/train/")

toy_df = train_df.sample(False, 0.1, seed=1)

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

lr = LinearRegression(
    maxIter=30,
    solver="normal",
    labelCol='total_amount',
    featuresCol='feature_vector'
)

cv_stages = stages + [lr]

cv_pipeline = Pipeline(stages=cv_stages)
param_grid = ParamGridBuilder()\
                .addGrid(lr.elasticNetParam, [0.1, 0.2, 0.3, 0.4, 0.5])\
                .addGrid(lr.regParam, [0.01, 0.02, 0.03, 0.04, 0.05])\
                .build()

cross_val = CrossValidator(estimator=cv_pipeline,
                           estimatorParamMaps=param_grid,
                           evaluator=RegressionEvaluator(labelCol="total_amount"),
                           numFolds=5)

cv_model = cross_val.fit(toy_df)
alpha = cv_model.bestModel.stages[-1]._java_obj.getElasticNetParam()
reg_param = cv_model.bestModel.stages[-1]._java_obj.getRegParam()

hyperparam = {
    'alpha': [alpha],
    'reg_param': [reg_param]
}
hyper_df = pd.DataFrame(hyperparam).to_csv(f"{data_dir}hyperparameter.csv")
print(hyper_df)