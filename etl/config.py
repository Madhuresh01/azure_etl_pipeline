"""
config.py

Centralized configuration module for the Azure ETL Pipeline.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()


class Config:
    """
    Central configuration class.
    """

    def __init__(self):

        # ==================================================
        # LOCAL PROJECT PATHS
        # ==================================================

        self.project_root = Path.cwd()

        self.csv_path = os.getenv("CSV_PATH")

        self.report_dir = os.getenv(
            "REPORT_DIR",
            "reports",
        )

        self.cleaned_csv = os.getenv(
            "CLEANED_CSV_PATH",
            "data/cleaned_sales_data.csv",
        )

        self.db_path = os.getenv(
            "DB_PATH",
            "data/pipeline_history.db",
        )

        self.table_name = os.getenv(
            "TABLE_NAME",
            "SalesData",
        )

        # ==================================================
        # AZURE SQL CONFIGURATION
        # ==================================================

        self.read_from_azure_sql = (
            os.getenv(
                "READ_FROM_AZURE_SQL",
                "false",
            ).lower()
            == "true"
        )

        self.azure_sql_server = os.getenv(
            "AZURE_SQL_SERVER"
        )

        self.azure_sql_database = os.getenv(
            "AZURE_SQL_DATABASE"
        )

        self.azure_sql_username = os.getenv(
            "AZURE_SQL_USERNAME"
        )

        self.azure_sql_password = os.getenv(
            "AZURE_SQL_PASSWORD"
        )

        self.azure_sql_table = os.getenv(
            "AZURE_SQL_TABLE"
        )

        self.azure_sql_driver = os.getenv(
            "AZURE_SQL_DRIVER"
        )

        # ==================================================
        # AZURE BLOB STORAGE
        # ==================================================

        self.upload_to_azure = (
            os.getenv(
                "UPLOAD_TO_AZURE",
                "false",
            ).lower()
            == "true"
        )

        self.azure_connection_string = os.getenv(
            "AZURE_STORAGE_CONNECTION_STRING"
        )

        self.azure_container = os.getenv(
            "AZURE_CONTAINER_NAME"
        )

        self.azure_blob = os.getenv(
            "AZURE_BLOB_NAME"
        )

        # ==================================================
        # EMAIL CONFIGURATION
        # ==================================================

        self.send_email = (
            os.getenv(
                "SEND_EMAIL",
                "false",
            ).lower()
            == "true"
        )

        self.smtp_server = os.getenv(
            "SMTP_SERVER"
        )

        self.smtp_port = int(
            os.getenv(
                "SMTP_PORT",
                587,
            )
        )

        self.smtp_user = os.getenv(
            "SMTP_USER"
        )

        self.smtp_pass = os.getenv(
            "SMTP_PASS"
        )

        self.to_address = os.getenv(
            "TO_ADDRESS"
        )

        self.email_subject = os.getenv(
            "EMAIL_SUBJECT",
            "Azure ETL Pipeline Report",
        )

        # ==================================================
        # PIPELINE OPTIONS
        # ==================================================

        self.retry_count = int(
            os.getenv(
                "RETRY_COUNT",
                3,
            )
        )

        self.retry_delay = int(
            os.getenv(
                "RETRY_DELAY",
                5,
            )
        )


# ==========================================================
# GLOBAL CONFIG OBJECT
# ==========================================================

config = Config()