# ETL Capstone Project Documentation

## Project Title

ETL Data Pipeline using Python, Azure SQL, Azure Blob Storage & Email Automation

---

# Project Objective

The objective of this project is to build a complete ETL (Extract, Transform, Load) Data Pipeline that automatically extracts sales data, cleans and transforms it, stores it in Azure SQL Database, uploads the cleaned file to Azure Blob Storage, generates a sales visualization, and sends an automated email report.

---

# Project Workflow

The project follows the ETL architecture.

Sales CSV
↓

Extract Data

↓

Transform Data

↓

Save Clean CSV

↓

Upload to Azure SQL

↓

Upload to Azure Blob Storage

↓

Generate Sales Chart

↓

Send Email Report

---

# Modules Description

## extractor.py

Responsibilities:

- Read sales_data.csv
- Load data into Pandas DataFrame

Output:

- Raw DataFrame

---

## transformer.py

Responsibilities:

- Remove duplicate rows
- Remove missing values
- Convert Date column into datetime

Output:

- Clean DataFrame

---

## loader.py

Responsibilities:

- Save cleaned dataframe into CSV

Output:

- cleaned_sales_data.csv

---

## azure_loader.py

Responsibilities:

- Connect Azure SQL Database
- Create SalesData table (if not exists)
- Upload cleaned records

Output:

- Azure SQL Database updated

---

## azure_sql_reader.py

Responsibilities:

- Read uploaded records from Azure SQL

Output:

- Display first few records

---

## blob_storage.py (Azure Blob Upload)

Responsibilities:

- Upload cleaned CSV
- Store file inside Azure Blob Storage Container

Output:

- cleaned_sales_data.csv uploaded successfully

---

## viz.py

Responsibilities:

- Group sales by Product
- Generate Bar Chart
- Save chart inside reports folder

Output:

reports/sales_chart.png

---

## emailer.py

Responsibilities:

- Load HTML Email Template
- Attach Sales Chart
- Send Email automatically using Gmail SMTP

Output:

- Email delivered successfully

---

# Azure Services Used

## Azure SQL Database

Purpose:

Store transformed sales records.

Features Used:

- SQL Tables
- ODBC Driver
- Cloud Database

---

## Azure Blob Storage

Purpose:

Store cleaned CSV file in cloud storage.

Container:

input

Stored File:

cleaned_sales_data.csv

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- PyODBC
- Azure SQL Database
- Azure Blob Storage
- Gmail SMTP
- Jinja2
- Dotenv

---

# Project Folder Structure

```
ETL_Capstone/

├── data/
├── etl/
├── reports/
├── templates/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── CAPSTONE_PROJECT.md
└── run_etl.py
```

---

# Project Features

✔ ETL Architecture

✔ Data Cleaning

✔ Azure SQL Integration

✔ Azure Blob Storage Upload

✔ Sales Visualization

✔ Email Automation

✔ Modular Python Code

✔ Environment Variables

✔ GitHub Ready Structure

---

# Output

The pipeline performs the following automatically:

- Load CSV
- Clean Data
- Save Clean CSV
- Upload to Azure SQL
- Upload to Azure Blob Storage
- Generate Sales Chart
- Send Email Report

---

# Future Improvements

- Schedule pipeline using Azure Data Factory
- Store logs in Azure Monitor
- Add Power BI Dashboard
- Dockerize the application
- CI/CD using GitHub Actions

---

# Author

**Madhuresh Kumar**

Python ETL Capstone Project