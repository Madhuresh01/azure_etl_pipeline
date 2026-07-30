import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")
BLOB_NAME = os.getenv("AZURE_BLOB_NAME")
LOCAL_FILE_PATH = os.getenv("CLEANED_CSV_PATH")


def upload_to_blob():
    """Upload cleaned CSV file to Azure Blob Storage."""

    if not CONNECTION_STRING:
        print("Azure Storage Connection String is missing.")
        return

    if not os.path.exists(LOCAL_FILE_PATH):
        print(f"File not found: {LOCAL_FILE_PATH}")
        return

    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            CONNECTION_STRING
        )

        container_client = blob_service_client.get_container_client(
            CONTAINER_NAME
        )

        blob_client = container_client.get_blob_client(BLOB_NAME)

        with open(LOCAL_FILE_PATH, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(
            f"'{LOCAL_FILE_PATH}' uploaded successfully "
            f"to container '{CONTAINER_NAME}' "
            f"as '{BLOB_NAME}'."
        )

    except Exception as e:
        print("Azure Blob upload failed.")
        print(e)