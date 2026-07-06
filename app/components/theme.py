import streamlit as st


def load_theme():

    st.markdown(
        """
        <style>

        .main {
            background-color: #F8FAFC;
        }

        div[data-testid="stMetric"]{
            border-radius:12px;
            padding:18px;
            background:#ffffff;
            box-shadow:0px 2px 8px rgba(0,0,0,.08);
        }

        div.stButton > button{
            width:100%;
            border-radius:10px;
        }

        .stDataFrame{
            border-radius:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )