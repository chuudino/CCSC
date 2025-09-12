import streamlit as st
from utils import init_page

init_page(page_name="calendar")  # 初始化頁面設定並設置對應的 page_name

st.title("行事曆")

st.sidebar.page_link("pages/calendar_head_office.py", label="總會活動", icon="🎯")
st.sidebar.page_link("pages/calendar_taipei_branch.py", label="台北分會活動", icon="🎯")
st.sidebar.page_link(
    "pages/calendar_taichung_branch.py", label="台中分會活動", icon="📋"
)
st.sidebar.page_link(
    "pages/calendar_kaohsiung_branch.py", label="高雄分會活動", icon="📅"
)
st.sidebar.page_link(
    "pages/calendar_northamerica_branch.py", label="北美分會活動", icon="📊"
)
