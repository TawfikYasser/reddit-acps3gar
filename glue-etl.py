import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1713633618514 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://reddit-s3-bucket/raw/reddit_cleaned.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1713633618514")


# convert DynamicFrame to DataFrame

df = AmazonS3_node1713633618514.toDF()
# Transform

df['title'] = df['title'].apply(lambda x: x.title())

S3bucket_node_combined = DynamicFrame.fromDF(df, glueContext, 'S3bucket_node_combined') 

# Script generated for node Amazon S3
AmazonS3_node1713633619939 = glueContext.write_dynamic_frame.from_options(frame=S3bucket_node_combined, connection_type="s3", format="csv", connection_options={"path": "s3://reddit-s3-bucket/transformed/", "compression": "snappy", "partitionKeys": []}, transformation_ctx="AmazonS3_node1713633619939")

job.commit()