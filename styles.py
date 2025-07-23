import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        .main {background-color: #fff;}
        .stApp {background-color: #fff;}
        .css-1d391kg {background-color: #fff;}
        .st-bd {background-color: #fff;}
        .st-emotion-cache-1v0mbdj {background-color: #fff;}
        .st-bx {background-color: #fff;}
        /* Orange and grey palette */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #fff;
            color: #f95d1d;
        }
        [data-baseweb="tab"] {
            color: #f95d1d;
        }
        [data-baseweb="tab"]:hover {
            background-color: #ececec;
            color: #f95d1d;
        }
        .stButton>button {
            background-color: #f95d1d;
            color: #fff;
        }
        .stButton>button:hover {
            background-color: #e65c00;
            color: #fff;
        }
        </style>
    """, unsafe_allow_html=True)
