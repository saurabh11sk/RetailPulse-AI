def calculate_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_products_sold = df["Quantity_Sold"].sum()
    low_stock_products = (df["Current_Stock"] <= df["Reorder_Level"]).sum()

    return {
        "revenue": total_revenue,
        "profit": total_profit,
        "products_sold": total_products_sold,
        "low_stock": low_stock_products
    }