# reddit-acps3gar
Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

- pip install apache-airflow
- pip install praw
- pip install pandas
- pip install numpy
- mkdir config dags data etls logs pipelines tests utils
- mkdir -p logs/scheduler/2024-04-20
- touch airflow.env docker-compose.yml Dockerfile requirements.txt
- pip install configparser


- sudo docker compose up -d --build
- pip install awscli
- pip install s3fs

- awscli-1.32.88 botocore-1.34.88 colorama-0.4.4 docutils-0.16 rsa-4.7.2

- reddit-s3-bucket
- Glue ETL Job
- Glue Crawler to create a database with table containing the data (create db)
- Amazon Athena to preview the data using sql