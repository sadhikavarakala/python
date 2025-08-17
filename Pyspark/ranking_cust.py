from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (
    SparkSession.builder
    .appName("CustomerRankingSpendApp")
    .getOrCreate()
)

df_orders = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/orders.csv")
)

df_total = (
    df_orders
    .withColumn("amount", F.col("amount").cast(T.DoubleType()))
    .groupBy("customer_id")
    .agg(F.round(F.sum(amount), 2).alias("total_spend"))
)

windowSpec = Window.orderBy(F.col("total_spend").desc())

df_ranking = (
    df_total
    .withColumn("rank", F.rank().over(windowSpec))
    .select("customer_id", "total_spend", "rank")
)

df_ranking.show(truncate=False)