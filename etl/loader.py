import os
import pandas as pd


def save_data(dataframe, table_name, db_path):
    output_folder = os.path.dirname(db_path)
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(
        output_folder,
        "cleaned_sales_data.csv"
    )

    dataframe.to_csv(
        output_file,
        index=False,
    )

    print("Cleaned CSV saved successfully.")

    return output_file


def load(dataframe, table_name, db_path):
    return save_data(dataframe, table_name, db_path)