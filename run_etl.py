"""
run_etl.py

Production Ready Azure ETL Pipeline

Author : Madhuresh Kumar
Project : Azure ETL Pipeline
"""

import time
import traceback
from datetime import datetime

from etl.extractor import load_sales_data
from etl.transformer import transform_data
from etl.loader import load
from etl.azure_loader import upload_to_azure
from etl.blob_storage import upload_to_blob
from etl.viz import plot_sales
from etl.emailer import send_email

from etl.config import config

from etl.logger import (
    logger,
    banner,
    stage,
    success,
    warning,
    error,
)

from etl.utils import (
    retry,
    progress,
    completed,
)

from etl.history import PipelineHistory


# ==========================================================
# GLOBAL VARIABLES
# ==========================================================

pipeline = PipelineHistory(config.db_path)

execution_source = "Unknown"

rows_processed = 0

blob_status = "Skipped"

email_status = "Skipped"


# ==========================================================
# CONFIGURATION VALIDATION
# ==========================================================

def validate_configuration():

    stage("STEP 1 : CONFIGURATION")

    progress("Validating configuration...")

    required = {
        "CSV_PATH": config.csv_path,
        "REPORT_DIR": config.report_dir,
    }

    if config.read_from_azure_sql:

        required.update(
            {
                "AZURE_SQL_SERVER": config.azure_sql_server,
                "AZURE_SQL_DATABASE": config.azure_sql_database,
                "AZURE_SQL_USERNAME": config.azure_sql_username,
                "AZURE_SQL_PASSWORD": config.azure_sql_password,
                "AZURE_SQL_TABLE": config.azure_sql_table,
            }
        )

    if config.upload_to_azure:

        required.update(
            {
                "AZURE_STORAGE_CONNECTION_STRING":
                    config.azure_connection_string,

                "AZURE_CONTAINER_NAME":
                    config.azure_container,

                "AZURE_BLOB_NAME":
                    config.azure_blob,
            }
        )

    if config.send_email:

        required.update(
            {
                "SMTP_USER": config.smtp_user,
                "SMTP_PASS": config.smtp_pass,
                "TO_ADDRESS": config.to_address,
            }
        )

    missing = []

    for key, value in required.items():

        if value is None or value == "":

            missing.append(key)

    if missing:

        error("Configuration validation failed.")

        for item in missing:

            error(item)

        raise ValueError(
            "Missing configuration values."
        )

    success("Configuration validated successfully.")


# ==========================================================
# DATA EXTRACTION
# ==========================================================

def extract_data():

    global execution_source

    stage("STEP 2 : DATA EXTRACTION")

    progress("Loading sales data...")

    data = load_sales_data(config.csv_path)

    execution_source = "CSV"

    completed(
        f"{len(data)} records loaded successfully."
    )

    logger.info(
        "Loaded %d records.",
        len(data),
    )

    return data


# ==========================================================
# DATA TRANSFORMATION
# ==========================================================

def clean_data(df):

    global rows_processed

    stage("STEP 3 : DATA TRANSFORMATION")

    progress("Cleaning dataset...")

    df = transform_data(df)

    rows_processed = len(df)

    completed(
        f"{rows_processed} records ready."
    )

    logger.info(
        "Transformation completed successfully."
    )

    return df

# ==========================================================
# SAVE CLEAN CSV
# ==========================================================

def save_cleaned_data(df):

    stage("STEP 4 : SAVE CLEAN CSV")

    progress("Saving cleaned CSV...")

    output_file = load(
        dataframe=df,
        table_name=config.table_name,
        db_path=config.db_path,
    )

    completed("Cleaned CSV saved successfully.")

    logger.info(
        "Cleaned CSV saved at %s",
        output_file,
    )

    return output_file


# ==========================================================
# AZURE SQL DATABASE
# ==========================================================

def upload_sql(df):

    stage("STEP 5 : AZURE SQL DATABASE")

    progress("Uploading records to Azure SQL...")

    upload_to_azure(df)

    completed("Azure SQL upload completed.")

    logger.info(
        "Azure SQL upload completed."
    )


# ==========================================================
# AZURE BLOB STORAGE
# ==========================================================

