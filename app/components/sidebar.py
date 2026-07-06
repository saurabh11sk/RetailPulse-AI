import streamlit as st


def sidebar_navigation():

    with st.sidebar:

        st.image(
            "assets/logo.png",
            use_container_width=True
        )

        st.title("RetailPulse AI")

        st.caption("Decision Intelligence Platform")

        st.markdown("---")

        page = st.radio(
            "",
            [
                "🏠 Dashboard",
                "📦 Inventory",
                "📈 Forecast",
                "🤖 AI Assistant",
                "📄 Reports",
                "📑 Executive Summary"
            ]
        )

        st.markdown("---")

        debug = st.toggle("🛠 Developer Mode")

        st.markdown("---")

        st.info("🚀 Google Gen AI Hackathon")

    return page, debug