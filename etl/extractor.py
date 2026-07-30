import pandas as pd


def load_sales_data(csv_path):
    """Load sales data from a CSV file."""

    try:
        data = pd.read_csv(csv_path)
        print("CSV loaded successfully.")
        return data

    except FileNotFoundError:
        print("CSV file not found.")
        return None

    except Exception as error:
        print(f"Error: {error}")
        return None