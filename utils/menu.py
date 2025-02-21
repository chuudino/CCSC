import streamlit as st


def menu():
    st.sidebar.title("導航")
    st.sidebar.page_link("main.py", label="首頁", icon="✝️")
    if st.session_state.page_name == "home":
        st.sidebar.page_link("pages/About Us.py", label="關於我們", icon="👨‍👩‍👧‍👦")
        st.sidebar.page_link("pages/Activities.py", label="活動", icon="🎯")
        st.sidebar.page_link("pages/Calendar.py", label="行事曆", icon="📅")
        st.sidebar.page_link("pages/Publications.py", label="出版品", icon="📚")
        st.sidebar.page_link("pages/Search.py", label="搜尋", icon="🔍")
        st.sidebar.page_link("pages/ServicesLife.py", label="禮拜生活", icon="🙏")
    elif st.session_state.page_name == "About Us":
        st.sidebar.page_link("pages/what_is_society.py", label="小會是什麼？")
