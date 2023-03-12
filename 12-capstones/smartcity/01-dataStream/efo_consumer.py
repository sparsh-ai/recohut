import boto3
import json
import logging
import base64
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
def lambda_handler(event: dict, _context):
 
  if event and "Records" in event:
    for record in event["Records"]:
 
      try:
        body = record['kinesis']
        data_in_stream_time = body['approximateArrivalTimestamp']
        data = body["data"]
        message_JSON = base64.b64decode(data)
        message_JSON = json.dumps(message_JSON)
        partition_key = {body['partitionKey']}
 
        logger.info(f"Record consumed with partition key: {partition_key} with an approximateArrivalTimestamp : {data_in_stream_time}")
        logger.info(message_JSON)  
       
      except KeyError as err:
          logger.error(err)
          raise err
