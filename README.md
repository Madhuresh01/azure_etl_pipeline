# Azure ETL Pipeline using Python

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

This project implements a complete End-to-End ETL (Extract, Transform, Load) pipeline using Python. The pipeline automates the complete lifecycle of structured sales data by extracting records from CSV files or Azure SQL Database, performing data cleaning and transformation, storing processed data into multiple destinations, generating visual reports, and sending automated email notifications.

The project has been designed with a modular architecture where every stage of the ETL process is implemented independently. This makes the application easy to maintain, test, extend, and deploy.

The solution integrates local storage with Microsoft Azure cloud services and demonstrates practical implementation of data engineering concepts including data extraction, transformation, loading, visualization, cloud storage, relational databases, automated reporting, configuration management, logging, and unit testing.

---

## Problem Statement

Organizations frequently receive sales data from multiple sources in raw CSV format. These datasets often require cleaning, validation, transformation, storage, visualization, and reporting before they can be used for business analysis.

Performing these operations manually introduces several challenges:

- Repetitive manual effort
- Data inconsistency
- Increased probability of human error
- Lack of centralized storage
- No automated reporting
- Poor scalability
- Difficult maintenance

This project addresses these challenges by automating the complete ETL workflow.

---

## Project Objectives

The primary objectives of this project are:

- Build a reusable ETL pipeline using Python
- Extract sales data from CSV files
- Read sales data directly from Azure SQL Database
- Clean and transform raw datasets
- Save processed datasets locally
- Store processed data inside Azure SQL Database
- Upload processed files to Azure Blob Storage
- Generate sales visualization automatically
- Generate HTML email reports
- Send automated email notifications
- Maintain execution history
- Log every execution step
- Validate project configuration
- Create automated unit tests for core ETL modules

---

## Key Features

The application provides the following functionality:

### Data Extraction

- Extract sales records from CSV
- Read records from Azure SQL Database
- Configuration-based source selection

### Data Transformation

- Remove duplicate records
- Handle missing values
- Standardize dataset
- Clean inconsistent data
- Prepare dataset for loading

### Local Storage

- Save cleaned CSV
- Maintain processed datasets
- Preserve execution history

### Database Integration

- SQLite integration
- Azure SQL Database upload
- Azure SQL Database read support

### Azure Cloud Integration

- Upload processed CSV to Azure Blob Storage
- Secure connection using Azure Storage Connection String

### Reporting

- Generate sales visualization
- Create HTML email report
- Automatically attach generated report

### Email Automation

- SMTP integration
- Gmail App Password authentication
- Automatic report delivery

### Testing

- Unit testing using PyTest
- Independent test cases for ETL modules
- Automated validation of pipeline components

---

## Complete ETL Workflow

```
                CSV File
                    │
                    │
                    ▼
            Data Extraction
                    │
                    ▼
         Data Cleaning & Transformation
                    │
                    ▼
          Save Cleaned CSV Locally
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
    SQLite Database       Azure SQL Database
                                │
                                ▼
                     Azure Blob Storage Upload
                                │
                                ▼
                     Generate Sales Visualization
                                │
                                ▼
                     Generate HTML Email Report
                                │
                                ▼
                       Send Email Notification
```

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.13 |
| Data Processing | Pandas |
| Local Database | SQLite |
| Cloud Database | Azure SQL Database |
| Cloud Storage | Azure Blob Storage |
| Visualization | Matplotlib |
| Email Service | SMTP (Gmail) |
| HTML Reports | HTML |
| Configuration | Python Dotenv |
| Logging | Python Logging Module |
| Testing | PyTest |

---

## Azure Services Used

This project integrates with the following Microsoft Azure services:

### Azure SQL Database

Used for:

- Reading sales records
- Uploading transformed data
- Cloud-based relational storage

### Azure Blob Storage

Used for:

- Uploading cleaned CSV files
- Centralized cloud storage
- File management

---

## Project Architecture

The project follows a modular architecture.

Each module performs a single responsibility, making the application scalable, maintainable, and easier to test.

