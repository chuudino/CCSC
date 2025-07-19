import streamlit as st


def menu():
    st.sidebar.title("導航")
    st.sidebar.page_link("main.py", label="首頁", icon="✝️")
    if st.session_state.page_name == "home":
        st.sidebar.page_link("pages/about_us.py", label="關於我們", icon="👨‍👩‍👧‍👦")
        st.sidebar.page_link("pages/activities.py", label="活動訊息", icon="🎯")
        st.sidebar.page_link("pages/serviceslife.py", label="服務與生活", icon="🛠️")
        st.sidebar.page_link("pages/calendar.py", label="行事曆", icon="📅")
        st.sidebar.page_link("pages/publications.py", label="小會刊物", icon="📚")
        st.sidebar.page_link("pages/search.py", label="搜尋", icon="🔍")
    elif st.session_state.page_name == "about_us":
        st.sidebar.page_link(
            "pages/about_us_what_is_ccsc.py", label="小會是甚麼?", icon="❓"
        )
        st.sidebar.page_link(
            "pages/about_us_vision_ccsc.py", label="宗旨與精神", icon=""
        )
        st.sidebar.page_link(
            "pages/about_us_history_ccsc.py", label="歷史沿革", icon="✝️"
        )
        st.sidebar.page_link(
            "pages/about_us_timeline_ccsc.py", label="大事年表", icon="📅"
        )
    elif st.session_state.page_name == "activities":
        st.sidebar.page_link(
            "pages/activities_head_office.py", label="總會活動", icon="🎯"
        )
        st.sidebar.page_link(
            "pages/activities_taipei_branch.py", label="台北分會活動", icon="🎯"
        )
        st.sidebar.page_link(
            "pages/activities_taichung_branch.py", label="台中分會活動", icon="📋"
        )
        st.sidebar.page_link(
            "pages/activities_kaohsiung_branch.py", label="高雄分會活動", icon="📅"
        )
        st.sidebar.page_link(
            "pages/northamerica_branch.py", label="北美分會活動", icon="📊"
        )

    elif st.session_state.page_name == "serviceslife":
        st.sidebar.page_link("pages/serviceslife_culture_spread.py", label="服務與生活")
    elif st.session_state.page_name == "calendar":
        st.sidebar.page_link(
            "pages/calendar_head_office.py", label="總會行事曆", icon="📅"
        )
        st.sidebar.page_link(
            "pages/calendar_taipei_branch.py", label="台北分會行事曆", icon="📅"
        )
        st.sidebar.page_link(
            "pages/calendar_taichung_branch.py", label="台中分會行事曆", icon="📅"
        )
        st.sidebar.page_link(
            "pages/calendar_kaohsiung_branch.py", label="高雄分會行事曆", icon="📅"
        )
        st.sidebar.page_link(
            "pages/calendar_northamerica_branch.py", label="北美分會行事曆", icon="📅"
        )
    elif st.session_state.page_name == "publications":
        st.sidebar.page_link("publications_wellspring.py", label="心泉", icon="💧")
        st.sidebar.page_link("publications_mustard_seed.py", label="芥子", icon="🌱")
    elif st.session_state.page_name == "search":
        st.sidebar.page_link("pages/search.py", label="搜尋", icon="🔍")
