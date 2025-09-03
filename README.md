📊 Batch ETL Pipeline using PySpark on Azure Databricks

This project demonstrates the design and implementation of a batch ETL pipeline using PySpark on Azure Databricks. The pipeline processes the NYC Taxi Trip dataset from raw CSV into cleaned, structured, and aggregated data, and stores the results in Parquet format on Azure Blob Storage for efficient analytics.

🚀 Objectives

Read raw CSV data from Azure Blob Storage

Perform data cleaning, filtering, and type casting

Apply aggregations (e.g., total rides per vendor per day)

Store final results in Parquet format back to Azure Blob Storage

🛠️ Tools & Technologies

Azure Databricks

PySpark

Azure Blob Storage

Parquet File Format

DBML (for ER Diagram)

📂 Dataset

NYC Taxi Trip Data (Kaggle dataset: https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc?utm_source=chatgpt.com )

Fields include: VendorID, pickup/dropoff timestamps, passenger count, trip distance, location IDs, payment details, fare, tips, and total amount.

🔄 ETL Pipeline Steps

Ingest raw CSV data from Azure Blob into Databricks.

Clean & Transform data with PySpark (type casting, filtering invalid rows).

Aggregate rides per vendor per day.

Load the final dataset into Parquet format in Azure Blob.

📊 Data Model

RawTripData → raw input table.

CleanedTripData → filtered and type-casted table.

AggregatedTrips → summary table (rides per vendor per day).

✅ Conclusion

This project shows how PySpark and Databricks can process large-scale data in the cloud, ensuring reliability, scalability, and efficiency. Using Parquet files makes the results analytics-ready for reporting and BI tools.
