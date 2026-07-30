# ETL Capstone Project Documentation

## Project Title

ETL Data Pipeline using Python, Azure SQL, Azure Blob Storage and Email Automation

---

# Project Overview

This project demonstrates an end-to-end ETL pipeline built using Python and Microsoft Azure services.

The pipeline extracts sales data from a CSV file, cleans and transforms it, stores the processed data in Azure SQL Database, uploads the cleaned CSV to Azure Blob Storage, generates a sales chart, and sends an email report automatically.

---

# Project Workflow

```text
Sales CSV
    │
    ▼
Extract Data
    │
    ▼
Transform Data
    │
    ▼
Save Clean CSV
    │
    ├──► Azure SQL Database
    │
    ├──► Azure Blob Storage
    │
    ▼
Generate Sales Chart
    │
    ▼
Send Email Report
```

---

# Project Modules

## extractor.py

Functions:

- Read the sales CSV file
- Load the data into a Pandas DataFrame

Output:

- Raw DataFrame

---

## transformer.py

Functions:

- Remove duplicate records
- Remove rows with missing values
- Convert the Date column to datetime format

Output:

- Cleaned DataFrame

---

## loader.py

Functions:

- Save the cleaned DataFrame as a CSV file

Output:

- cleaned_sales_data.csv

---

## azure_loader.py

Functions:

- Connect to Azure SQL Database
- Create the SalesData table if it does not exist
- Upload cleaned records

Output:

- Data stored in Azure SQL Database

---

## azure_sql_reader.py

Functions:

- Read uploaded records from Azure SQL Database
- Display sample records

---

## blob_storage.py

Functions:

- Upload cleaned CSV file to Azure Blob Storage

Output:

- cleaned_sales_data.csv uploaded successfully

---

## viz.py

Functions:

- Group sales by product
- Generate a bar chart
- Save the chart inside the reports folder

Output:

reports/sales_chart.png

---

## emailer.py

Functions:

- Create an HTML email
- Attach the generated sales chart
- Send the report using Gmail SMTP

---

# Azure Services Used

## Azure SQL Database

Purpose:

Store transformed sales records.

Features:

- SQL Tables
- ODBC Driver
- Cloud Database

---

## Azure Blob Storage

Purpose:

Store the cleaned CSV file.

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
- python-dotenv

---

# Project Structure

```text
ETL_Capstone/

├── assets/
├── data/
├── etl/
├── reports/
├── templates/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── CAPSTONE_PROJECT.md
└── run_etl.py
```

---

# Features

- End-to-end ETL pipeline
- Data cleaning and transformation
- Azure SQL integration
- Azure Blob Storage upload
- Sales visualization
- Email automation
- Modular project structure
- Environment variable support

---

# Output

The pipeline performs the following tasks:

- Read the input CSV
- Clean and transform the data
- Save the cleaned CSV
- Upload data to Azure SQL Database
- Upload the CSV to Azure Blob Storage
- Generate a sales chart
- Send an email report

---

# Future Improvements

- Schedule the pipeline using Azure Data Factory
- Store logs for monitoring
- Add a Power BI dashboard
- Dockerize the application
- Implement CI/CD using GitHub Actions

---

# Author

**Madhuresh Kumar**