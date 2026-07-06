def generate_recommendations(df):
    recommendations = {}

    # Low Stock Products
    low_stock = df[
        df["Current_Stock"] <= df["Reorder_Level"]
    ][["Product_Name", "Current_Stock", "Reorder_Level"]]

    # Top Selling Products
    top_products = (
        df.groupby("Product_Name")["Quantity_Sold"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    # Slow Selling Products
    slow_products = (
        df.groupby("Product_Name")["Quantity_Sold"]
        .sum()
        .sort_values()
        .head(5)
        .reset_index()
    )

    # Top Revenue Categories
    top_categories = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    recommendations["low_stock"] = low_stock
    recommendations["top_products"] = top_products
    recommendations["slow_products"] = slow_products
    recommendations["top_categories"] = top_categories

    return recommendations