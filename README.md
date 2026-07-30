# ETL Data Pipeline with Azure SQL, Azure Blob Storage, Azure Data Factory & Email Automation

## Project Overview

This project implements a complete ETL (Extract, Transform, Load) Data Pipeline using Python and Microsoft Azure.

The pipeline performs the following tasks automatically:

- Extracts sales data from a CSV file
- Cleans and transforms the data
- Saves the cleaned data
- Uploads data to Azure SQL Database
- Uploads cleaned CSV to Azure Blob Storage
- Transfers data from Azure Blob Storage to Azure SQL Database using Azure Data Factory
- Generates sales visualization
- Sends an automated email with the sales chart attached.

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Azure SQL Database
- Azure Blob Storage
- Azure Data Factory
- Gmail SMTP
- PyODBC
- Python Dotenv

---

# Project Architecture

```text
               +----------------------+
               |   Sales CSV File     |
               +----------+-----------+
                          |
                          v
                 Extract (extractor.py)
                          |
                          v
             Transform (transformer.py)
          - Remove Duplicates
          - Remove Missing Values
          - Convert Date Format
                          |
                          v
               Save Clean CSV (loader.py)
                          |
              +-----------+-----------+
              |                       |
              v                       v
      Azure SQL Database      Azure Blob Storage
                                      |
                                      |
                                      v
                         Azure Data Factory Pipeline
                          (PL_Blob_To_SQL)
                                      |
                                      v
                           Azure SQL Database
                                      |
                                      v
                         Generate Chart (viz.py)
                                      |
                                      v
                    Send Email Report (emailer.py)
```

---

# Project Structure

```text
ETL_Capstone/

│
├── adf/
│   └── Pipeline JSON Files
│
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
│
├── etl/
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   ├── azure_loader.py
│   ├── azure_sql_reader.py
│   ├── emailer.py
│   └── viz.py
│
├── reports/
│   └── sales_chart.png
│
├── templates/
│   └── email_template.html
│
├── .env
├── requirements.txt
├── README.md
└── run_etl.py
```

---

# ETL Workflow

## Step 1 – Extract

- Read `sales_data.csv`
- Load data into a Pandas DataFrame

---

## Step 2 – Transform

- Remove duplicate records
- Remove missing values
- Convert Date column into datetime format

---

## Step 3 – Load

- Save cleaned CSV
- Upload data into Azure SQL Database
- Upload cleaned CSV into Azure Blob Storage

---

## Step 4 – Visualization

Generate a bar chart showing total sales by product.

Chart location:

```text
reports/sales_chart.png
```

---

## Step 5 – Email Automation

Automatically sends an email after successful ETL execution.

Email contains:

- ETL Success Message
- Sales Chart Attachment

---

## Step 6 – Azure Data Factory Pipeline

An Azure Data Factory pipeline named **PL_Blob_To_SQL** has been created to automate the movement of data from Azure Blob Storage to Azure SQL Database.

Pipeline Components:

- Azure Blob Storage Linked Service
- Azure SQL Database Linked Service
- BlobSalesCSV Dataset
- AzureSqlTable Dataset
- Copy Data Activity

Pipeline Execution:

- Validate
- Publish
- Debug
- Monitor Pipeline Run
- Verify Data in Azure SQL Database

---

# Azure Services Used

## Azure SQL Database

Stores cleaned sales records.

---

## Azure Blob Storage

Stores the cleaned CSV file.

File uploaded:

```
cleaned_sales_data.csv
```

---

## Azure Data Factory

Used for automated data movement.

Pipeline Name:

```
PL_Blob_To_SQL
```

Activity Used:

```
Copy Data Activity
```

Pipeline Status:

- Validate ✔
- Publish ✔
- Debug ✔
- Monitor ✔

---

# Python Packages

- pandas
- matplotlib
- pyodbc
- python-dotenv
- azure-storage-blob
- openpyxl

---

# How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run the ETL Pipeline

```bash
python run_etl.py
```

---

# Output

The project automatically performs:

- ✔ Load CSV
- ✔ Clean Data
- ✔ Save Clean CSV
- ✔ Upload to Azure SQL
- ✔ Upload to Azure Blob Storage
- ✔ Execute Azure Data Factory Pipeline
- ✔ Copy Blob Data to Azure SQL
- ✔ Generate Sales Chart
- ✔ Send Automated Email

---

# Future Enhancements

- Schedule Azure Data Factory pipeline using Triggers
- Integrate Power BI Dashboard
- Add Logging and Monitoring
- Implement Incremental Data Loading
- Secure credentials using Azure Key Vault
- Deploy the project using Azure DevOps CI/CD Pipeline

---

# Author

**Madhuresh Kumar**

ETL Data Pipeline using Python, Azure SQL Database, Azure Blob Storage, Azure Data Factory and Email Automation.