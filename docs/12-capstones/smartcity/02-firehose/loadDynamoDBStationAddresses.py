import boto3
import csv
import argparse
import os, sys
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser()
parser.add_argument("--region", nargs='?', const=1, help="region where the Cloudformation template was run", default="us-east-1")
parser.add_argument("--csvFilePath", nargs='?', const=1, help="the full path to the csv file including the file name", default=os.path.join(sys.path[0],"stations_addresses.csv"))
parser.add_argument("--dynamoDBTableName", nargs='?', const=1, help="the name of DynamoDB table", default="BikeStationAddress")
args = parser.parse_args()

region = args.region
csvFilePath = args.csvFilePath
dynamoDBTableName = args.dynamoDBTableName

ddb = boto3.client('dynamodb', region_name=region)

def writeDynamoDBRecord(record):
    try:
        response = ddb.put_item(
                TableName=dynamoDBTableName,
                Item={
                'StationId' : {'N':record[0]},
                'Address': {'S':record[1]}
                }
        )
    except ClientError as err:
        print(err.response['Error'])
        raise


def readCSV(dataFile):
    csvFile = csv.reader(dataFile)
    counter = 0
    for row in csvFile:
        writeDynamoDBRecord(row)
        counter+=1
    print("Successfully inserted {} records into DynamoDB table {}".format(counter, dynamoDBTableName))

with open(csvFilePath) as csvFile:
    readCSV(csvFile)



