import pandas as pd
from datetime import datetime, timedelta, date
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")

if __name__ == '__main__':
    currencies = pd.read_sql(f"select * from currencies", con=engine)

    # change datetime to timestamp
    date_ = date.today() - timedelta(days=date.today().day)
    # date_ = date(2022,12,6)
    today = datetime(date_.year, date_.month, date_.day)
    yesterday = today.replace(day=1)
    today = datetime.timestamp(today)
    yesterday = datetime.timestamp(yesterday)

    fct_currency_monthly = currencies[(currencies.timestamp >= yesterday) & (currencies.timestamp < today)]
    fct_currency_monthly = fct_currency_monthly.groupby('currency_code').agg({'rate': 'mean'}).reset_index()
    fct_currency_monthly.rename(columns={'rate':'monthly_avg_rate'}, inplace=True)
    
    
    # Load to dwh
    try:
        res = fct_currency_monthly.to_sql('fct_currency_monthly', con=engine, schema='dwh', index=False, if_exists='replace')
        logging.info(f'success insert data to table: fct_currency_monthly, inserted {res} data')
    except Exception as e:
        logging.info('Failed to insert data to table: fct_currency_monthly')
        logging.error(e)