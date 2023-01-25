'''
 This model, demonstrates the performing feature engineering as part of the data processing pipeline.
 The user attributes contains various categorical columns, which needs to be encoded in a format that is suitable for
 the model used for training. Hence we perform a 1-hot-encoding on the dataset. 
 
 As of this beta version 1.3.0-b2, there is no ability to share python code across models. Also as of today the 
 IMPORT clause of Snowflake Stored Procedure is also not possible using DBT. Hence to overcome this limitation we had
 to implement various classes/methods in a single file.
 We are not using scikit one hot encoder implementation, as our dataset is huge, with over 32 million records and 12+GB in size.
 loading this entire dataset is not feasible. To overcome this the Snowflake team has created the sp4py library:
 https://github.com/Snowflake-Labs/snowpark-python-demos/tree/main/sp4py_utilities
 I had copied the necessary code implementation into this model file.
'''

import numpy as np
import pandas as pd
from snowflake.snowpark import DataFrame
import snowflake.snowpark.functions as F
import json ,sys
import os ,sys ,json ,zipfile ,tarfile
import importlib.util

# We need to add the imported third party libraries 
IMPORT_DIR = sys._xoptions["snowflake_import_directory"]

# This is a local directoy, used for storing the various artifacts locally
LOCAL_TEMP_DIR = f'/tmp/churn_'
TARGET_LIB_PATH = os.path.join(LOCAL_TEMP_DIR, 'lib')

def extract_libraries():
    # We perform extraction only on a first run. Hence this simplistic check
    # can help in doing this extraction multiple times.
    if os.path.exists(LOCAL_TEMP_DIR) == False:

        # We extract each of the library locally into its own directory
        archived_lib_files = [
            'sp4py_utilities.zip'
        ]
        for archived_lib_fl in archived_lib_files:
            with zipfile.ZipFile( os.path.join(IMPORT_DIR, archived_lib_fl) , 'r') as zip_ref:
                zip_ref.extractall(TARGET_LIB_PATH)

def model(dbt, session):

    dbt.config(
        materialized = "table"
        ,packages = ["numpy", "scikit-learn", "pandas"]
        ,imports = ['@lib_stg/libs/sp4py_utilities.zip']
    )

    df_user_attributes = dbt.ref("int_user_attributes")

    extract_libraries()
    
    # We need to add the libraries to the system path, so that
    # the various autogluon modules can be imported
    sys.path.insert(0 ,os.path.join(TARGET_LIB_PATH, 'sp4py_utilities') )
    sys.path.insert(0 ,TARGET_LIB_PATH )

    import preprocessing as pp

     # The list of categorical columns to be encoded
    encoder_input_cols = ['CORE_MARITAL_STATUS', 'CORE_PRESENCE_OF_CHILDREN', 'CORE_HOMEOWNER' ,'HAS_HAD_TRIAL' ]

    # Create a One hot encoder object that will encode the input_cols
    ohe = pp.OneHotEncoder(input_cols=encoder_input_cols ,drop_input_cols=False)
    # Fit the values needed for the encoder for each of the input_cols
    ohe.fit(df_user_attributes)
    # Encode the input_cols and return the scaled values in the output_cols in the returned Snowpark DataFrame, the actual
    # encoding are not done until a action method is called ie show(), collect() etc.
    ohe_tr_df = ohe.transform(df_user_attributes)

    return ohe_tr_df
