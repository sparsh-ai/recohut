import pandas as pd
from sqlalchemy import create_engine
import logging

if __name__ == '__main__':
    engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")

    # Extract Data
    companies = pd.read_sql(f"select * from dwh_final.companies", con=engine)
    dim_country = pd.read_sql(f"select * from dwh_final.dim_country", con=engine)

    # Transform Data
    cols = ['offices_state_code', 'offices_country_code']
    dim_state = companies[cols].groupby(cols).count().reset_index().reset_index()
    dim_state = dim_state.rename(columns={"index":"state_id"})
    dim_state = dim_state[dim_state.offices_country_code != '']
    dim_state = dim_state.merge(dim_country, on='offices_country_code').drop(columns='offices_country_code')
    dim_state = dim_state[dim_state.offices_state_code != '']
    dim_state.head(2)

    # Load Data
    try:
        res = dim_state.to_sql('dim_state', con=engine, schema='dwh_final', index=False, if_exists='replace')
        logging.info(f'success insert data to table: dim_state, inserted {res} data')
    except Exception as e:
        logging.info('Failed to insert data to table: dim_state')
        logging.error(e)