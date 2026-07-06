import streamlit as st


def show_inventory(data):

    st.title("📦 Inventory Intelligence")

    if data is None:
        st.info("📁 Upload a dataset to continue.")
        return

    inventory = data["inventory"]

    tab1, tab2, tab3 = st.tabs(
        [
            "🔴 Low Stock",
            "🟡 Overstock",
            "🟢 Healthy Stock"
        ]
    )

    with tab1:
        st.dataframe(
            inventory["low_stock"],
            use_container_width=True
        )

    with tab2:
        st.dataframe(
            inventory["over_stock"],
            use_container_width=True
        )

    with tab3:
        st.dataframe(
            inventory["healthy_stock"],
            use_container_width=True
        )