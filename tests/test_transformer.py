import pandas as pd

from etl.transformer import transform_data


def test_transform_data():

    data = {
        "OrderID": [1, 1, 2],
        "Customer": ["A", "A", "B"],
        "Product": ["Laptop", "Laptop", "Mouse"],
        "Quantity": [1, 1, 2],
        "Price": [50000, 50000, 1000],
        "Date": ["2025-01-01", "2025-01-01", "2025-01-02"],
    }

    df = pd.DataFrame(data)

    cleaned = transform_data(df)

    assert len(cleaned) == 2

    assert pd.api.types.is_datetime64_any_dtype(cleaned["Date"])