import pandas as pd


def load_sales_data(csv_path):
    """
    Load sales CSV file into a Pandas DataFrame.
    """

    try:

        dataframe = pd.read_csv(csv_path)

        print(f"{len(dataframe)} records loaded successfully.")

        return dataframe

    except FileNotFoundError:

        print("CSV file not found.")

        raise

    except Exception as error:

        print("Data extraction failed.")

        raise error