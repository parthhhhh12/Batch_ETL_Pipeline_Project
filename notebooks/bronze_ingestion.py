# MOUNTING
storage_account_name = "deaatraining25"
container_name = "parth"
mount_point = "/mnt/parth"

# Use either storage account key or service principal for authentication
storage_account_access_key = "..."

configs = {
    f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_access_key
}

# Mount if not already mounted
if not any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):
    dbutils.fs.mount(
        source=f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
        mount_point=mount_point,
        extra_configs=configs
    )
else:
    print(f"{mount_point} is already mounted")

# Reading raw data
raw_df = spark.read.option("header", True).option("inferSchema", True).csv("/mnt/parth/nyc_taxi_trip_data.csv")
display(raw_df)
display(raw_df.schema)
