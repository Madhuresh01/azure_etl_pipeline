import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Output File Configuration
# ==========================================

OUTPUT_FILE = os.getenv("CLEANED_CSV_PATH")


def save_data(df):
    """
    Save the transformed dataframe to a CSV file.
    """

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Cleaned data saved to {OUTPUT_FILE}")