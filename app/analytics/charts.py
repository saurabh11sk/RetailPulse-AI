import plotly.express as px


def revenue_by_category(df):
    category_sales = (
        df.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        names="Category",
        values="Revenue",
        title="Revenue by Category"
    )

    return fig


def daily_sales(df):
    daily = (
        df.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily,
        x="Date",
        y="Revenue",
        title="Daily Revenue Trend",
        markers=True
    )

    return fig


def top_products(df):
    products = (
        df.groupby("Product_Name")["Quantity_Sold"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        products,
        x="Product_Name",
        y="Quantity_Sold",
        title="Top 10 Selling Products"
    )

    return fig
