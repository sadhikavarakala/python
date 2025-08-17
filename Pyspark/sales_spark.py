from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (
    SparkSession.builder
    .appName("SalesTop5Revenue")
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true")
    .getOrCreate()
)

#load csv
gcs_input_path = "gs://sadhika-1-central1/data/sales.csv"
df_raw = (
    spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv("gcs_input_path")
)

# basic cleanup and correct types
df = (
    df_raw
        .withColumn("product", F.trim(F.col("product")))
        .withColumn("quantity", F.col("quantity").cast(T.IntegerType()))
        .withColumn("price", F.col("price").cast(T.DoubleType()))
        .filter(F.col("product").isNotNull() & F.col("quantity").isNotNull() & F.col("price").isNotNull())
        .filter(F.col("quantity") > 0)
        .filter(F.col("price") >= 0)
    )

# revenue per prod = sum(quantity * price)
revenue_per_prod = (
    df
    .withColumn("line_revenue", F.col("quantity") * F.col("price"))
    .groupBy("product")
    .agg(F.round(F.sum("line_revenue"), 2).alias("revenue"))
    .orderBy(F.col("revenue").desc())
    .limit(5)
)

# output

gcs_output_path = "sadhika-1-central1/data/output/top5filtered"
top5.write.mode("overwrite").option("header", "true").csv(gcs_output_path)

print("Done!")

# Spark SQL

# df.createOrReplaceTempView("sales")

# result = spark.sql("""
#                                             SELECT 
#                                                 TRIM(product) AS product,
#                                                 ROUND(SUM(CAST(quantity AS INT) * CAST(price AS DOUBLE)), 2) AS revenue
#                                             FROM sales
#                                             WHERE 
#                                                 product IS NOT NULL
#                                                 AND quantity IS NOT NULL AND CAST(quantity AS INT) > 0
#                                                 AND price IS NOT NULL AND CAST(price AS DOUBLE) >= 0
#                                             GROUP BY TRIM(product)
#                                             ORDER BY revenue DESC
#                                             LIMIT 5
#                                                 """).show(truncate=False)
