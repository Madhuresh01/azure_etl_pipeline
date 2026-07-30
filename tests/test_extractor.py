import pandas as pd

from etl.extractor import load_sales_data


def test_load_sales_data():

    df = load_sales_data("data/sales_data.csv")

    assert isinstance(df, pd.DataFrame)

    assert len(df) > 0

    assert "OrderID" in df.columns