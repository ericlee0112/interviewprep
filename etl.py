import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import concat, col, lit
from awsglue.gluetypes import StructType, Field, StringType, DoubleType, LongType

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

schema = StructType(
  [Field("addressId_ReasonCode_compositeKey", StringType()),
  Field("imageId_modelVersion", StringType()),
  Field("score", DoubleType()),
  Field("reasonCode", StringType()),
  Field("imageId", StringType()),
  Field("creationDate", LongType()),
  Field("ttl", LongType()),
  Field("modelVersion", StringType()),
  Field("addressId", StringType())])


dyf = glue_context.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={"dynamodb.input.tableName": 'ranked_pod_image_information-beta-us-east-1',
        "dynamodb.throughput.read.percent": "1.0",
        "dynamodb.splits": "100"
    }
)
print(dyf.schema())

# convert dyf to spark dataframe
df = dyf.toDF()

df1 = df.select(
    col("imageId"),
    col("addressId"),
    col("score"),
    col("modelVersion"),
    col("reasonCode"),
    col("ttl"),
    col("creationDate")
)

dyf1 =  DynamicFrame.fromDF(df1, glue_context, "df1")

final_DYF = dyf1.rename_field("creationDate", "imageCreationDate")

print(final_DYF.schema())
print(final_DYF.show())

glue_context.write_dynamic_frame_from_options(
    frame=final_DYF,
    connection_type="dynamodb",
    connection_options={"dynamodb.output.tableName": 'testtable',
        "dynamodb.throughput.write.percent": "1.0"
    },
)


job.commit()