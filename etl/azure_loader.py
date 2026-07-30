import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Azure SQL Configuration
# ==========================
SERVER = os.getenv("AZURE_SQL_SERVER")
DATABASE = os.getenv("AZURE_SQL_DATABASE")
USERNAME = os.getenv("AZURE_SQL_USERNAME")
PASSWORD = os.getenv("AZURE_SQL_PASSWORD")

TABLE_NAME = os.getenv("AZURE_SQL_TABLE")
DRIVER = os.getenv("AZURE_SQL_DRIVER")


def upload_to_azure(df):
    """
    Upload cleaned DataFrame to Azure SQL Database.
    """

    conn_str = (
        f"DRIVER={{{DRIVER}}};"
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

    # Create table if it doesn't exist
    cursor.execute(f"""
    IF OBJECT_ID('{TABLE_NAME}', 'U') IS NULL
    CREATE TABLE {TABLE_NAME} (
        OrderID INT,
        Customer NVARCHAR(100),
        Product NVARCHAR(100),
        Quantity INT,
        Price FLOAT,
        Date DATE
    )
    """)
    conn.commit()

    # Clear previous data
    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    conn.commit()

    # Insert cleaned records
    insert_query = f"""
    INSERT INTO {TABLE_NAME}
    (
        OrderID,
        Customer,
        Product,
        Quantity,
        Price,
        Date
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """

    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            int(row["OrderID"]),
            row["Customer"],
            row["Product"],
            int(row["Quantity"]),
            float(row["Price"]),
            str(row["Date"])
        )

    conn.commit()
    conn.close()

    print(f"✅ Data uploaded to Azure SQL table '{TABLE_NAME}' successfully!")