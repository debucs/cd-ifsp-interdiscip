import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 ifsp-cd-staging/diabetes
S3ifspcdstagingdiabetes_node1702128329450 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
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

# Script generated for node Convert datatypes
SqlQuery0 = """
select
    cast(diabetes_012 as int) as diabetes_012
    ,cast(highbp as int) as highbp
    ,cast(highchol as int) as highchol
    ,cast(cholcheck as int) as cholcheck
    ,cast(bmi as float) as bmi
    ,case 
        when cast(bmi as float) is null then -1 --'N/A'
        when cast(bmi as float) = 0     then -1 --'N/A'
        when cast(bmi as float) < 18.5  then 1 --'Abaixo do peso'
        when cast(bmi as float) < 25    then 2 --'Peso normal'
        when cast(bmi as float) < 30    then 3 --'Sobrepeso'
        when cast(bmi as float) < 35    then 4 --'Obesidade grau I'
        when cast(bmi as float) < 40    then 5 --'Obesidade grau II'
        else 6 end as bmi_id
    ,cast(smoker as int) as smoker
    ,cast(stroke as int) as stroke
    ,cast(heartdiseaseorattack as int) as heartdiseaseorattack
    ,cast(physactivity as int) as physactivity
    ,cast(fruits as int) as fruits
    ,cast(veggies as int) as veggies
    ,cast(hvyalcoholconsump as int) as hvyalcoholconsump
    ,cast(anyhealthcare as int) as anyhealthcare
    ,cast(nodocbccost as int) as nodocbccost
    ,cast(genhlth as int) as genhlth
    ,cast(menthlth as int) as menthlth
    ,cast(physhlth as int) as physhlth
    ,cast(diffwalk as int) as diffwalk
    ,cast(sex as int) as sex
    ,cast(age as int) as age
    ,cast(education as int) as education
    ,cast(income as int) as income
from diabetes_raw
"""
Convertdatatypes_node1702231120428 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"diabetes_raw": S3ifspcdstagingdiabetes_node1702128329450},
    transformation_ctx="Convertdatatypes_node1702231120428",
)

# Script generated for node S3 ifsp-cd-raw/diabetes
S3ifspcdrawdiabetes_node1702128633924 = glueContext.write_dynamic_frame.from_options(
    frame=Convertdatatypes_node1702231120428,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://ifsp-cd-raw/diabetes/", "partitionKeys": []},
    format_options={"compression": "gzip"},
    transformation_ctx="S3ifspcdrawdiabetes_node1702128633924",
)

job.commit()
