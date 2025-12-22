from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CombineFlightsToParquet") \
    .getOrCreate()

# Read the existing Parquet file
df = spark.read.parquet("data/final/flights_enriched.parquet")

# Write as a single Parquet file
df.coalesce(1).write \
    .mode("overwrite") \
    .parquet("data/final/flights_enriched_single_parquet")

spark.stop()