```
run_etl.py
      │
      ▼
Configuration Validation
      │
      ▼
Extractor
      │
      ▼
Transformer
      │
      ▼
Loader
      │
      ├────────► SQLite
      │
      ├────────► Azure SQL
      │
      ├────────► Azure Blob Storage
      │
      ├────────► Visualization
      │
      └────────► Email Report
```
## Project Structure

```
ETL_Capstone/
│
├── data/
│   ├── sales_data.csv
│   ├── cleaned_sales_data.csv
│   └── pipeline_history.db
│
├── etl/
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   ├── azure_loader.py
│   ├── azure_sql_reader.py
│   ├── blob_storage.py
│   ├── emailer.py
│   ├── viz.py
│   ├── history.py
│   ├── logger.py
│   ├── utils.py
│   ├── config.py
│   └── validation.py
│
├── templates/
│   └── email_template.html
│
├── reports/
│   └── sales_chart.png
│
├── logs/
│   └── pipeline.log
│
├── tests/
│   ├── conftest.py
│   ├── test_extractor.py
│   ├── test_transformer.py
│   ├── test_loader.py
│   └── test_viz.py
│
├── run_etl.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Module Description

## run_etl.py

This file acts as the project entry point.

Responsibilities:

- Validate configuration
- Select execution source
- Execute ETL pipeline
- Generate reports
- Upload to Azure
- Send email
- Display execution summary

---

## extractor.py

Responsible for extracting raw sales records.

Functions:

- Read CSV file
- Load dataset into Pandas DataFrame
- Handle missing files
- Handle extraction errors

---

## transformer.py

Responsible for cleaning and transforming raw data.

Operations performed:

- Remove duplicate records
- Remove null values
- Convert Date column into datetime format
- Prepare cleaned dataset

---

## loader.py

Responsible for storing transformed data.

Responsibilities:

- Save cleaned CSV
- Create output directory automatically
- Return generated file path

---

## azure_loader.py

Responsible for uploading processed data into Azure SQL Database.

Responsibilities:

- Establish Azure SQL connection
- Upload cleaned dataset
- Handle SQL errors
- Close database connection safely

---

## azure_sql_reader.py

Responsible for reading existing records from Azure SQL Database.

Responsibilities:

- Connect Azure SQL
- Execute SQL query
- Return Pandas DataFrame

---

## blob_storage.py

Responsible for uploading processed CSV file to Azure Blob Storage.

Responsibilities:

- Connect Azure Blob Storage
- Upload cleaned CSV
- Replace existing blob
- Handle authentication failures

---

## viz.py

Responsible for generating graphical reports.

Responsibilities:

- Group sales by product
- Generate bar chart
- Save visualization
- Return chart location

---

## emailer.py

Responsible for automated email reporting.

Responsibilities:

- Load HTML template
- Attach generated chart
- Authenticate using Gmail SMTP
- Send ETL completion report

---

## history.py

Responsible for maintaining pipeline execution history.

Stores:

- Execution source
- Execution time
- Rows processed
- Pipeline status

---

## logger.py

Responsible for project logging.

Logs include:

- Pipeline execution
- Errors
- Warnings
- Azure operations
- Email status

---

## validation.py

Responsible for validating configuration before pipeline execution.

Validation includes:

- Azure SQL configuration
- Azure Blob configuration
- Email configuration
- Local paths
- Required environment variables

---

## utils.py

Contains helper utilities used across the project.

Examples:

- Progress messages
- Success messages
- Common helper functions

---

# Configuration Management

The project uses environment variables stored inside a `.env` file.

Configuration includes:

- Local project paths
- Azure SQL credentials
- Azure Blob Storage credentials
- SMTP credentials
- Feature flags

Using `.env` keeps sensitive credentials outside the source code.

---

# Environment Variables

The following configuration variables are required:

### Local

- CSV_PATH
- CLEANED_CSV_PATH
- REPORT_DIR

### Azure SQL

- AZURE_SQL_SERVER
- AZURE_SQL_DATABASE
- AZURE_SQL_USERNAME
- AZURE_SQL_PASSWORD
- AZURE_SQL_TABLE
- AZURE_SQL_DRIVER

### Azure Blob Storage

- AZURE_STORAGE_CONNECTION_STRING
- AZURE_CONTAINER_NAME
- AZURE_BLOB_NAME

### Email

- SMTP_SERVER
- SMTP_PORT
- SMTP_USER
- SMTP_PASS
- TO_ADDRESS
- EMAIL_SUBJECT

---

# Dataset Description

The project processes sales records containing the following columns:

| Column | Description |
|---------|-------------|
| OrderID | Unique Order Identifier |
| Customer | Customer Name |
| Product | Product Name |
| Quantity | Quantity Sold |
| Price | Product Price |
| Date | Transaction Date |

---

# Data Cleaning Rules

During transformation the following operations are performed:

- Remove duplicate rows
- Remove missing values
- Convert Date column into datetime format
- Prepare clean dataset for storage

This ensures data consistency before loading into databases and Azure services.
# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Azure-ETL-Pipeline.git

cd Azure-ETL-Pipeline
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Configuration

Create a `.env` file inside the project root directory.

The configuration file contains:

- Local Paths
- Azure SQL Credentials
- Azure Blob Storage Credentials
- SMTP Credentials

---

# Running the Pipeline

Execute the complete ETL Pipeline using:

```bash
python run_etl.py
```

The pipeline automatically performs the following operations:

1. Validate configuration
2. Extract data
3. Transform data
4. Save cleaned CSV
5. Update SQLite database
6. Upload data to Azure SQL Database
7. Upload cleaned CSV to Azure Blob Storage
8. Generate sales visualization
9. Generate HTML email report
10. Send email notification
11. Display execution summary

---

# Pipeline Execution Summary

A successful execution displays a summary similar to:

```
Execution Source : CSV

