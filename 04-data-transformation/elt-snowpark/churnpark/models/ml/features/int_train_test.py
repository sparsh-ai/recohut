import snowflake.snowpark.functions as F
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, balanced_accuracy_score
import io
from xgboost import XGBClassifier
from joblib import dump, load
import joblib
import logging
import sys
from joblib import dump, load

logger = logging.getLogger("mylog")

def save_file(session, model, path, dest_filename):
  input_stream = io.BytesIO()
  joblib.dump(model, input_stream)
  session._conn.upload_stream(input_stream, path, dest_filename)
  return "successfully created file: " + path

def model(dbt, session):
    dbt.config(
        packages = ['numpy','scikit-learn','pandas','numpy','joblib','xgboost','cachetools'],
        materialized = "table",
        snowflake_warehouse = "DBT_HIGH_MEM_WH"

    )
    session._use_scoped_temp_objects = False
    version = "1.0"
    logger.info('Model training version: ' + version)
    user_df = dbt.ref("int_users_and_subscriptions")
    user_ch = user_df.with_column("churn", F.when(F.col("has_had_cancel"), F.lit(1)).otherwise(F.lit(0))).drop(F.col("has_had_cancel"))

    user_spdf = user_ch.select([
         "USER_ID"
        ,"CORE_MARITAL_STATUS_S"
        ,"CORE_MARITAL_STATUS_M"
        ,"CORE_NUMBER_OF_PERSONS_IN_LIVING_UNIT"
        ,"CORE_PRESENCE_OF_CHILDREN_N"
        ,"CORE_PRESENCE_OF_CHILDREN_Y"
        ,"CORE_HOMEOWNER_R"
        ,"CORE_HOMEOWNER_Y"
        ,"CORE_MERKLE_ADJUSTED_WEALTH_RATING"
        ,"CORE_LENGTH_OF_RESIDENCE"
        ,"CORE_HOUSEHOLD_INCOME"
        ,"CORE_PROBABLE_USING_INTERNET_FOR_GENERAL_ENTERTAINMENT"
        ,"TOTAL_AMOUNT_PAID"
        ,"NUMBER_OF_SUBSCRIPTIONS"
        ,"TOTAL_SUBSCRIBED_MONTH"
        ,"CHURN"]).limit(100000)
    
    df_orig=user_spdf.to_pandas()
    target_col = "CHURN"
    split_X = df_orig.drop([target_col], axis=1)
    split_y = df_orig[target_col]

    # Split out train data
    X_train,  X_test, y_train, y_test = train_test_split(split_X, split_y, train_size=0.7, random_state=470520671, stratify=split_y)
    train = [X_train, y_train]
    test = [X_test, y_test]
    standardizer = StandardScaler()

    xgbc_classifier = XGBClassifier(
        colsample_bytree=0.20033896648561572,
        learning_rate=0.10268222106305344,
        max_depth=7,
        min_child_weight=12,
        n_estimators=505,
        n_jobs=100,
        subsample=0.37569870499628705,
        verbosity=0,
        random_state=470520671
    )

    model = Pipeline([
    ("standardizer", standardizer),
    ("classifier", xgbc_classifier),
    ])
   
    # fit the preprocessing pipeline and the model together  
    model.fit(X_train, y_train)
    y_pred = model.predict_proba(X_test)[:,1]
    predictions = [round(value) for value in y_pred]
    balanced_accuracy =  balanced_accuracy_score(y_test, predictions)

    #Confusion Matrix
    cm = confusion_matrix(y_test, predictions)
    TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()
    accuracy =  (TP+TN) /(TP+FP+TN+FN)
    logger.info('Model training accuracy:' + str(accuracy))

    # Save the model to a stage
    save_file(session, model, "@LIB_STG/cust_churn_"+version, "cust_churn_"+version+".joblib" )
    logger.info('Model artifact:' + "@LIB_STG/cust_churn_"+version+".joblib")
    
    #return user_spdf
    snowpark_train_df = session.write_pandas(pd.concat(train, axis=1, join='inner'), "train_table", auto_create_table=True, create_temp_table=True)
    snowpark_test_df = session.write_pandas(pd.concat(test, axis=1, join='inner'), "test_table", auto_create_table=True, create_temp_table=True)
    
    # Add a column indicating train vs test
    return  snowpark_train_df.with_column("DATASET_TYPE", F.lit("train")).union(snowpark_test_df.with_column("DATASET_TYPE", F.lit("test")))
   

   