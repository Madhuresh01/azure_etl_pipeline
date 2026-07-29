import pandas as pd

def transform_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df