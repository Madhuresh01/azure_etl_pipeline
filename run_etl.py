from etl.extractor import load_sales_data
from etl.transformer import transform_data
from etl.loader import save_data
from etl.viz import plot_sales
from etl.azure_loader import upload_to_azure
from etl.blob_storage import upload_to_blob
from etl.emailer import send_email


def main():

    file_path = "data/sales_data.csv"

    data = load_sales_data(file_path)

    if data is not None:

        data = transform_data(data)

        save_data(data)

        upload_to_azure(data)

        upload_to_blob()

        plot_sales(data)

        send_email()

        print("\nFirst 5 rows:")
        print(data.head())

        print("\nETL Pipeline completed successfully.")


if __name__ == "__main__":
    main()