Big Data Project: Flight Data Analysis Pipeline
1. Project Overview
Business Problem

Air travel generates massive amounts of data from multiple sources such as flights, airports, delays, and weather.
Analyzing this data at scale is critical for:

Understanding flight delays and cancellations

Identifying high-traffic airports and routes

Supporting data-driven operational and business decisions

The challenge is handling large, multi-source datasets efficiently, transforming them into an analytical format, and enabling fast querying and visualization.

Dataset

The project uses large-scale flight-related datasets, provided as raw files stored in compressed and database-like formats.
These datasets include flight records and related attributes that require cleaning, transformation, and integration.

2. Architecture Overview
Pipeline Flow
Raw Flight Data (ZIP / DB files)
        |
        v
PySpark ETL Processing
(Data cleaning, transformation, joining)
        |
        v
DuckDB
(Analytical storage & fast querying)
        |
        v
Power BI
(Dashboards & visual analytics)

Key Idea

PySpark handles scalable data processing

DuckDB provides fast, SQL-based analytics

Power BI enables business-friendly visualization

3. Project Structure
data/
├── source/
│   ├── source.zip              # Raw flight data (compressed)
│   └── flight_db/              # Raw database or structured files
├── final/                      # Final processed datasets (generated)

spark_env/                      # Spark environment / virtual environment

pipeline_with_prefect.ipynb     # Pipeline with Prefect orchestration (Bonus)
flights_analysis.duckdb         # DuckDB analytical database
combin_file_for_power_BI.py     # Script to prepare data for Power BI
big_data.pbix                   # Power BI dashboard file

4. Technologies Used

Python – Core programming language

PySpark – Distributed data processing

DuckDB – Embedded analytical database

Prefect – Workflow orchestration (Bonus)

Jupyter Notebook – Pipeline development

Power BI – Data visualization and reporting

5. Installation & Setup
5.1 Unzip Source Data
unzip data/source/source.zip -d data/source/

5.2 Create Virtual Environment (Optional)
python -m venv spark_env
source spark_env/bin/activate   # Linux/Mac
spark_env\Scripts\activate      # Windows

5.3 Install Dependencies
pip install pandas duckdb pyspark prefect jupyter

6. Running the Pipeline
Option 1: Standard ETL Pipeline

Open Jupyter Notebook:

jupyter notebook


Run:

pipeline.ipynb

Option 2: Orchestrated Pipeline (Bonus)

Run pipeline_with_prefect.ipynb

This notebook defines and executes a Prefect Flow to orchestrate ETL tasks.

7. Orchestration Files (Bonus)

Prefect Flow Definition

Located in: pipeline_with_prefect.ipynb

Manages:

Data loading

Transformation

Writing to DuckDB

Pipeline execution order and monitoring

8. DuckDB Analytics

After running the pipeline, data is stored in:

flights_analysis.duckdb

Query Example
SELECT *
FROM flights
LIMIT 10;


DuckDB enables fast analytical SQL queries without requiring a separate database server.

9. BI Report (Power BI)
Preparing Data for Power BI

Run:

python combin_file_for_power_BI.py


This script generates combined, BI-ready datasets from DuckDB or processed files.

Viewing the Dashboard

Open big_data.pbix in Power BI Desktop

Refresh the data connection if needed

Explore:

Flight delays

Airport traffic

Route analysis

Time-based trends

10. Team Members & Contributions
Name	Contribution
Nahom	PySpark ETL pipeline development, DuckDB integration
[Member 2]	Data cleaning, transformation logic
[Member 3]	Prefect orchestration & workflow design
[Member 4]	Power BI dashboard & visualization

(Update names as needed)

11. Bonus Components

✅ Workflow Orchestration using Prefect

❌ dbt Models (Not implemented in this project)

12. Conclusion

This project demonstrates a modern big data analytics pipeline, combining:

Distributed processing (PySpark)

Embedded analytics (DuckDB)

Orchestration (Prefect)

Business intelligence (Power BI)

It provides a scalable, efficient foundation for real-world flight data analysis.
