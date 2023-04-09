import pandas as pd
from sqlalchemy import create_engine
import logging

if __name__ == '__main__':
    engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")

    # Extract Data
    currencies = pd.read_sql(f"select * from dwh_final.topic_currency", con=engine)

    # Transform Data
    cols = ['currency_id', 'currency_name']
    dim_currencies = currencies[cols].groupby(cols).count().reset_index()
    dim_currencies

    # Load Data
    try:
        res = dim_currencies.to_sql('dim_currencies', con=engine, schema='dwh_final', if_exists='replace')
        logging.info(f'success insert data to table: dim_currencies, inserted {res} data')
    except Exception as e:
        logging.info('Failed to insert data to table: dim_currencies')
        logging.error(e)