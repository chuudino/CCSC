import streamlit as st
from utils import init_page

init_page(page_name="calendar_taipei_branch")  # 初始化頁面設定並設置對應的 page_name

st.title("台北分會行事曆")

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/calendar.py")

# 這之後可以加入你的頁面內容
st.write(
    """

""",
    unsafe_allow_html=True,
)
