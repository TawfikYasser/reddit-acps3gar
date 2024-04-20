import s3fs
import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_SECRET_KEY

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False, 
                            key = AWS_ACCESS_KEY_ID,
                            secret= AWS_ACCESS_SECRET_KEY)
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name: str):
    try:
        if not s3.exists(bucket_name):
            s3.makedir(bucket_name)
            print('Bucket Created')
        else:
            print('Bucket already exists')
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket_name: str, s3_file_name: str):
    try:
        s3.put(file_path, bucket_name+'/raw/'+s3_file_name)
        print('File uploaded')
    except FileNotFoundError:
        print('The file was not found')