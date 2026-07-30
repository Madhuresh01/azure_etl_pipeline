import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("AZURE_SQL_SERVER")
DATABASE = os.getenv("AZURE_SQL_DATABASE")
USERNAME = os.getenv("AZURE_SQL_USERNAME")
PASSWORD = os.getenv("AZURE_SQL_PASSWORD")


def upload_to_azure(df):
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""
    IF OBJECT_ID('SalesData', 'U') IS NULL
    CREATE TABLE SalesData (
        OrderID INT,
        Customer NVARCHAR(100),
        Product NVARCHAR(100),
        Quantity INT,
        Price FLOAT,
        Date DATE
    )
    """)
    conn.commit()

    cursor.execute("DELETE FROM SalesData")
    conn.commit()

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO SalesData
        (OrderID, Customer, Product, Quantity, Price, Date)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        int(row["OrderID"]),
        row["Customer"],
        row["Product"],
        int(row["Quantity"]),
        float(row["Price"]),
        str(row["Date"])
        )

    conn.commit()
    conn.close()

    print("✅ Data uploaded to Azure SQL successfully!")