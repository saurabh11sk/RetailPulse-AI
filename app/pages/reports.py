import streamlit as st
from datetime import datetime

from services.report_generator import generate_report


def show_reports(data):

    st.title("📄 Business Reports")

    if data is None:
        st.info("📁 Upload a dataset to continue.")
        return

    clean_df = data["clean_df"]
    kpis = data["kpis"]

    st.subheader("📊 Business Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Revenue", f"₹{kpis['revenue']:,.2f}")
        st.metric("Profit", f"₹{kpis['profit']:,.2f}")

    with col2:
        st.metric("Products Sold", kpis["products_sold"])
        st.metric("Low Stock", kpis["low_stock"])

    st.divider()

    report = generate_report(kpis)

    st.subheader("📋 Generated Report")

    st.text(report)

    st.download_button(
        "📥 Download TXT Report",
        report,
        file_name=f"RetailPulse_Report_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

    csv = clean_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        csv,
        file_name=f"RetailPulse_Data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

    st.divider()

    st.subheader("Dataset")

    st.dataframe(
        clean_df,
        use_container_width=True
    )