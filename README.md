# 🚀 Azure ETL Pipeline Project

A complete End-to-End ETL Pipeline built using Python and Microsoft Azure.

## 📌 Project Overview

This project extracts sales data from a CSV file, cleans and transforms it using Pandas, uploads it to Azure SQL Database, stores the cleaned CSV in Azure Blob Storage, generates a sales visualization, and emails the final report automatically.

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

```
ETL_CAPSTONE/
│
├── adf/
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

```
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
    ├────────────► Azure SQL
    │
    ├────────────► Azure Blob Storage
    │
    ▼
Generate Chart
    │
    ▼
Send Email
```

---

# ✨ Features

- Extract CSV data
- Clean and transform records
- Save cleaned dataset
- Upload to Azure SQL Database
- Upload CSV to Azure Blob Storage
- Generate Sales Chart
- Send HTML Email Report
- Environment Variable Support (.env)
- Modular ETL Architecture

---

# ▶️ Run Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run ETL

```bash
python run_etl.py
```

---

# 📊 Output

- Cleaned CSV
- Azure SQL Table
- Azure Blob Storage
- Sales Chart
- Email Report

---

# 👨‍💻 Author

Madhuresh Kumar