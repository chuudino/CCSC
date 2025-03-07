import streamlit as st


def menu():
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
        st.sidebar.page_link("pages/what_is_society.py", label="小會是什麼？")
    elif st.session_state.page_name == "activities":
        st.sidebar.page_link("pages/taipei_branch.py", label="台北分會")
    elif st.session_state.page_name == "serviceslife":
        st.sidebar.page_link("pages/culture_spread.py", label="文化福傳")
    elif st.session_state.page_name == "calendar":
        st.sidebar.page_link("pages/calendar_branch.py", label="分會行事曆")
    elif st.session_state.page_name == "publications":
        st.sidebar.page_link("pages/wellspring_of_the_Soul.py", label="心泉")
