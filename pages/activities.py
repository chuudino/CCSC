import streamlit as st
from utils import init_page

init_page(page_name="activities")  # 初始化頁面設定並設置對應的 page_name

st.title("小會活動")

st.sidebar.page_link("pages/activites_head_office.py", label="總會活動", icon="🎯")
st.sidebar.page_link(
    "pages/activites_taipei_branch.py", label="台北分會活動", icon="🎯"
)
st.sidebar.page_link(
    "pages/activites_taichung_branch.py", label="台中分會活動", icon="📋"
)
st.sidebar.page_link(
    "pages/activites_kaohsiung_branch.py", label="高雄分會活動", icon="📅"
)
st.sidebar.page_link(
    "pages/activites_northamerica_branch.py", label="北美分會活動", icon="📊"
)
