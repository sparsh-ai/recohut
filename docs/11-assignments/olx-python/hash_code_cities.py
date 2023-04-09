"""
This Python code has the functionality of extracting the raw file with
the cities of the world, filter by one country, make some transformations
and upload a JSON file into the lsoawsprd AWS S3 Bucket

It accepts three parameters to be able to run:
Country: The country we want to filter
Access_key: Access key in order to use AWS API
Secret_key: Secret key in order to use AWS API
"""
import os
from zipfile import ZipFile
import argparse
import json
import requests as rq
import pandas as pd
import geohash2 as gh
import boto3


def main(params):
    """
    Main function to perform Extract, Transform and Load
    :param params: Input data
    :return: None
    """
    # Parameters
    access_key = params.access_key
    secret_key = params.secret_key
    country_to_filter = params.country
    bucket = 'lsoawsprd'

    # EXTRACT
    # Download and conversion into dataframe
    download_zip_file('https://simplemaps.com/static/data/'
                      'world-cities/basic/simplemaps_worldcities_basicv1.75.zip',
                      'worldcities.zip')
    dataframe_cities = get_full_df('worldcities.zip', 'worldcities.csv')

    # TRANSFORMATION
    # Country filtering
    # Columns selections
    # Adding extra geohash_code
    # Conversion of dataframe into json file
    dataframe_country = filter_country(dataframe_cities, country_to_filter)
    dataframe_select = select_columns(dataframe_country, 'city', 'lat', 'lng', 'population')
    final_df = adding_geohash_code(dataframe_select)
    country_name = 'World' if country_to_filter is None else country_to_filter
    from_df_to_json(final_df, f'cites_from_{country_name}.json')

    # LOAD
    upload_to_s3(bucket, f'refined/{country_name}/', f'cites_from_{country_name}.json'
                 , access_key, secret_key)
    # CLEAN LOCAL
    clean_local(f'cites_from_{country_name}.json','worldcities.zip')


def download_zip_file(online_path, local_path):
    """
    Function to download a zip file into the local_path
    :param online_path: string of a URL of a zip file
    :param local_path: string of a full path of the file
    :return: None
    """
    with rq.get(online_path) as response:
        with open(local_path, "wb") as write_path:
            write_path.write(response.content)


def get_full_df(local_zip_path, filename):
    """
    Function to convert a csv file (inside a zip file) into a pandas dataframe
    :param local_zip_path: string of the zip file path
    :param filename: string with the csv file name inside the zip file
    :return: pandas dataframe
    """
    with ZipFile(local_zip_path) as zip_file:
        with zip_file.open(filename) as csv_file:
            output_dataframe = pd.read_csv(csv_file)
    return output_dataframe


def filter_country(dataframe, country_to_filter):
    """
    Function to filter a pandas dataframe to extract only cities of one country
    If no country is provide it will return all the world

    :param dataframe: pandas dataframe to be filter
    :param country_to_filter: string with the name of one country in English
    :return: filtered dataframe
    """
    # If there is no country to filter it will return all the dataset
    if country_to_filter is None:
        print('LOG: No country to filter. Returning all the World')
        output_dataframe = dataframe
    else:
        print(f'LOG: Getting cities from {country_to_filter}..')
        output_dataframe = dataframe[dataframe.country == country_to_filter]
    return output_dataframe


def select_columns(dataframe, *argv):
    """
    Function to select columns in a pandas dataframe
    :param dataframe: pandas dataframe
    :param argv: multiple strings with the name of the columns to select
    :return: pandas dataframe
    """
    output_dataframe = pd.DataFrame()
    print('LOG: Selecting columns...')
    for arg in argv:
        output_dataframe[arg] = dataframe[[arg]]
    return output_dataframe


def adding_geohash_code(dataframe):
    """
    Function to build a Geohash code column using latitude and longitude
    :param dataframe: pandas dataframe
    :return: A pandas dataframe with an extra column
    """
    print('LOG: Adding GeoHash column...')
    dataframe["geohash"] = dataframe.apply(lambda x: gh.encode(x.lat, x.lng, precision=12)
                                           , axis=1)
    return dataframe


def from_df_to_json(dataframe, json_filename):
    """
    Function to convert a pandas dataframe into a JSON file
    :param dataframe: pandas dataframe
    :param json_filename: string with the name necessary for the JSON file
    :return: None
    """
    result = dataframe.to_json(orient="records")
    parsed = json.loads(result)
    with open(json_filename, 'w', encoding='utf-8') as file_open:
        json.dump(parsed, file_open, ensure_ascii=False, indent=4)


def upload_to_s3(s3_bucket, s3_path, filename, access_key, secret_key):
    """
    Function to upload a file into AWS S3
    :param filename: string with the name of the file to upload
    :param s3_bucket: string with the name of a bucket
    :param s3_path: string with the name of a s3 path without the file name
    :param access_key: string with the AWS access key
    :param secret_key: string with the AWS secret key
    :return: None
    """
    region_name = 'eu-west-1'
    s3_client = boto3.client('s3', aws_access_key_id=access_key
                             , aws_secret_access_key=secret_key
                             , region_name=region_name)
    try:
        s3_client.upload_file(filename, s3_bucket, f'{s3_path}{filename}')
        print(f'LOG: The file {filename} was inserted in s3://{s3_bucket}/{s3_path} with success !')
    except Exception as err:
        print(f"LOG: Some ERROR occur when inserting the file "
              f"{filename} in s3://{s3_bucket}/{s3_path} "
              f"({err})")


def clean_local(*argv):
    """
    Function to clean the downloaded files
    :param argv: files to be removed
    :return: None
    """
    for filename in argv:
        os.remove(filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Process of ETL to extract information of the cities of one country'
                    ', obtain the geohash code and load a json into AWS S3')

    # Arguments
    parser.add_argument('country'
                        , help='The country we want to filter', nargs='?', const='', type=str)
    parser.add_argument('access_key'
                        , help='Access_key AWS ', nargs='?', const='', type=str)
    parser.add_argument('secret_key'
                        , help='Secret_key AWS ', nargs='?', const='', type=str)

    args = parser.parse_args()

    main(args)
