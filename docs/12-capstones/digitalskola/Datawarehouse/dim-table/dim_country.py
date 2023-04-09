import pandas as pd
from sqlalchemy import create_engine
import logging

if __name__ == '__main__':
    engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")

    # Extract Data
    companies = pd.read_sql(f"select * from dwh_final.companies", con=engine)

    # Transform Data
    companies.columns
    cols = ['offices_country_code']
    dim_country = companies[cols].groupby(cols).count().reset_index().reset_index()
    dim_country = dim_country.rename(columns={"index":"country_id"})
    dim_country = dim_country[dim_country.offices_country_code != '']

    # Load Data
    try:
        res = dim_country.to_sql('dim_country', con=engine, schema='dwh_final', index=False, if_exists='replace')
        logging.info(f'success insert data to table: dim_country, inserted {res} data')
    except Exception as e:
        logging.info('Failed to insert data to table: dim_country')
        logging.error(e)
