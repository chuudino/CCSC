import streamlit as st
from utils import init_page

init_page(page_name="activities_head_office")  # 初始化頁面設定

st.title("總會活動")

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/activities.py")

# 這之後可以加入你的頁面內容
st.write(
    """

""",
    unsafe_allow_html=True,
)
