from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import tyoes as T

spark = (
    SparkSession.builder
    .appName("SalesPerDay")
    .getOrCreate()
)

df_raw = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("gs://sadhika-1-central1/data/sales.csv")
)

# clean
df = (
    df_raw
        .withColumn("product", F.trim(F.col("product")))
        .withColumn("quantity", F.col("quantity").cast(T.IntegerType()))
        .withColumn("price", F.col("price").cast(T.DoubleType()))
        .withColumn("date", F.to_date(F.col("date"), "yyyy-MM-dd"))
        .filter(F.col("product").isNotNull() & F.col("quantity").isNotNull() & F.col("price").isNotNull() & F.col("date").isNotNull())
        .filter(F.col("quantity") > 0)
        .filter(F.col("price") >= 0)
)

# total revenue per day
revenue_per_day = (
    df
    .withColumn("revenue", F.col("quantity") * F.col("price"))
    .groupBy("date")
    .agg(F.round(F.sum("revenue"), 2).alias("total_revenue"))
    .orderBy(F.col("date"))
)

df.show(revenue_per_day)

df.revenue_per_day("sales")

result = spark.sql("""
                    SELECT 
                        TRIM(product) AS product,
                        ROUND(SUM(CAST(quantity AS INT) * CAST(price AS DOUBLE)), 2) AS revenue
                        CAST(date AS DATE) AS date
                    FROM sales
                    WHERE 
                        product IS NOT NULL AND quantity IS NOT NULL AND price IS NOT NULL AND date IS NOT NULL
                   GROUP BY 
                       TRIM(product), CAST(date AS DATE)
                   ORDER BY 
                       CAST(date AS DATE)
                   """)
