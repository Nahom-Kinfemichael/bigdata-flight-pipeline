Big Data Project: Flight Data Analysis Pipeline
Overview
This repository contains a big data processing pipeline for flight-related data. It includes source data, processing scripts, notebooks for orchestration, and analysis outputs using DuckDB and potentially Power BI.
The goal is to process large-scale flight data, combine sources, build an ETL pipeline, and enable efficient querying and visualization.
Project Structure

data/
final/: Processed or final datasets (currently empty or not included).
source/
source.zip: Compressed archive containing the raw/source flight data files.
flight_db: Directory with raw database or data files.


spark_env: Directory for Spark environment configuration or virtual environment.
big_data.pbix: Power BI file for visualizations and dashboards built from the processed data.
combin_file_for_power_BI.py: Python script to combine or prepare data files specifically for import into Power BI.
flights_analysis.duckdb: DuckDB database file containing processed flight data for fast analytical queries.
pipeline_with_prefect.ipynb: Jupyter notebook implementing the data pipeline using Prefect for orchestration and workflow management.
pipeline.ipynb: Main Jupyter notebook for the data processing pipeline (exploration, ETL steps, etc.).

Technologies Used

Python: Core scripting language.
DuckDB: Embedded analytical database for efficient querying of the processed data.
Prefect: Workflow orchestration (used in one of the notebooks).
Jupyter Notebooks: For interactive development and pipeline definition.
Power BI: For data visualization (via the .pbix file and preparation script).
Potentially Apache Spark (inferred from spark_env).

Setup and Usage

Unzip the source data:textunzip data/source/source.zip -d data/source/
Install dependencies:
Create a virtual environment if needed.
Install required packages (based on scripts/notebooks):textpip install pandas duckdb prefect jupyter pyspark powerbi-related-libs-if-any

Run the pipeline:
Open and execute pipeline.ipynb or pipeline_with_prefect.ipynb in Jupyter.
This will process the raw data, populate the DuckDB database, and prepare files for Power BI.

Run the combination script for Power BI:textpython combin_file_for_power_BI.pyThis generates combined files suitable for loading into big_data.pbix.
Query the data:
Use DuckDB directly:textduckdb flights_analysis.duckdb
Or open big_data.pbix in Power BI for visualizations.