import os
import pandas as pd

from etl.loader import save_data


def test_save_data():
    df = pd.DataFrame(
        {
            "OrderID": [1],
            "Customer": ["A"],
            "Product": ["Laptop"],
            "Quantity": [1],
            "Price": [50000],
            "Date": ["2025-01-01"],
        }
    )

    output = save_data(
        df,
        "SalesData",
        "data/pipeline_history.db",
    )

    assert os.path.exists(output)