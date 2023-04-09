import pandas as pd
import secrets_key
import requests
from prefect import task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

cities = (
    pd.read_csv("city_data/cities.csv").reset_index().rename(columns={"index": "id"})
)

@task(retries=3, log_prints=True)
def get_pollution_data(
    start_time: int, end_time: int, lat: float, lon: float
) -> pd.DataFrame:
    """
    Retrieve air pollution data from the OpenWeatherMap API for a specified time range and location.
    Parameters:
        start_time (int): The start time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
        end_time (int): The end time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
        lat (float): The latitude of the location for which to retrieve data.
        lon (float): The longitude of the location for which to retrieve data.
    Returns:
        pandas.DataFrame: A dataframe containing the API response data.
    """

    # API endpoint and API key
    api_endpoint = "https://api.openweathermap.org/data/2.5/air_pollution/history"
    api_key = secrets_key.API_KEY

    # Send the API request
    response = requests.get(
        api_endpoint,
        params={
            "lat": lat,
            "lon": lon,
            "start": start_time,
            "end": end_time,
            "appid": api_key,
        },
    )

    # Check for errors
    if response.status_code != 200:
        print("Error: API request failed with status code", response.status_code)
        exit()

    # Parse the API response
    data = response.json()

    # Convert the data to a dataframe
    df = pd.json_normalize(data["list"])

    return df


@task(retries=3, log_prints=True)
def get_current_pollution(lat: float, lon: float) -> pd.DataFrame:
    """
    Retrieve air pollution data for the current time for a specific latitude and longitude.

    Parameters
    ----------
    lat : float
        The latitude of the location for which to retrieve data.
    lon : float
        The longitude of the location for which to retrieve data.

    Returns
    -------
    df : pd.DataFrame
        A pandas DataFrame containing the retrieved air pollution data.
    """
    # API endpoint and API key
    api_endpoint = "https://api.openweathermap.org/data/2.5/air_pollution"
    api_key = secrets_key.API_KEY

    # Make a request to the OpenWeatherMap API
    response = requests.get(
        api_endpoint,
        params={
            "lat": lat,
            "lon": lon,
            "appid": api_key,
        },
    )

    # Check for errors
    if response.status_code != 200:
        print("Error: API request failed with status code", response.status_code)
        exit()

    # Parse the API response
    data = response.json()

    # Convert the data to a dataframe
    df = pd.json_normalize(data, "list", [["coord", "lon"], ["coord", "lat"]])

    return df


@task(retries=3, log_prints=True)
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename the columns of a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to rename the columns of.

    Returns
    -------
    df : pd.DataFrame
        The DataFrame with renamed columns.
    """
    df = df.rename(
        columns={
            "components.co": "Carbon_Monoxide_CO",
            "components.no": "Nitric_oxide_NO",
            "components.no2": "Nitrogen_Dioxide_NO2",
            "components.o3": "Ozone_O3",
            "components.so2": "Sulfur_Dioxide_SO2",
            "components.pm2_5": "PM2_5",
            "components.pm10": "PM10",
            "components.nh3": "NH3",
        }
    )
    return df


@task(retries=3, log_prints=True)
def cleaning_columns(df: pd.DataFrame, columns=[None]) -> pd.DataFrame:
    """
    Clean and transform the columns of a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to clean and transform.
    columns : list of str or None, optional
        The columns to drop from the DataFrame. If None, no columns are dropped.
        Default is None.

    Returns
    -------
    df : pd.DataFrame
        The cleaned and transformed DataFrame.
    """
    if columns:
        df.drop(columns=columns, inplace=True)
    df["dt"] = pd.to_datetime(df["dt"], unit="s")
    return df


@task(retries=3, log_prints=True)
def write_gcs(df: pd.DataFrame, path: str) -> None:
    """
    Uploads a parquet file to GCS.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be uploaded.
    path : str
        The destination path in GCS.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If the upload fails.
    """
    gcp_cloud_storage_bucket_block = GcsBucket.load("airpollution-gcs")
    gcp_cloud_storage_bucket_block.upload_from_dataframe(
        df, to_path=path, serialization_format="parquet"
    )
    return


@task(retries=3, log_prints=True)
def write_bq(
    df: pd.DataFrame, table: str, credentials_path: str = "airpollution-credential"
) -> None:
    """
    Writes a Pandas DataFrame to BigQuery.

    Args:
        df (pd.DataFrame): The DataFrame to write to BigQuery.
        table (str): The name of the destination table in BigQuery.
        credentials_path (str, optional): The path to the Google Cloud Platform
            service account credentials file. Defaults to 'airpollution-credential'.

    Raises:
        prefect.engine.signals.FAIL: If the function fails to write to BigQuery.
    """
    try:
        gcp_credentials_block = GcpCredentials.load(credentials_path)

        df.to_gbq(
            destination_table=table,
            project_id="continual-block-378617",
            credentials=gcp_credentials_block.get_credentials_from_service_account(),
            chunksize=500_000,
            if_exists="append",
        )
    except Exception as e:
        print(f"Failed to write to BigQuery: {str(e)}")
