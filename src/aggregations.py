# aggregations.py
from pyspark.sql.functions import count, sum, date_format

def aggregate_trips(df_clean):
    """
    Aggregates trip data to calculate daily stats by VendorID.
    """
    agg_df = (df_clean
        .withColumn("pickup_date", date_format("lpep_pickup_datetime", "yyyy-MM-dd"))
        .groupBy("VendorID", "pickup_date")
        .agg(
            count("*").alias("total_trips"),
            sum("fare_amount").alias("total_fare"),
            sum("tip_amount").alias("total_tips"),
            sum("total_amount").alias("total_revenue")
        )
    )
    return agg_df


