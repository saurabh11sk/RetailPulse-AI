import streamlit as st


REQUIRED_COLUMNS = [
    "Date",
    "Product_ID",
    "Product_Name",
    "Category",
    "Quantity_Sold",
    "Selling_Price",
    "Current_Stock"
]


def validate_columns(df):
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        st.error(f"❌ Missing Columns: {', '.join(missing_columns)}")
        return False

    return True