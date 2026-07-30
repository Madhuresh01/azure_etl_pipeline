"""
history.py

Store ETL pipeline execution history in SQLite.
"""

import sqlite3
from datetime import datetime

from etl.logger import logger


class PipelineHistory:
    """
    Manage pipeline execution history.
    """

    def __init__(self, db_path):

        self.db_path = db_path

        self.create_table()

    # ======================================================
    # CREATE TABLE
    # ======================================================

    def create_table(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pipeline_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                execution_date TEXT,

                source TEXT,

                rows_processed INTEGER,

                execution_time REAL,

                blob_uploaded INTEGER,

                email_sent INTEGER,

                status TEXT

            )
            """
        )

        conn.commit()

        conn.close()

        logger.info(
            "Pipeline history table verified."
        )

    # ======================================================
    # SAVE EXECUTION
    # ======================================================

    def save_execution(
        self,
        source,
        rows_processed,
        execution_time,
        blob_uploaded,
        email_sent,
        status,
    ):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO pipeline_history (

                execution_date,

                source,

                rows_processed,

                execution_time,

                blob_uploaded,

                email_sent,

                status

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                source,
                rows_processed,
                execution_time,
                int(blob_uploaded),
                int(email_sent),
                status,
            ),
        )

        conn.commit()

        conn.close()

        logger.info(
            "Pipeline execution saved successfully."
        )

    # ======================================================
    # GET COMPLETE HISTORY
    # ======================================================

    def get_history(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *

            FROM pipeline_history

            ORDER BY id DESC
            """
        )

        history = cursor.fetchall()

        conn.close()

        return history

    # ======================================================
    # GET LAST EXECUTION
    # ======================================================

    def latest_execution(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *

            FROM pipeline_history

            ORDER BY id DESC

            LIMIT 1
            """
        )

        latest = cursor.fetchone()

        conn.close()

        return latest

    # ======================================================
    # TOTAL EXECUTIONS
    # ======================================================

    def total_runs(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM pipeline_history
            """
        )

        total = cursor.fetchone()[0]

        conn.close()

        return total