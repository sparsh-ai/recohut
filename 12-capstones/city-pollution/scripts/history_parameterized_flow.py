from pathlib import Path
import pandas as pd
from prefect import flow
from datetime import datetime, timedelta
from etl_tasks import (
    write_bq,
    get_pollution_data,
    rename_columns,
    cleaning_columns,
    write_gcs,
    cities,
)


@flow()
def fetch_history_data(
    start_date: int, end_date: int, lat: float, lon: float
) -> pd.DataFrame:
    """
    A Prefect flow that fetches historical air pollution data from an API.

    Args:
        start_date (int): The start date for the data to fetch.
        end_date (int): The end date for the data to fetch.
        lat (float): The latitude of the location to fetch data for.
        lon (float): The longitude of the location to fetch data for.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the fetched air pollution data.
    """
    df = get_pollution_data(start_date, end_date, lat, lon)
    df_clean = cleaning_columns(df, columns=["main.aqi"])
    df_renamed = rename_columns(df_clean)
    return df_renamed


@flow()
def etl_to_gcs(df, city) -> None:
    """
    A Prefect flow that writes a pandas DataFrame to a GCS bucket.

    Args:
        df (pd.DataFrame): The DataFrame to write.
        city (str): The name of the city associated with the DataFrame.
    """
    path = Path(f"data/air_pollution/{city}.parquet")
    with path.open(mode="wb") as f:
        write_gcs(df, f)


@flow()
def etl_history_parent_flow(start_date: int, end_date: int, cities_df):
    """
    A Prefect flow that processes historical air pollution data for a list of cities.

    Args:
        start_date (int): The start date for the data to fetch.
        end_date (int): The end date for the data to fetch.
        cities_df (pd.DataFrame): A pandas DataFrame containing the list of cities to process.

    Raises:
        Exception: If there is an error processing any of the cities.
    """
    for index, city in cities_df.iterrows():
        try:
            df_pollution = fetch_history_data(
                start_date, end_date, city["Latitude"], city["Longitude"]
            )
            df_pollution["City_index"] = index
            write_bq(df_pollution, "raw.airpollution")
            if index > 1:
                break
        except Exception as e:
            print(f"Failed to process city {city['City']}: {str(e)}")


@flow()
def etl_cities_parent_flow(cities_df):
    """
    A Prefect flow that processes a pandas DataFrame containing information about cities.

    Args:
        cities_df (pd.DataFrame): A pandas DataFrame containing city information.

    Raises:
        Exception: If there is an error processing the cities table.
    """
    try:
        write_bq(cities_df, "raw.cities")
    except Exception as e:
        print(f"Failed to process cities table: {str(e)}")


if __name__ == "__main__":
    end = int((datetime.now() - timedelta(minutes=1)).timestamp())
    start = int((datetime.strptime("2020-11-28", "%Y-%m-%d").timestamp()))
    etl_history_parent_flow(start_date=start, end_date=end, cities_df=cities)
    etl_cities_parent_flow(cities_df=cities)
