import streamlit as st
from utils import init_page

init_page(page_name="About Us")  # 初始化頁面設定


def menu_about_us():
    st.sidebar.title("導航")
    st.sidebar.page_link("main.py", label="首頁", icon="✝️")
    if st.session_state.page_name == "home":
        st.sidebar.page_link("pages/about_us.py", label="關於我們", icon="👨‍👩‍👧‍👦")
        st.sidebar.page_link("pages/activities.py", label="活動", icon="🎯")
        st.sidebar.page_link("pages/serviceslife.py", label="服務與生活", icon="🛠️")
        st.sidebar.page_link("pages/calendar.py", label="行事曆", icon="📅")
        st.sidebar.page_link("pages/publications.py", label="出版品", icon="📚")
        st.sidebar.page_link("pages/search.py", label="搜尋", icon="🔍")
    elif st.session_state.page_name == "about_us":
        st.sidebar.page_link("pages/what_is_ccsc.py", label="小會是什麼？")
        st.sidebar.page_link("pages/Wission_ccsc.py", label="宗旨與精神")
        st.sidebar.page_link("pages/History_ccsc.py", label="歷史沿革")
        st.sidebar.page_link("pages/Timeline_ccsc.py", label="大事年表")
        st.sidebar.page_link("pages/Contact_ccsc.py", label="聯絡我們")


menu_about_us()
