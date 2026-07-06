import streamlit as st

from ai.context_builder import build_business_context
from ai.prompt_builder import build_prompt
from ai.gemini_service import ask_gemini


def show_executive_summary(data):

    st.title("📑 Executive Summary")

    if data is None:
        st.info("📁 Upload a dataset first.")
        return

    clean_df = data["clean_df"]

    if st.button("Generate Executive Report"):

        with st.spinner("Generating report..."):

            context = build_business_context(clean_df)

            prompt = build_prompt(
                "Generate a one-page executive business summary with key insights, risks, opportunities and recommendations.",
                context
            )

            answer = ask_gemini(prompt)

        st.markdown(answer)