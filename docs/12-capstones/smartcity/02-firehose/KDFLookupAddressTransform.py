import boto3
import base64
import os
import json
from botocore.exceptions import ClientError

ddb = boto3.resource('dynamodb')

def getAddressList(tableName):
  try:
    table = ddb.Table(tableName)
    response = table.scan()
    return response['Items']
  except ClientError as err:
    print(err.response['Error'])
    raise


def lookupRecord(addressList, stationId):

  for rec in addressList:
    if stationId == rec['StationId']:
      return rec['Address']

def lambda_handler(event, context):
    output = []
    dynamoDBTableName = os.environ['dynamodb_table_name']
    addressList = getAddressList(dynamoDBTableName)


    for record in event['records']:
        kinesisRecord = json.loads(base64.b64decode(record['data']))
        stationAddRecord = lookupRecord(addressList,kinesisRecord['stationId'])
        kinesisRecord['stationAddress'] = stationAddRecord

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode((json.dumps(kinesisRecord) +"\n").encode("utf-8"))
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}