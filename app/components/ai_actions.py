import streamlit as st


def ai_actions():

    st.subheader("⚡ Smart AI Actions")

    col1, col2 = st.columns(2)

    with col1:
        inventory = st.button("📦 Inventory Recommendation")
        sales = st.button("📈 Sales Summary")
        profit = st.button("💰 Profit Analysis")

    with col2:
        risk = st.button("⚠ Risk Analysis")
        executive = st.button("📊 Executive Summary")
        custom = st.button("🤖 Custom Question")

    return {
        "inventory": inventory,
        "sales": sales,
        "profit": profit,
        "risk": risk,
        "executive": executive,
        "custom": custom
    }