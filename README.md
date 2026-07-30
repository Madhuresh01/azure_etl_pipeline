# Azure ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline developed using Python and Microsoft Azure services.

This project extracts sales data, performs data cleaning and transformation, loads the processed data into Azure SQL Database and Azure Blob Storage, generates visual reports, sends automated email notifications, and maintains execution history.

---

## Project Overview

The objective of this project is to simulate a production-style cloud ETL workflow using Python and Azure services.

The pipeline performs:

- Data Extraction
- Data Cleaning & Transformation
- Local CSV Generation
- Azure SQL Upload
- Azure Blob Storage Upload
- Sales Visualization
- Automated Email Notification
- Execution History Logging

---

## Technologies Used

- Python 3
- Microsoft Azure SQL Database
- Azure Blob Storage
- SQLite
- Pandas
- Matplotlib
- PyODBC
- Azure Storage SDK
- SMTP Email
- Dotenv
## Features

- Extract sales data from CSV
- Optional Azure SQL extraction
- Data cleaning and preprocessing
- Upload transformed data to Azure SQL Database
- Upload processed CSV to Azure Blob Storage
- Generate sales visualization
- Send HTML email reports
- Maintain pipeline execution history
- Logging with execution stages
- Configuration using environment variables
- Retry mechanism for cloud operations
## Project Structure

```text
ETL_Capstone
│
├── assets
├── data
├── etl
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   ├── azure_loader.py
│   ├── azure_sql_reader.py
│   ├── blob_storage.py
│   ├── emailer.py
│   ├── viz.py
│   ├── config.py
│   ├── logger.py
│   ├── history.py
│   └── utils.py
│
├── reports
├── templates
├── logs
├── run_etl.py
├── requirements.txt
└── README.md
```
## ETL Workflow

1. Validate Configuration
2. Extract Data
3. Transform Data
4. Save Clean CSV
5. Upload to Azure SQL Database
6. Upload to Azure Blob Storage
7. Generate Sales Visualization
8. Send Email Notification
9. Save Pipeline Execution History
10. Display Pipeline Summary

## Azure Services Used

- Azure SQL Database
- Azure Blob Storage
- Azure Storage Account
- Azure Portal

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure all required environment variables.

Run the ETL pipeline

```bash
python run_etl.py
```

## Environment Variables

The project uses a `.env` file for configuration.

Example variables:

- CSV_PATH
- REPORT_DIR
- AZURE_SQL_SERVER
- AZURE_SQL_DATABASE
- AZURE_SQL_USERNAME
- AZURE_SQL_PASSWORD
- AZURE_SQL_TABLE
- AZURE_SQL_DRIVER
- AZURE_STORAGE_CONNECTION_STRING
- AZURE_CONTAINER_NAME
- AZURE_BLOB_NAME
- SMTP_SERVER
- SMTP_PORT
- SMTP_USER
- SMTP_PASS
- TO_ADDRESS
- EMAIL_SUBJECT

## Pipeline Output

After successful execution, the pipeline performs the following:

- Cleans and transforms sales data
- Saves cleaned CSV locally
- Uploads data to Azure SQL Database
- Uploads cleaned CSV to Azure Blob Storage
- Generates sales visualization
- Sends email notification
- Stores execution history in SQLite

## Screenshots

- ETL Pipeline Execution
- Azure SQL Upload
- Azure Blob Storage Upload
- Sales Visualization
- Email Notification

## Future Improvements

- Schedule pipeline using Azure Data Factory
- Docker container support
- CI/CD using GitHub Actions
- Power BI dashboard integration
- Data validation framework
- Unit testing
- Monitoring and alerting

## Author

**Madhuresh**

Azure ETL Pipeline Capstone Project

Developed using Python and Microsoft Azure Cloud Services.