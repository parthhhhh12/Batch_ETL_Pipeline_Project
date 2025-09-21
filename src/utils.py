# utils.py
def mount_storage(storage_account_name, container_name, mount_point, storage_account_access_key):
    """
    Mounts Azure Blob storage to Databricks.
    """
    configs = {
        f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_access_key
    }

    if not any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):
        dbutils.fs.mount(
            source=f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
            mount_point=mount_point,
            extra_configs=configs
        )
    else:
        print(f"{mount_point} is already mounted")


def read_raw_data(spark, file_path):
    """
    Reads raw CSV data from mounted storage.
    """
    return spark.read.option("header", True).option("inferSchema", True).csv(file_path)


def write_to_parquet(df, output_path):
    """
    Writes DataFrame to Parquet format.
    """
    df.write.mode("overwrite").parquet(output_path)
