from pathlib import Path
import pandas as pd
from prefect import flow

from datetime import datetime, timedelta
from etl_tasks import (
    get_current_pollution,
    get_pollution_data,
    rename_columns,
    cleaning_columns,
    write_gcs,
    write_local,
)

now = int((datetime.now() - timedelta(minutes=1)).timestamp())
week_earlier = int((datetime.now() - timedelta(days=7)).timestamp())

pszczyna = [(1, "Pszczyna", 49.9778328, 18.9425124)]


@flow()
def fetch_data(start_time: int, end_time: int, lat: float, lon: float) -> None:

    df = get_pollution_data(week_earlier, now, lat, lon)
    df_clean = cleaning_columns(df)
    df_renamed = rename_columns(df_clean)
    return df_renamed


@flow()
def etl_to_gcs(df, city) -> None:
    # date = datetime.fromtimestamp(time).date()
    dataset_file = f"Air_pollution{city}"
    path = write_local(df, dataset_file)
    # write_gcs(path)


@flow()
def etl_parent_flow(city_list):
    for city in city_list:
        df_pollution = fetch_data(week_earlier, now, city[2], city[3])
        etl_to_gcs(df_pollution, city[1])


if __name__ == "__main__":
    etl_parent_flow(city_list=pszczyna)
