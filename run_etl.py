from etl.extractor import load_sales_data
from etl.transformer import transform_data
from etl.loader import save_data
from etl.viz import plot_sales
from etl.azure_loader import upload_to_azure


def main():
    file_path = "data/sales_data.csv"

    # Extract
    data = load_sales_data(file_path)

    if data is not None:

        # Transform
        data = transform_data(data)

        # Save cleaned CSV
        save_data(data)

        # Upload to Azure SQL
        upload_to_azure(data)

        # Visualization
        plot_sales(data)

        # Preview
        print("\nFirst 5 rows:")
        print(data.head())


if __name__ == "__main__":
    main()