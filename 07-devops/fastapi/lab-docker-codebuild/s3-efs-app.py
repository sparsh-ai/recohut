import boto3
import os

model_dir = os.getenv('MODEL_DIR', '/mnt/ml/models/')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    raw_dir = os.path.join(model_dir, 'raw')
    processed_dir = os.path.join(model_dir, 'processed')
    
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    save_path = os.path.join(model_dir, key)
    
    print(save_path)
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    s3.download_file(bucket_name, key, save_path)
    
    print("ML Model file downloaded!")