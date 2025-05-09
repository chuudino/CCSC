import streamlit as st
from utils import init_page

init_page(page_name="publications")  # 初始化頁面設定並設置對應的 page_name

st.title("出版品")

st.page_link("pages/wellspring_of_the_soul.py", label="心泉", icon="💧")
