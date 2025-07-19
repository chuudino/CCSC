import streamlit as st
from utils import init_page

init_page(page_name="calendar_kaohsiung_branch")  # 初始化頁面設定並設置對應的 page_name

st.title("高雄分會行事曆")
if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/activities_kaohsiung_branch.py")
