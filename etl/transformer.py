import pandas as pd


def transform_data(df):
    """
    Clean and transform the sales dataset.
    """

    before = len(df)

    df = df.drop_duplicates()

    df = df.dropna()

    df["Date"] = pd.to_datetime(df["Date"])

    after = len(df)

    print(f"Records before cleaning : {before}")

    print(f"Records after cleaning  : {after}")

    return df