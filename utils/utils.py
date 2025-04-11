import os
import dotenv
import streamlit as st
from .menu import menu

dotenv.load_dotenv()


def init_page(page_name: str = "home"):
    DEV = os.getenv("dev", "false").lower() == "true"
    if DEV:
        pass
        # import subprocess
        # try:
        #     subprocess.run(
        #         ["pipreqs", ".", "--force"], check=True, text=True, capture_output=True
        #     )
        # except Exception as e:
        #     print(f"命令執行失敗：\n{e}")

    # 設置頁面配置和標題
    page_titles = {
        "home": "首頁",
        "about_us": "關於我們",
        "what_is_ccsc": "小會是甚麼",
        "vision_ccsc": "宗旨與精神",
        "history_ccsc": "歷史沿革",
        "timeline_ccsc": "大事年表",
        "activities": "活動",
        "serviceslife": "服務與生活",
        "calendar": "行事曆",
        "calendar_branch": "分會行事曆",
        "publications": "出版品",
        "search": "搜尋",
        "taipei_branch": "台北分會",
        "culture_spread": "文化福傳",
        "wellspring": "心泉",
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
