import pandas as pd


def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["Date"] = pd.to_datetime(df["Date"])

    return df