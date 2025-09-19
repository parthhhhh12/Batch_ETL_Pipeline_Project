from pyspark.sql.functions import count, sum, date_format

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
display(agg_df)

# Writing transformed data
agg_df.write.mode("overwrite").parquet("/mnt/parth/ETL_Pipeline_Project/staged/raw_df")
