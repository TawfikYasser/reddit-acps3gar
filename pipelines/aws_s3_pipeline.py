import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from utils.constants import AWS_BUCKET
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3

def upload_s3_pipeline(ti):
    file_path=ti.xcom_pull(task_ids='reddit_extraction', key='return_value')
    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_BUCKET)
    upload_to_s3(s3, file_path, AWS_BUCKET, file_path.split('/')[-1])