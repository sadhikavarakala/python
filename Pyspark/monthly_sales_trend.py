from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (
    SparkSession.builder
    .appName("MonthlySalesTrendApp")
    .getOrCreate()
)

df_orders = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/orders.csv")
)

df_monthly_trend = (
    df_orders
    .withColumn("order_date", F.to_date(F.col("order_date")))
    .withColumn("year_month", F.date_format(F.col("order_date"), "yyyy-MM"))
    .groupBy("year_month")
    .agg(
        F.round(F.sum("amount").cast(T.DoubleType()), 2).alias("total_revenue")
    )
    .orderBy("year_month")
    .select("year_month", "total_revenue")
)

df_monthly_trend.show(truncate=False)