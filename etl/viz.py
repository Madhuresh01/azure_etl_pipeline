import matplotlib.pyplot as plt

def plot_sales(df):
    # Group total price by product
    sales = df.groupby("Product")["Price"].sum()

    # Create bar chart
    plt.figure(figsize=(8, 5))
    sales.plot(kind="bar")

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Price")

    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save chart
    plt.savefig("reports/sales_chart.png")

    # Show chart
    plt.show()

    print("✅ Chart saved in reports/sales_chart.png")
    
    import matplotlib.pyplot as plt


def plot_sales(df):
    sales = df.groupby("Product")["Price"].sum()

    plt.figure(figsize=(8, 5))
    sales.plot(kind="bar")

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Price")

    plt.xticks(rotation=45)
    plt.tight_layout()

    chart_path = "reports/sales_chart.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Chart saved to {chart_path}")