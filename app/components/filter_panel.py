import streamlit as st


def apply_filters(df):

    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filters")

    category = st.sidebar.multiselect(
        "Category",
        sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    region = st.sidebar.multiselect(
        "Region",
        sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    filtered_df = df[
        (df["Category"].isin(category)) &
        (df["Region"].isin(region))
    ]

    return filtered_df