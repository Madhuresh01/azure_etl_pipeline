# 🚀 Azure ETL Pipeline using Python & Microsoft Azure

An End-to-End ETL (Extract, Transform, Load) Pipeline built using Python and Microsoft Azure services.

The pipeline extracts sales data from a CSV file, performs data cleaning and transformation, loads the processed data into Azure SQL Database and Azure Blob Storage, generates a sales visualization, and automatically sends an email report.

---

# 📌 Project Architecture

![Architecture](assets/architecture.png)

---

# 🛠 Tech Stack

- Python
- Pandas
- Azure SQL Database
- Azure Blob Storage
- Azure Data Factory
- PyODBC
- Azure Storage SDK
- Matplotlib
- SMTP (Gmail)
- Git & GitHub

---

# 📂 Project Structure

```text
ETL_CAPSTONE/
│
├── adf/
├── assets/
│   ├── architecture.png
│   ├── azure_sql.jpeg
│   ├── azure_blob.jpeg
│   ├── email_report.jpeg
│   └── sales_chart.png
│
├── data/
├── etl/
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   ├── azure_loader.py
│   ├── blob_storage.py
│   ├── azure_sql_reader.py
│   ├── emailer.py
│   └── viz.py
│
├── reports/
├── templates/
├── run_etl.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙ ETL Workflow

```text
CSV File
    │
    ▼
Extract
    │
    ▼
Transform
    │
    ▼
Save Cleaned CSV
    │
    ├────────► Azure SQL Database
    │
    ├────────► Azure Blob Storage
    │
    ▼
Generate Sales Chart
    │
    ▼
Send Email Report
```

---

# ✨ Features

- Extract sales data from CSV
- Data cleaning & transformation using Pandas
- Upload processed data to Azure SQL Database
- Store cleaned CSV in Azure Blob Storage
- Generate sales visualization using Matplotlib
- Send automated HTML Email Report
- Environment Variable Support (.env)
- Modular ETL Architecture

---

# ▶️ Run Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python run_etl.py
```

---

# 📊 Project Output

## Azure SQL Database

![Azure SQL](assets/azure_sql.jpeg)

---

## Azure Blob Storage

![Azure Blob](assets/azure_blob.jpeg)

---

## Sales Chart

![Sales Chart](assets/sales_chart.png)

---

## Email Report

![Email Report](assets/email_report.jpeg)

---

# 👨‍💻 Author

**Madhuresh Kumar**