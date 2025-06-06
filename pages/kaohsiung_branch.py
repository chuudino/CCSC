import streamlit as st
from utils import init_page

init_page(page_name="kaohsiung_branch")  # 初始化頁面設定並設置對應的 page_name

st.title("高雄分會")


if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/activities.py")

# 這之後可以加入你的頁面內容
st.title("高雄分會活動")
st.write(
    """

"""
)
