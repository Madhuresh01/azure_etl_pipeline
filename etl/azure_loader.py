"""
azure_loader.py

Upload cleaned sales data to Azure SQL Database.
"""

import os
import pyodbc

from dotenv import load_dotenv

from etl.logger import logger
from etl.utils import progress, completed

load_dotenv()

# ==========================================================
# AZURE SQL CONFIGURATION
# ==========================================================

SERVER = os.getenv("AZURE_SQL_SERVER")

DATABASE = os.getenv("AZURE_SQL_DATABASE")

USERNAME = os.getenv("AZURE_SQL_USERNAME")

PASSWORD = os.getenv("AZURE_SQL_PASSWORD")

TABLE_NAME = os.getenv("AZURE_SQL_TABLE")

DRIVER = os.getenv("AZURE_SQL_DRIVER")


# ==========================================================
# AZURE SQL UPLOAD
# ==========================================================

def upload_to_azure(df):
    """
    Upload cleaned dataframe into Azure SQL Database.
    """

    progress("Connecting to Azure SQL Database...")

    logger.info("Starting Azure SQL upload.")

    connection_string = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    connection = None

    try:

        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()

        logger.info("Azure SQL connection established.")

        # --------------------------------------------------
        # CREATE TABLE
        # --------------------------------------------------

        create_table_query = f"""
        IF OBJECT_ID('{TABLE_NAME}', 'U') IS NULL

        CREATE TABLE {TABLE_NAME}
        (
            OrderID INT,
            Customer NVARCHAR(100),
            Product NVARCHAR(100),
            Quantity INT,
            Price FLOAT,
            Date DATE
        )
        """

        cursor.execute(create_table_query)

        connection.commit()

        logger.info("Verified target table.")

        # --------------------------------------------------
        # CLEAR OLD DATA
        # --------------------------------------------------

        cursor.execute(
            f"DELETE FROM {TABLE_NAME}"
        )

        connection.commit()

        logger.info("Old records removed.")

        # --------------------------------------------------
        # INSERT DATA
        # --------------------------------------------------

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

        records = []

        for _, row in df.iterrows():

            records.append(
                (
                    int(row["OrderID"]),
                    row["Customer"],
                    row["Product"],
                    int(row["Quantity"]),
                    float(row["Price"]),
                    str(row["Date"]),
                )
            )

        cursor.executemany(
            insert_query,
            records,
        )

        connection.commit()

        completed(
            f"{len(records)} records uploaded successfully."
        )

        logger.info(
            "%d records uploaded successfully.",
            len(records),
        )

    except Exception as error:

        logger.exception(error)

        print("Azure SQL upload failed.")

        raise

    finally:

        if connection:

            connection.close()

            logger.info("Azure SQL connection closed.")