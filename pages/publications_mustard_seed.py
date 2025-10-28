import streamlit as st
from utils import init_page

init_page(page_name="publications_mustard_seed")  # 初始化頁面設定並設置對應的 page_name

st.title("芥子")

# 芥子期數與對應 Google Drive 連結
mustard_issues = {
    "第 001 期:   ": "https://drive.google.com/file/d/1Vxm9bg8vI3PYVuI4Nk9QY1tqGzpooegv/preview",
    "第 002 期:   ": "https://drive.google.com/file/d/1ICu4fT9bPHOxD6EexVDbpiO7I2kLbzjn/preview",
}

selected_issue = st.sidebar.selectbox("請選擇期數：", list(mustard_issues.keys()))

st.write(f"### {selected_issue}")

# 顯示 Google Drive PDF 內容
st.components.v1.iframe(mustard_issues[selected_issue], height=600)

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/publications.py")
