"""
viz.py

Generate sales visualization for the Azure ETL Pipeline.
"""

import os

import matplotlib.pyplot as plt

from etl.logger import logger
from etl.utils import progress, completed


# ==========================================================
# SALES VISUALIZATION
# ==========================================================

def plot_sales(df):
    """
    Generate a sales chart and save it
    inside the reports directory.
    """

    stage_message = "Generating sales visualization..."

    progress(stage_message)

    logger.info(stage_message)

    report_directory = "reports"

    os.makedirs(
        report_directory,
        exist_ok=True,
    )

    # ------------------------------------------------------
    # PREPARE DATA
    # ------------------------------------------------------

    sales = (
        df.groupby("Product")["Price"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    # ------------------------------------------------------
    # CREATE CHART
    # ------------------------------------------------------

    plt.figure(
        figsize=(10, 6)
    )

    sales.plot(
        kind="bar"
    )

    plt.title(
        "Total Sales by Product",
        fontsize=15,
        fontweight="bold",
    )

    plt.xlabel("Product")

    plt.ylabel("Sales")

    plt.xticks(
        rotation=45,
        ha="right",
    )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    plt.tight_layout()

    # ------------------------------------------------------
    # SAVE CHART
    # ------------------------------------------------------

    output_path = os.path.join(
        report_directory,
        "sales_chart.png",
    )

    plt.savefig(
        output_path,
        dpi=300,
    )

    plt.close()

    completed(
        "Sales chart generated successfully."
    )

    logger.info(
        "Sales chart saved at %s",
        output_path,
    )

    return output_path 