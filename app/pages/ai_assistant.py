import streamlit as st

from ai.context_builder import build_business_context
from ai.prompt_builder import build_prompt
from ai.gemini_service import ask_gemini
from components.ai_actions import ai_actions


def show_ai_assistant(data, debug):

    st.title("🤖 AI Business Assistant")

    if data is None:
        st.info("📁 Upload a dataset to continue.")
        return

    clean_df = data["clean_df"]

    actions = ai_actions()

    question = st.text_input(
        "Or ask your own question"
    )

    if actions["inventory"]:
        question = "Which products should I reorder immediately?"

    elif actions["sales"]:
        question = "Summarize the sales performance."

    elif actions["profit"]:
        question = "Analyze the business profit."

    elif actions["risk"]:
        question = "Identify the biggest inventory risks."

    elif actions["executive"]:
        question = "Give me an executive summary."

    if st.button("Ask Gemini"):

        with st.spinner("RetailPulse AI is generating business insights..."):

            context = build_business_context(clean_df)

            prompt = build_prompt(
                question,
                context
            )

            if debug:
                st.subheader("Business Context")
                st.code(context)

                st.subheader("Generated Prompt")
                st.code(prompt)

            answer = ask_gemini(prompt)

        st.markdown(answer)