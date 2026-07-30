"""
blob_storage.py

Upload cleaned CSV file to Azure Blob Storage.
"""

import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

from etl.logger import logger
from etl.utils import progress, completed

load_dotenv()

# ==========================================================
# AZURE BLOB CONFIGURATION
# ==========================================================

CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

CONTAINER_NAME = os.getenv(
    "AZURE_CONTAINER_NAME"
)

BLOB_NAME = os.getenv(
    "AZURE_BLOB_NAME"
)

LOCAL_FILE_PATH = os.getenv(
    "CLEANED_CSV_PATH"
)


# ==========================================================
# UPLOAD CSV TO AZURE BLOB STORAGE
# ==========================================================

def upload_to_blob():
    """
    Upload cleaned CSV file to Azure Blob Storage.
    """

    progress("Connecting to Azure Blob Storage...")

    logger.info("Starting Azure Blob upload.")

    if not CONNECTION_STRING:

        raise ValueError(
            "Azure Storage Connection String not found."
        )

    if not os.path.exists(LOCAL_FILE_PATH):

        raise FileNotFoundError(
            f"File not found : {LOCAL_FILE_PATH}"
        )

    try:

        blob_service_client = (
            BlobServiceClient.from_connection_string(
                CONNECTION_STRING
            )
        )

        logger.info(
            "Connected to Azure Blob Storage."
        )

        container_client = (
            blob_service_client.get_container_client(
                CONTAINER_NAME
            )
        )

        blob_client = (
            container_client.get_blob_client(
                BLOB_NAME
            )
        )

        with open(
            LOCAL_FILE_PATH,
            "rb",
        ) as file:

            blob_client.upload_blob(
                file,
                overwrite=True,
            )

        completed(
            f"CSV uploaded successfully to '{CONTAINER_NAME}'."
        )

        logger.info(
            "Blob upload completed successfully."
        )

    except Exception as error:

        logger.exception(error)

        print("Azure Blob upload failed.")

        raise