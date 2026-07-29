import pandas as pd

def save_data(df, output_file="data/cleaned_sales_data.csv"):
    """
    Save the transformed dataframe to a CSV file.
    """
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")