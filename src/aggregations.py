# transformations.py
from pyspark.sql.functions import col, to_timestamp

def clean_and_transform(raw_df):
    """
    Cleans and transforms raw NYC Taxi data.
    """
    df_clean = (raw_df
        .withColumn("VendorID", col("VendorID").cast("int"))
        .withColumn("lpep_pickup_datetime", to_timestamp("lpep_pickup_datetime", "yyyy-MM-dd HH:mm:ss"))
        .withColumn("lpep_dropoff_datetime", to_timestamp("lpep_dropoff_datetime", "yyyy-MM-dd HH:mm:ss"))
        .withColumn("RatecodeID", col("RatecodeID").cast("int"))
        .withColumn("PULocationID", col("PULocationID").cast("int"))
        .withColumn("DOLocationID", col("DOLocationID").cast("int"))
        .withColumn("passenger_count", col("passenger_count").cast("int"))
        .withColumn("trip_distance", col("trip_distance").cast("double"))
        .withColumn("fare_amount", col("fare_amount").cast("double"))
        .withColumn("extra", col("extra").cast("double"))
        .withColumn("mta_tax", col("mta_tax").cast("double"))
        .withColumn("tip_amount", col("tip_amount").cast("double"))
        .withColumn("tolls_amount", col("tolls_amount").cast("double"))
        .withColumn("ehail_fee", col("ehail_fee").cast("double"))
        .withColumn("improvement_surcharge", col("improvement_surcharge").cast("double"))
        .withColumn("total_amount", col("total_amount").cast("double"))
        .withColumn("payment_type", col("payment_type").cast("int"))
        .withColumn("trip_type", col("trip_type").cast("int"))
        .withColumn("congestion_surcharge", col("congestion_surcharge").cast("double"))
        .filter(col("passenger_count") > 0)
        .filter(col("total_amount") > 0)
        .filter(col("trip_distance") > 0)
    )
    return df_clean
