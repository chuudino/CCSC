import streamlit as st
from utils import init_page

init_page(page_name="wellspring")  # 初始化頁面設定並設置對應的 page_name

st.title("心泉")

# 心泉期數與對應 Google Drive 連結
wellspring_issues = {
    "第 102 期:地上的鹽 世界的光": "https://drive.google.com/file/d/1Vxm9bg8vI3PYVuI4Nk9QY1tqGzpooegv/preview",
    "第 101 期:福傳・靈修・陪伴": "https://drive.google.com/file/d/1ICu4fT9bPHOxD6EexVDbpiO7I2kLbzjn/preview",
}

selected_issue = st.sidebar.selectbox("請選擇期數：", list(wellspring_issues.keys()))

st.write(f"### {selected_issue}")

# 顯示 Google Drive PDF 內容
st.components.v1.iframe(wellspring_issues[selected_issue], height=600)
