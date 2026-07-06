def generate_summary(df):
    return f"""
Total Revenue: ₹{df['Revenue'].sum():,.2f}
Total Profit: ₹{df['Profit'].sum():,.2f}
Products Sold: {df['Quantity_Sold'].sum()}
Categories: {df['Category'].nunique()}
Low Stock Products: {(df['Current_Stock'] <= df['Reorder_Level']).sum()}
"""