import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import concat, col, lit

import pyspark.sql.functions as func

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# create DynamicFrame from source table
dyf = glue_context.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={"dynamodb.input.tableName": 'ranked_pod_image_information-beta-us-east-1',
        "dynamodb.throughput.read.percent": "1.0",
        "dynamodb.splits": "100"
    }
)

# convert dyf to spark dataframe
df = dyf.toDF()


# create a new column called imageId_modelVersion and concatenate imageId + "#" + modelVersion
df1 = df.withColumn("imageId_modelVersion", concat(col("imageId"), lit("#"), col("modelVersion")))

df2 = df1.select(
    col("imageId"),
    col("imageId_modelVersion"),
    col("creationDate")
)

df3 = df2.withColumn("imageCreationDateInMilliSeconds", col("creationDate")/1000)
df4 = df3.withColumn("imageCreationDateInMilliSecondsRounded", func.round(col("imageCreationDateInMilliSeconds"), 0))
df5 = df4.withColumn("correctTTL", col("imageCreationDateInMilliSecondsRounded") + 30240000)


# turn imageId_modelVersion + imageId spark dataframe back into a Glue DynamicFrame
imageId_and_sortKeyDYF = DynamicFrame.fromDF(df5, glue_context, "df5")

# join at imageId
merged_DYF = dyf.join(paths1=["imageId"], paths2=["imageId"], frame2=imageId_and_sortKeyDYF)
merged_DYF1 = merged_DYF.drop_fields(paths=['`.imageId`', '`.creationDate`', '`creationDate`', '`ttl`', '`imageId_modelVersion`', '`addressId_ReasonCode_compositeKey`', '`imageCreationDateInMilliSeconds`'])

# get creationDate column, get time in millis, add 350 days, create ttl column
merged_DYF2 = merged_DYF1.rename_field("imageCreationDateInMilliSecondsRounded", "imageCreationDate")
final_DYF = merged_DYF2.rename_field("correctTTL", "ttl")


# write DynamicFrame to target table
glue_context.write_dynamic_frame_from_options(
    frame=final_DYF,
    connection_type="dynamodb",
    connection_options={"dynamodb.output.tableName": 'pod_ranking_information',
        "dynamodb.throughput.write.percent": "1.0"
    }
)
job.commit()

