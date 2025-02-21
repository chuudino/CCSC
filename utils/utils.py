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

    st.set_page_config(page_title="CCSC Website", page_icon="⛪", layout="wide")
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


#     st.write(
#         """
# <style>
#     /* 隱藏多餘元素 */
#     [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stHeader"], footer{
#         display: none !important;
#     }
# </style>
# """,
#         unsafe_allow_html=True,
#     )
