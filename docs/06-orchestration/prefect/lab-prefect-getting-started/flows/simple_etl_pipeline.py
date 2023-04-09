import json
import requests
import pandas as pd
from datetime import datetime
from prefect import task, flow

@task
def extract(url: str) -> dict:
    res = requests.get(url)
    if not res:
        raise Exception('No data fetched!')
    return json.loads(res.content)

@task
def transform(data: dict) -> pd.DataFrame:
    transformed = []
    for user in data:
        transformed.append({
            'ID': user['id'],
            'Name': user['name'],
            'Username': user['username'],
            'Email': user['email'],
            'Address': f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}",
            'PhoneNumber': user['phone'],
            'Company': user['company']['name']
        })
    return pd.DataFrame(transformed)

@task
def load(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path_or_buf=path, index=False)

@flow
def simple_etl_pipeline(param_url='https://jsonplaceholder.typicode.com/users'):
    users = extract(url=param_url)
    df_users = transform(users)
    load(data=df_users, path=f'./data/users_{int(datetime.now().timestamp())}.csv')
    
if __name__ == "__main__":
    simple_etl_pipeline()
