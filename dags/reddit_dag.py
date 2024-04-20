from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Tawfik Yasser',
    'start_date': datetime(2024, 4, 20)
}

input_file_path = "data/input/reddit_posts.csv"

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Extraction from reddit

extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name':input_file_path
    },
    dag=dag  # Add this line to add the task to the DAG

)

# Upload to S3

upload_to_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

# RUN 
extract >> upload_to_s3