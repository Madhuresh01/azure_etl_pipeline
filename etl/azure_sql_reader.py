import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("AZURE_SQL_SERVER")
DATABASE = os.getenv("AZURE_SQL_DATABASE")
USERNAME = os.getenv("AZURE_SQL_USERNAME")
PASSWORD = os.getenv("AZURE_SQL_PASSWORD")

TABLE_NAME = os.getenv("AZURE_SQL_TABLE")
DRIVER = os.getenv("AZURE_SQL_DRIVER")


def read_from_azure():
    """Read data from Azure SQL Database."""

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

    query = f"SELECT * FROM {TABLE_NAME}"
    df = pd.read_sql(query, conn)

    conn.close()

    return df


if __name__ == "__main__":
    data = read_from_azure()
    print(data.head())