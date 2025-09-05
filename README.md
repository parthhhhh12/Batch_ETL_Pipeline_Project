# 📊 Batch ETL Pipeline using PySpark on Azure Databricks  

---

## 📖 Project Overview  

This project demonstrates the design and implementation of a **batch ETL pipeline** using **PySpark in Azure Databricks**.  

The pipeline processes the **NYC Taxi Trip dataset** from raw CSV into cleaned, structured, and aggregated datasets.  
The final output is stored in **Parquet format** within **Azure Blob Storage** for efficient analytics and reporting.  

---

## 🎯 Objectives  

- 📥 Ingest raw CSV data from **Azure Blob Storage**  
- 🧹 Perform **data cleaning, filtering, and type casting**  
- 📊 Apply **aggregations** (e.g., total rides per vendor per day)  
- 💾 Store the final results in **Parquet format** back into Azure Blob Storage  

---

## 🛠️ Tools & Technologies  

- 🔹 **Azure Databricks**  
- 🔹 **PySpark**  
- 🔹 **Azure Blob Storage**  
- 🔹 **Parquet File Format**  
- 🔹 **DBML** (for ER Diagram)  

---

## 📂 Dataset  

**Source:** [NYC Taxi Trip Data – Kaggle](https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc)  

**Schema Highlights:**  

- `VendorID`  
- `pickup_datetime`, `dropoff_datetime`  
- `passenger_count`, `trip_distance`  
- `pickup_location_id`, `dropoff_location_id`  
- `payment details`, `fare_amount`, `tip_amount`, `total_amount`  

---

## 🔄 ETL Pipeline Steps  

1️⃣ **Ingest Raw Data** → Mount or access Azure Blob Storage to read the CSV file  

2️⃣ **Read Data** → Use PySpark DataFrame API with `inferSchema` and `header` options  

3️⃣ **Data Cleaning & Transformation** → Apply `.withColumn()` for type casting + filter invalid rows  

4️⃣ **Aggregation** → Compute total rides per vendor per day using `groupBy()` and `count()`  

5️⃣ **Load Processed Data** → Store final aggregated data in **Parquet format** back into Azure Blob Storage  

6️⃣ **Verification** → Validate results in Azure Cloud Storage  

---

## 🗂️ Data Model (ER Diagram)  

- **RawTripData** → Raw input table with all fields from CSV  
- **CleanedTripData** → Filtered and type-casted dataset  
- **AggregatedTrips** → Aggregated dataset (rides per vendor per day)  

**Relationships:**  

- CleanedTripData is derived from RawTripData  
- AggregatedTrips references CleanedTripData  

---

## 📜 Code Overview  

The PySpark code performs the following operations inside **Databricks Notebook cells**:  

- Read CSV file into DataFrame  
- Clean and type-cast columns  
- Filter invalid rows  
- Aggregate trips per vendor per day  
- Write results in **Parquet format**  

---

## ✅ Conclusion  

This ETL project successfully demonstrates how to:  

- ⚡ Use **PySpark on Azure Databricks** for scalable data processing  
- 🧹 Perform **data cleaning, transformation, and aggregation**  
- 💾 Store processed datasets in **Parquet format** for efficient analytics  

The pipeline ensures **scalability, reliability, and performance**, while making data ready for BI and reporting tools.  

---

## 📂 Repository Contents  

- `README.md` → Project documentation (this file)  
- `Parth_Batch_ETL_Pipeline.docx` → 📥 **Download this file to view the complete detailed project report**  

---

