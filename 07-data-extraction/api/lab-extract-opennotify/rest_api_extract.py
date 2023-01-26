# returns the current lat/lon of the ISS
import requests
import json
import configparser
import csv
import boto3

api_response = requests.get("http://api.open-notify.org/iss-now.json")

# create a json object from the response content
response_json = json.loads(api_response.content)

# {'timestamp': 1673923459, 'iss_position': {'longitude': '-148.7648', 'latitude': '14.4172'}, 'message': 'success'}

timestamp = response_json["timestamp"]
lon = response_json["iss_position"]["longitude"]
lat = response_json["iss_position"]["latitude"]
message = response_json["message"]

iss_location = {
    "timestamp": timestamp,
    "longitude": lon,
    "latitude": lat,
    "message": message    
}
print(iss_location)
export_file = "export_rest_api_file.csv"

with open(export_file,'w') as fp:
    csvw = csv.writer(fp,delimiter='|')
    csvw.writerow(iss_location.keys())
    csvw.writerow(iss_location.values())

fp.close()

# Upload the CSV file to S3 bucket
# load the 'aws_boto_credentials' values
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

s3 = boto3.client('s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)

s3_file = export_file

s3.upload_file(export_file, bucket_name, s3_file)