def upload_blob_storage():

    global blob_status

    stage("STEP 6 : AZURE BLOB STORAGE")

    if not config.upload_to_azure:

        blob_status = "Skipped"

        warning("Azure Blob upload disabled.")

        return

    progress("Uploading cleaned CSV to Azure Blob Storage...")

    upload_to_blob()

    blob_status = "Uploaded"

    completed("Azure Blob upload completed.")

    logger.info(
        "Azure Blob upload successful."
    )


# ==========================================================
# SALES VISUALIZATION
# ==========================================================

def generate_chart(df):

    stage("STEP 7 : SALES VISUALIZATION")

    progress("Generating sales chart...")

    chart_path = plot_sales(df)

    completed("Sales chart generated.")

    logger.info(
        "Chart generated at %s",
        chart_path,
    )

    return chart_path


# ==========================================================
# EMAIL NOTIFICATION
# ==========================================================

def email_report():

    global email_status

    stage("STEP 8 : EMAIL NOTIFICATION")

    if not config.send_email:

        email_status = "Skipped"

        warning("Email notification disabled.")

        return

    progress("Sending email report...")

    send_email()

    email_status = "Sent"

    completed("Email sent successfully.")

    logger.info(
        "Email notification completed."
    )

  # ==========================================================
# PIPELINE SUMMARY
# ==========================================================

def pipeline_summary(execution_time):

    stage("PIPELINE SUMMARY")

    print()

    print("=" * 70)

    print(f"Execution Date      : {datetime.now()}")

    print(f"Execution Source    : {execution_source}")

    print(f"Rows Processed      : {rows_processed}")

    print("SQLite Database     : Updated")

    print(f"Azure Blob Upload   : {blob_status}")

    print(f"Email Status        : {email_status}")

    print(f"Execution Time      : {execution_time:.2f} sec")

    print("Pipeline Status     : SUCCESS")

    print("=" * 70)

    logger.info("=" * 70)

    logger.info("Pipeline Summary")

    logger.info("Source : %s", execution_source)

    logger.info("Rows : %d", rows_processed)

    logger.info("Blob : %s", blob_status)

    logger.info("Email : %s", email_status)

    logger.info("Execution Time : %.2f", execution_time)

    logger.info("=" * 70)


# ==========================================================
# SAVE PIPELINE HISTORY
# ==========================================================

def save_pipeline_history(execution_time, status):

    pipeline.save_execution(
        source=execution_source,
        rows_processed=rows_processed,
        execution_time=execution_time,
        blob_uploaded=(blob_status == "Uploaded"),
        email_sent=(email_status == "Sent"),
        status=status,
    )

    logger.info("Pipeline history saved.")

      # ==========================================================
# MAIN ETL PIPELINE
# ==========================================================

def main():

    banner()

    logger.info("=" * 70)
    logger.info("Azure ETL Pipeline Started")
    logger.info("=" * 70)

    start_time = time.time()

    try:

        # Step 1
        validate_configuration()

        # Step 2
        data = extract_data()

        # Step 3
        data = clean_data(data)

        # Step 4
        cleaned_csv = save_cleaned_data(data)

        # Step 5
        upload_sql(data)

        # Step 6
        upload_blob_storage()

        # Step 7
        chart_path = generate_chart(data)

        # Step 8
        email_report()

        execution_time = time.time() - start_time

        save_pipeline_history(
            execution_time=execution_time,
            status="SUCCESS",
        )

        pipeline_summary(execution_time)

        success("ETL Pipeline completed successfully.")

        logger.info("Pipeline execution completed.")

    except KeyboardInterrupt:

        execution_time = time.time() - start_time

        warning("Pipeline interrupted by user.")

        save_pipeline_history(
            execution_time=execution_time,
            status="CANCELLED",
        )

        logger.warning("Pipeline cancelled by user.")

    except Exception as err:

        execution_time = time.time() - start_time

        error("ETL Pipeline failed.")

        logger.exception(err)

        save_pipeline_history(
            execution_time=execution_time,
            status="FAILED",
        )

        print()

        print("=" * 70)
        print("PIPELINE STATUS : FAILED")
        print("=" * 70)

        print(traceback.format_exc())

        raise


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except Exception:

        print()

        print("=" * 70)

        print(
            "The pipeline terminated because of an unrecoverable error."
        )

        print(
            "Please check the log file for more details."
        )

        print("=" * 70)

        raise