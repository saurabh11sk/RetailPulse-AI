# from ai.recommendation_engine import generate_recommendations

# def build_business_context(df):

#     recommendations = generate_recommendations(df)

#     context = f"""
# BUSINESS SUMMARY

# Total Revenue: ₹{df['Revenue'].sum():,.2f}

# Total Profit: ₹{df['Profit'].sum():,.2f}

# Products Sold: {df['Quantity_Sold'].sum()}

# LOW STOCK PRODUCTS

# {recommendations['low_stock'].to_string(index=False)}

# TOP SELLING PRODUCTS

# {recommendations['top_products'].to_string(index=False)}

# SLOW SELLING PRODUCTS

# {recommendations['slow_products'].to_string(index=False)}

# TOP REVENUE CATEGORIES

# {recommendations['top_categories'].to_string(index=False)}
# """

#     return context



def build_business_context(df):

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()
    products = df["Quantity_Sold"].sum()

    low_stock = len(
        df[df["Current_Stock"] <= df["Reorder_Level"]]
    )

    top_category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .idxmax()
    )

    top_product = (
        df.groupby("Product_Name")["Revenue"]
        .sum()
        .idxmax()
    )

    context = f"""
Business Overview

Total Revenue : ₹{revenue:,.2f}

Total Profit : ₹{profit:,.2f}

Products Sold : {products}

Low Stock Products : {low_stock}

Best Category : {top_category}

Best Selling Product : {top_product}
"""

    return context
