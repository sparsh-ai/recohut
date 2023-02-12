## Search a file in S3

# A business group received 100+ data feeds from different source systems and use Glue or lambda and process the files. To ensure at end of the day, all files are available in the S3 or any source system did not transfer the file for that day, it is important to have a reconciliation process in place. The process will take the require files as input and generate report and sent a list which files are missing. 

# We will make try to achieve a one part of the use case and develop a function which will take input the file name, s3 bucket and prefix and validate whether the file is there in that prefix of the bucket or not. This program can be generalized by taking the file pattern and generate a report and sent via email.

import boto3

def S3FileCheck(file_name,client,bucket_name,bucket_prefix):
    my_bucket = client.Bucket(bucket_name)
    file_obj = []
    for objects in my_bucket.objects.filter(Prefix= bucket_prefix):
         file_obj.append(objects.key)
    s3_file_list = []
    for file in file_obj:
        object_key = str(file)
        s3_file_name = file.split('/')[-1]
        s3_file_list.append(s3_file_name)

    file_check_status = {}
    if file_name in s3_file_list:
        file_check_status['file_name'] =file_name
        file_check_status['file_available_S3'] ='Y'
    else:
         file_check_status['file_name'] =file_name
         file_check_status['file_available_S3'] ='N'
    return file_check_status

client = boto3.resource('s3')
bucket_name = 'sanjeeb-poc-lab-001'
bucket_prefix = 'file_validation'

file_name='test_s3.txt'

file_check_status = S3FileCheck(file_name,client,bucket_name,bucket_prefix)
print(file_check_status)