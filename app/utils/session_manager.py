import streamlit as st


def initialize_session():

    if "clean_df" not in st.session_state:
        st.session_state.clean_df = None

    if "data" not in st.session_state:
        st.session_state.data = None


def save_data(data):

    st.session_state.data = data

    st.session_state.clean_df = data["clean_df"]


def get_data():

    return st.session_state.data