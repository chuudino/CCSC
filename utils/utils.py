import streamlit as st
from .menu import menu


def init_page(page_name: str = "home"):
    # 設置頁面配置和標題
    page_titles = {
        "home": "首頁",
        "about_us": "關於我們",
        "about_us_what_is_ccsc": "小會是甚麼",
        "about_us_vision_ccsc": "宗旨與精神",
        "about_us_history_ccsc": "歷史沿革",
        "about_us_timeline_ccsc": "大事年表",
        "activities": "活動訊息",
        "activities_head_office": "總會活動",
        "activities_taipei_branch": "台北分會活動",
        "activities_taichung_branch": "台中分會活動",
        "activities_kaohsiung_branch": "高雄分會活動",
        "activities_northamerica_branch": "北美分會活動",
        "serviceslife": "服務與生活",
        "serviceslife_culture_spread": "文化福傳",
        "calendar": "行事曆",
        "calendar_head_office": "總會行事曆",
        "calendar_taipei_branch": "台北分會行事曆",
        "calendar_taichung_branch": "台中分會行事曆",
        "calendar_kaohsiung_branch": "高雄分會行事曆",
        "calendar_northamerica_branch": "北美分會行事曆",
        "publications": "小會刊物",
        "publications_wellspring": "心泉",
        "publications_mustard_seed": "芥子",
        "search": "搜尋",
    }

    page_title = page_titles.get(page_name, "CCSC Website")
    st.set_page_config(page_title=f"{page_title} - CCSC", page_icon="⛪", layout="wide")
    st.logo("static/images/logo.png")
    if page_name not in st.session_state:
        st.session_state.page_name = page_name

    menu()

    # 添加版權聲明
    st.markdown(
        """
        <div style="
            position: fixed;
            left: 50%;
            bottom: 20px;
            transform: translateX(-50%);
            text-align: center;
            background-color: transparent;
            z-index: 1000;
        ">
            <p style="margin: 0; font-size: 14px;">Copyright © 中華基督神修小會</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
