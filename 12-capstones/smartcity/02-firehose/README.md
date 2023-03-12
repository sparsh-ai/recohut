# Amazon Kinesis Data Firehose

## Description of files
1. station_addresses.csv - Contains the address data for SmartCity bike stations in csv format.
2. loadDynamoDBStationAddresses.py - Python code to load the address data to a Amazon DynamoDB table.
3. TrustPolicyForLambda.json - Contains the trust policy for the role used with the Lambda transform in the KDF delivery stream.
4. KDFSmartCityLambdaPolicy.json - Contains the IAM policy for the role used with the Lambda transform in the KDF delivery stream.
5. KDFLookupAddressTransform.py - The Lambda function to lookup and transform incoming data in KDF to include station address data.
6. CreateLambdaKDFLookupAddressTransform.json - Contains the configuration to create the Lambda function.
7. SmartCityGlueTable.json - Contains the configuration to create the Glue table, whose schema is used by KDF for data format conversion to parquet.
8. TrustPolicyForFirehose.json - Contains the trust policy for the role used with KDF.
9. KDFSmartCityDeliveryStreamPolicy.json - Contains the IAM policy for the role used with KDF.
10. KDFCreateDeliveryStreamSmartCityBikes.json - Contains the configuration to create the KDF delivery stream.
