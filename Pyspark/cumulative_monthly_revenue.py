from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import types as t

spark = (
    SparkSession.builder
    .appName("CumulativeMonthlyRevenueApp")
    .getOrCreate()
)

df_orders = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/orders.csv")
)

df_cumulative_revenue = (
    df_orders
    .withColumn("order_date", f.to_date(f.col("order_date")))
    .withColumn("year_month", f.date_format(f.col("order_date"), 'yyyy-MM'))
    .groupBy("year_month")
    .agg(f.round(f.sum("amount"), 2).alias("total_revenue"))
    .withColumn("cumulative_revenue", f.sum("total_revenue").over(Window.orderBy("year_month").rowsBetween(Window.unboundedPreceding, 0)))
    .select("year_month", "total_revenue", "cumulative_revenue")
)

df_cumulative_revenue.show(truncate=False)