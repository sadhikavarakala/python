from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (
    SparkSession.builder
    .appName("CustomerApp")
    .getOrCreate()
)

df_raw = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/customers.csv")
)

#clean 

df = (
    df_raw
        .withColumn("order_date", F.to_date(F.col("order_date"), "yyyy-MM-dd"))
        .withColumn("amount", F.col("amount").cast(T.DoubleType()))
        .filter(F.col("customer_id").isNotNull() & F.col("order_date").isNotNull())
        .filter(~((F.col("amount") < 0 | F.col("amount") > 100000)))
)

df.select("order_id", "customer_id", "order_date", "amount").show(truncate=False)