Rows Processed : 10

SQLite Database : Updated

Azure SQL Upload : Uploaded

Azure Blob Upload : Uploaded

Visualization : Generated

Email Status : Sent

Pipeline Status : SUCCESS
```

---

# Logging

The pipeline maintains detailed execution logs.

The log file contains:

- Start time
- Pipeline stages
- Success messages
- Error messages
- Azure operations
- Email status

Log file location:

```
logs/pipeline.log
```

---

# Visualization

The visualization module automatically generates a sales chart.

Output location:

```
reports/sales_chart.png
```

The chart is also attached with the automated email report.

---

# Automated Email Report

After successful pipeline execution:

- HTML report is generated
- Sales chart is attached
- Report is sent automatically using Gmail SMTP

---

# Unit Testing

The project includes automated unit testing using **PyTest**.

The following ETL modules are tested independently:

- Data Extraction
- Data Transformation
- Data Loading
- Sales Visualization

Project Test Structure:

```
tests/

├── conftest.py

├── test_extractor.py

├── test_transformer.py

├── test_loader.py

└── test_viz.py
```

Run all tests using:

```bash
pytest tests -v
```

Successful execution:

```
========================

collected 4 items

tests/test_extractor.py PASSED

tests/test_loader.py PASSED

tests/test_transformer.py PASSED

tests/test_viz.py PASSED

========================

4 passed
```

This validates that the core ETL components are functioning correctly and independently.

---

# Skills Demonstrated

This project demonstrates practical implementation of:

- Python Programming
- ETL Pipeline Development
- Data Cleaning
- Data Transformation
- Pandas
- SQLite
- Azure SQL Database
- Azure Blob Storage
- SMTP Email Automation
- HTML Report Generation
- Data Visualization
- Configuration Management
- Logging
- Error Handling
- Modular Programming
- Cloud Integration
- Unit Testing using PyTest

---

# Future Enhancements

Possible improvements include:

- Azure Data Factory Integration
- Azure Functions Deployment
- Azure Key Vault Integration
- Docker Containerization
- CI/CD using GitHub Actions
- Apache Airflow Scheduling
- Power BI Dashboard Integration
- REST API Support
- Incremental Data Loading
- Data Validation Framework

---

# Author

**Madhuresh Kumar**

Azure ETL Pipeline using Python

End-to-End Data Engineering Project

---

# License

This project is intended for educational and portfolio purposes.



