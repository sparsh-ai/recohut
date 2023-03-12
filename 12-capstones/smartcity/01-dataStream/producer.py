import json
import uuid
import boto3

stream_name = "smartcity-emergency-system-events"

message_json = {
  "record_id": "18742",
  "date_and_time": "2020-11-14T15:53:00.000",
  "notificationtype": "Weather",
  "notification_title": "Coastal Flood Statement (BK)",
  "email_body": "Notification issued 11-15-2020 at 3:53 PM.   The National Weather Service has issued the following: What: Coastal Flood Statement Where: Brooklyn When: 6 AM to10 AM on 11/15 Hazards: Above normal tidal departures may result in minor flooding of shore roads and/or properties. ..."
}

kinesis = boto3.client('kinesis')
data = json.dumps(message_json)
partition_key = str(uuid.uuid4())
resp = kinesis.put_record(
        StreamName=stream_name,
        Data=data,
        PartitionKey=partition_key)
        
print(json.dumps(resp))

