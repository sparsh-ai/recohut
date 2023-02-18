import logging
import joblib
import pandas as pd
import os 
from snowflake.snowpark import types as T

DB_STAGE = 'lib_stg'
version = '1.0'
# The name of the model file
model_file_path = 'cust_churn_'+version
model_file_packaged = 'cust_churn_'+version+'.joblib'

# This is a local directoy, used for storing the various artifacts locally
LOCAL_TEMP_DIR = f'/tmp/customer_churn'
DOWNLOAD_DIR = os.path.join(LOCAL_TEMP_DIR, 'download')
TARGET_MODEL_DIR_PATH = os.path.join(LOCAL_TEMP_DIR, 'ml_model')
TARGET_LIB_PATH = os.path.join(LOCAL_TEMP_DIR, 'lib')

# The feature columns that were used during model training 
# and that will be used during prediction
FEATURE_COLS = [
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
            ,"TOTAL_SUBSCRIBED_MONTH"]

def register_udf_for_prediction(p_predictor ,p_session ,p_dbt):

    # The prediction udf

    def predict_churn(p_df: T.PandasDataFrame[int, int, int, int,
                                        int, int, int, int,
                                        int, int, int, int,
                                        int, int, int]) -> T.PandasSeries[int]:
        # Snowpark currently does not set the column name in the input dataframe
        # The default col names are like 0,1,2,... Hence we need to reset the column
        # names to the features that we initially used for training. 
        p_df.columns = [*FEATURE_COLS]
        
        # Perform prediction. this returns an array object
        pred_array = p_predictor.predict(p_df)
        # Convert to series 
        df_predicted = pd.Series(pred_array)
        return df_predicted

    # The list of packages that will be used by UDF
    udf_packages = p_dbt.config.get('packages')

    predict_churn_udf = p_session.udf.register(
        predict_churn
        ,name=f'predict_churn'
        ,packages = udf_packages
    )
    return predict_churn_udf

def load_model(p_session):
    # Load the model and initialize the predictor
    model_fl_path = os.path.join(DOWNLOAD_DIR, model_file_packaged)
    predictor = joblib.load(model_fl_path)
    return predictor

def download_models_and_libs_from_stage(p_session):
    p_session.file.get(f'@{DB_STAGE}/{model_file_path}/{model_file_packaged}', DOWNLOAD_DIR)
    
# -------------------------------
def model(dbt, session):
    dbt.config(
        packages = ['snowflake-snowpark-python' ,'scipy' 
        ,'scikit-learn' ,'pandas' ,'numpy' ,'xgboost']
        ,materialized = "table"
    )
    session._use_scoped_temp_objects = False
    download_models_and_libs_from_stage(session)
    predictor = load_model(session)
    predict_churn_udf = register_udf_for_prediction(predictor, session ,dbt)
    
    # Retrieve the data, and perform the prediction
    user_dfsp = (dbt.ref("int_users_and_subscriptions")
        .select(*FEATURE_COLS)
    )

    # Perform prediction.
    df_predicted = user_dfsp.withColumn("churn_predicted"
        ,predict_churn_udf(*FEATURE_COLS)
    )
    
    return df_predicted
