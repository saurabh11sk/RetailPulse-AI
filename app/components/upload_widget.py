import streamlit as st


def upload_csv():

    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None

    uploaded_file = st.file_uploader(
        "📂 Upload Retail Dataset",
        type=["csv"]
    )

    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file

    return st.session_state.uploaded_file