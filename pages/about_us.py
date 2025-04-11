import streamlit as st
from utils import init_page

st.set_page_config(page_title="About Us", page_icon="👨‍👩‍👧‍👦", layout="wide")
st.logo("static/images/logo.png")
st.title("關於我們")

st.sidebar.title("導航")
st.sidebar.page_link("main.py", label="首頁", icon="✝️")
st.sidebar.page_link("pages/what_is_ccsc.py", label="小會是什麼？", icon="❓")
st.sidebar.page_link("pages/vision_ccsc.py", label="宗旨與精神", icon="📜")
st.sidebar.page_link("pages/history_ccsc.py", label="歷史沿革", icon="📖")
st.sidebar.page_link("pages/timeline_ccsc.py", label="大事年表", icon="📅")
