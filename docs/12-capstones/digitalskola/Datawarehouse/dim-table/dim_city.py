import pandas as pd
from sqlalchemy import create_engine
import logging

if __name__ == '__main__':
    engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")

    # Extract Data
    zips = pd.read_sql(f"select * from dwh_final.zips", con=engine)
    dim_state = pd.read_sql(f"select * from dwh_final.dim_state", con=engine)

    # Transform Data
    cols = ['state','city', 'zip']
    dim_city = zips[cols].groupby(cols).count().reset_index()
    dim_city = dim_city.merge(dim_state, left_on='state', right_on='offices_state_code').drop(columns=['offices_state_code','state_id','country_id'])
    dim_city = dim_city.groupby(['state', 'city', 'zip']).count().reset_index().reset_index()
    dim_city = dim_city[(dim_city.city != '') | (dim_city.zip != '')]
    dim_city = dim_city.rename(columns={"index":"city_id"})
    dim_city['city_id'] = dim_city['city_id'] + 1

    # Load Data
    try:
        res = dim_city.to_sql('dim_city', con=engine, schema='dwh_final', index=False, if_exists='replace')
        logging.info(f'success insert data to table: dim_city, inserted {res} data')
    except Exception as e:
        logging.info('Failed to insert data to table: dim_city')
        logging.error(e)