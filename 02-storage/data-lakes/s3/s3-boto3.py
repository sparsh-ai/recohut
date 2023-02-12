# AWS S3 Python Utilities

import os
import glob
import json

import boto3
from botocore.exceptions import ClientError
import configparser
import matplotlib.pyplot as plt
import pandas as pd
from time import time      
import datetime as dt
  

def s3_create_bucket(s3c, s3r, location, bucket_name):
    """
    Summary line. 
    Creates an S3 bucket, if it does not exist
  
    Parameters: 
    arg1 (S3 Client)
    arg2 (S3 Resource)
    arg3 (AWS Region)
    arg4 (Bucket name)
  
    Returns: None
    """     

    # Check if S3 bucket exists
    if( s3r.Bucket(bucket_name) in s3r.buckets.all() ):
        print('{} : {} {} {}'.format('S3', 'bucket', bucket_name, 'exists'))
    else:
        s3c.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration=location)
        print('{} : {} {} {}'.format('S3', 'bucket', bucket_name, 'created'))

def s3_list_buckets(s3c):
    """
    Summary line. 
    Displays S3 Buckets
  
    Parameters: 
    arg1 (S3 Client)
  
    Returns: None
    """     

#    for bucket in s3r.buckets.all():
#         print(bucket)
    try:
        # Call S3 to list current buckets
        response = s3c.list_buckets()
        print('Total Buckets = ',len(response['Buckets']))
        for num, bucket in enumerate(response['Buckets'], start=1):
        #for bucket in response['Buckets']:
            print ('{}. {}'.format(num, bucket['Name']))
    except ClientError as e:
        print("The bucket does not exist, choose how to deal with it or raise the exception: "+e)
        return
        
def s3_delete_bucket(s3r, bucket_name):
    """
    Summary line. 
    Deletes S3 Bucket after emptying the bucket
  
    Parameters: 
    arg1 (S3 Resource)
    arg2 (Bucket name)
  
    Returns: None
    """     

    bucket = s3r.Bucket(bucket_name)
    
    # suggested by Jordon Philips 
    bucket.objects.all().delete()    
    bucket.delete()    
    print('{} : {} {} {}'.format('S3', 'bucket', bucket_name, 'deleted'))


def local_get_all_files(folders):
    """
    Summary line. 
    Scans folder and prepares files list except folders starting with '.'
  
    Parameters: 
    arg1 (Folder names in array)
  
    Returns: 
    Return1 (Array of Selected files)
    Return2 (Array of Ignored files)
    """     
    
    selected_files, ignored_files = [], []    
    
    # 1. checking your current working directory
    print('Current Working Directory : ',os.getcwd())

    for folder in folders:
        # Get your current folder and subfolder event data
        filepath = os.getcwd() + '/' + folder
        print('Scanning Directory : ',filepath)

        # 2. Create a for loop to create a list of files and collect each filepath
        #    join the file path and roots with the subdirectories using glob
        #    get all files matching extension from directory

        for root, dirs, files in os.walk(filepath):
            files = glob.glob(os.path.join(root,'*.*'))
            #print('root = ',root)
            #print('dirs = ',dirs, ' : ',len(dirs))

            # Below condition is to ignore directories like ['.ipynb_checkpoints']
            dotdir = root.split('/')[-1]
            #print('dotdir = ',dotdir[0:1], 'length = ',len(dotdir))
            if( (dotdir[0:1]!='.' and len(dotdir) > 1) or (dotdir[0:1]=='.' and len(dotdir)==1) ):
                #print(files)
                for f in files :
                    selected_files.append(os.path.abspath(f))
            else:
                ignored_files.append(root)

    # 3. get total number of files found
    print('{} files found, {} files ignored'.format(len(selected_files), len(ignored_files) ))
    #print(all_files)
    return selected_files, ignored_files

def s3_upload_files(s3c, bucket_name, selected_files, rFindStr, rStr):
    """
    Summary line. 
    Upload only files to S3 will fail when a directory is encountered in the filepath
  
    Parameters: 
    arg1 (S3 Client)
    arg2 (Bucket name)
    arg3 (Selected files list)
    arg4 (Find string to replace)
    arg5 (String to be replaced with)
  
    Returns: None
    """     

    print('Uploading {} files to S3'.format(len(selected_files)))
    for f in selected_files:
        f = f.replace(rFindStr, rStr)
        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.    
        s3c.upload_file(f, bucket_name, f)

def s3_upload_parquet_files(s3, bucket_name, folder, path):
    """
    Summary line. 
    Uploads files/directories to S3
  
    Parameters: 
    arg1 : (S3 resource object)
    arg2 : (Bucket name)
    arg3 : (filename)
    arg4 : (local File path)
  
    Returns: None
    """        
    
    bucket = s3.Bucket(bucket_name)
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                #print('Fullpath : ',full_path)
                #print(full_path[len(path)+1:])
                #print(folder+'/'+full_path[len(path)+1:])
                #bucket.upload_file('/tmp/' + filename, '<bucket-name>', 'folder/{}'.format(filename))
                bucket.put_object(Key=folder+'/'+full_path[len(path)+1:], Body=data)                

                
def delete_filetype_in_s3_bucket(s3c, bucket_name, delete_files, delete_types):
    """
    Summary line. 
    Delete specific files & file types from s3 bucket
  
    Parameters: 
    arg1 : (S3 client object)
    arg2 : (Bucket name)
    arg3 : (array of files to be deleted)
    arg4 : (array of file types)
  
    Returns: None
    """        
    
    try:
        response = s3c.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print('{:13} {:25}   {:10}   {}(Total scanned files={}) '.format('Action', 'Date', 'Size', 'Filename', len(response['Contents']) ))
            for item in response['Contents']:
                if(item['Key'].split('.')[-1] in delete_types):
                    print('{:13} {} : {:10} : {} '.format('deleting file', item['LastModified'], item['Size'], item['Key']))           
                    s3c.delete_object(Bucket=bucket_name, Key=item['Key'])

                if(item['Key'].split('/')[-1] in delete_files):
                    print('{:13} {} : {:10} : {} '.format('deleting file', item['LastModified'], item['Size'], item['Key']))           
                    s3c.delete_object(Bucket=bucket_name, Key=item['Key'])
    except ClientError as e:
        print("Check if the bucket {} exists!".format(bucket_name))
        print("Exception message : "+e)
        return