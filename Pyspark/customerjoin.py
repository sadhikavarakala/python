from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (
    SparkSession.builder
    .appName("CustomerJoinApp")
    .getOrCreate()
)

df_cust = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/customers.csv")
)

df_orders = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/orders.csv")
)

#  Register DataFrames as SQL views
df_cust.createOrReplaceTempView("customers")
df_orders.createOrReplaceTempView("orders")

df_join = spark.sql("""
                    SELECT 
                        c.customer_name,
                        o.order_id,
                        o.order_date,
                        o.amount
                    FROM customers c
                    INNER JOIN orders o ON c.customer_id = o.customer_id
                    WHERE 
                        o.order_date > '2024-11-01'
                    ORDER BY o.order_date
                    """)

df_join.show(truncate=False)

# equivalent pyspark (no SQL)

df_orders_clean = df_orders.withColumn("order_date", F.to_date(F.col("order_date"), "yyyy-MM-dd"))

df_join_pyspark = (
    df.cust
    .join(df_orders_clean, on="customer_id", how="inner")
    .filter(F.col("order_date") > F.lit("2024-11-01"))
    .select("customer_name", "order_id", "order_date", "amount")
    .orderBy("order_date")
)

df_join.show(truncate=False)


