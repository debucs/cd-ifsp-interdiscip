import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 ifsp-cd-staging/diabetes
S3ifspcdstagingdiabetes_node1702128329450 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://ifsp-cd-staging/diabetes/diabetes_012_health_indicators_BRFSS2015.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="S3ifspcdstagingdiabetes_node1702128329450",
)

# Script generated for node S3 ifsp-cd-raw/diabetes
S3ifspcdrawdiabetes_node1702128633924 = glueContext.write_dynamic_frame.from_options(
    frame=S3ifspcdstagingdiabetes_node1702128329450,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://ifsp-cd-raw/diabetes/", "partitionKeys": []},
    format_options={"compression": "gzip"},
    transformation_ctx="S3ifspcdrawdiabetes_node1702128633924",
)

job.commit()
