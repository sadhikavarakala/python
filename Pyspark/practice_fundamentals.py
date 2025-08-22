#creating dataframe

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Practice").getOrCreate()

data = [("Maddy", "24"), ("Sandy", "40")]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()
    
