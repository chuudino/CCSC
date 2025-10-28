try:
    from .utils import init_page
except Exception:
    # 若無法匯入 utils.init_page，提供一個簡單的替代函式以避免 import 時崩潰
    def init_page(page_name: str = "home"):
        # 最小化實作：在頁面上顯示頁面名稱（實際專案可用更完整實作替換）
        try:
            import streamlit as st

            st.session_state.setdefault("page_name", page_name)
            try:
                st.set_page_config(
                    page_title=f"{page_name} - CCSC", page_icon="⛪", layout="wide"
                )
            except Exception:
                pass
        except Exception:
            pass


try:
    from .menu import menu
except Exception:
    # 提供一個簡單的 fallback menu，避免在匯入時拋錯
    def menu():
        try:
            import streamlit as st

            st.sidebar.title("導航")
        except Exception:
            pass
