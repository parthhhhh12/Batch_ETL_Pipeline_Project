📊 Batch ETL Pipeline using PySpark on Azure Databricks
📖 Project Overview

This project demonstrates the design and implementation of a batch ETL pipeline using PySpark on Azure Databricks.

The pipeline processes the NYC Taxi Trip dataset from raw CSV files into cleaned, structured, and aggregated Parquet files, which are stored in Azure Blob Storage for efficient analytics and reporting.

🎯 Objectives

📥 Read raw CSV data from Azure Blob Storage

🧹 Perform data cleaning, filtering, and type casting

📊 Apply aggregations (e.g., total rides per vendor per day)

💾 Store final results in Parquet format back to Azure Blob Storage

🛠️ Tools & Technologies

🔹 Azure Databricks

🔹 PySpark

🔹 Azure Blob Storage

🔹 Parquet File Format

🔹 DBML (for ER Diagram)

📂 Dataset

Source: NYC Taxi Trip Data – Kaggle

Schema Highlights:

VendorID

pickup_datetime, dropoff_datetime

passenger_count, trip_distance

pickup_location_id, dropoff_location_id

fare_amount, tip_amount, total_amount

🔄 ETL Pipeline Steps

1️⃣ Ingest Raw Data → Load CSV from Azure Blob into Databricks

2️⃣ Data Cleaning & Transformation → Type casting + filtering invalid rows using PySpark

3️⃣ Aggregation → Compute total rides per vendor per day

4️⃣ Load Processed Data → Write aggregated dataset in Parquet format back to Azure Blob Storage

🗂️ Data Model

RawTripData → Raw input table (direct from CSV)

CleanedTripData → Filtered & type-casted dataset

AggregatedTrips → Summary dataset (rides per vendor per day)

✅ Conclusion

This project demonstrates how PySpark on Azure Databricks can:

⚡ Process large-scale datasets in the cloud

🔒 Ensure reliability, scalability, and efficiency

📈 Deliver analytics-ready data in Parquet format for BI & reporting tools
