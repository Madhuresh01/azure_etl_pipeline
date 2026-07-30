import os
import pandas as pd

from etl.viz import plot_sales


def test_plot_sales():

    df = pd.DataFrame(
        {
            "Product": ["Laptop", "Mouse"],
            "Price": [50000, 3000],
        }
    )

    chart_path = plot_sales(df)

    assert os.path.exists(chart_path)