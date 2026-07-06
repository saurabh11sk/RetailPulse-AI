import streamlit as st

from components.filter_panel import apply_filters
from analytics.business_score import calculate_business_score
from analytics.kpi_engine import calculate_kpis
from analytics.insights_engine import generate_insights

from analytics.charts import (
    revenue_by_category,
    daily_sales,
    top_products
)

from ai.recommendation_engine import generate_recommendations
from analytics.alert_engine import generate_alerts

def show_dashboard(data, debug):

    st.title("🏠 Dashboard")

    if data is None:
        st.info("📁 Upload a dataset to continue.")
        return

    clean_df = apply_filters(data["clean_df"])

    kpis = calculate_kpis(clean_df)
    insights = generate_insights(kpis)
    alerts = generate_alerts(clean_df)
    business_score = calculate_business_score(kpis)
    recommendations = generate_recommendations(clean_df)

    # ==========================
    # KPI Cards
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Revenue",
            f"₹{kpis['revenue']:,.2f}"
        )

    with col2:
        st.metric(
            "📦 Products Sold",
            f"{kpis['products_sold']:,}"
        )

    with col3:
        st.metric(
            "⚠ Low Stock",
            kpis["low_stock"]
        )

    with col4:
        st.metric(
            "💵 Profit",
            f"₹{kpis['profit']:,.2f}"
        )

    # ==========================
    # Business Insights
    # ==========================
    st.divider()

    st.subheader("🏆 Retail Health Score")

    score_col1, score_col2 = st.columns([1, 3])

    with score_col1:
        st.metric(
            "Business Score",
            f"{business_score}/100"
        )

    with score_col2:
        st.progress(business_score / 100)

        if business_score >= 80:
            st.success("Excellent Business Health")

        elif business_score >= 60:
            st.warning("Business is Stable")

        else:
            st.error("Business Needs Attention")

    st.divider()

    st.subheader("🚨 Business Alerts")

    if alerts:

        for level, message in alerts:

            if level == "success":
                st.success(message)

            elif level == "warning":
                st.warning(message)

            elif level == "error":
                st.error(message)

    st.divider()

    st.subheader("🧠 Business Insights")

    if insights:

        for insight in insights:
            st.info(insight)

    else:
        st.success("No business insights available.")

    # ==========================
    # Dataset Preview
    # ==========================

    st.divider()

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        clean_df.head(),
        use_container_width=True
    )

    st.caption(f"Total Records : {len(clean_df)}")

    # ==========================
    # Charts
    # ==========================

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            revenue_by_category(clean_df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            daily_sales(clean_df),
            use_container_width=True
        )

    st.plotly_chart(
        top_products(clean_df),
        use_container_width=True
    )

    # ==========================
    # Developer Mode
    # ==========================

    if debug:

        st.divider()

        st.subheader("🛠 Developer Mode")

        st.write("### 🔴 Low Stock Products")
        st.dataframe(
            recommendations["low_stock"],
            use_container_width=True
        )

        st.write("### 🟢 Top Selling Products")
        st.dataframe(
            recommendations["top_products"],
            use_container_width=True
        )

        st.write("### 🟡 Slow Selling Products")
        st.dataframe(
            recommendations["slow_products"],
            use_container_width=True
        )

        st.write("### 📈 Top Revenue Categories")
        st.dataframe(
            recommendations["top_categories"],
            use_container_width=True
        )