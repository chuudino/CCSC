# 新增分頁與初始化步驟說明

1. 詢問使用者需求
   - 請使用者提供新頁面的功能說明即可，英文名稱（檔案名稱與 page_name）將根據需求自動產生（僅用英文、數字或底線，不需詢問使用者）。

2. 新增分頁檔案
   - 依據使用者需求，在 pages 資料夾中建立新的 Python 檔案，檔名會自動以英文產生。

3. 貼上基本程式架構
   - 在新檔案中加入以下基本程式碼架構，page_name 會自動以英文產生並與檔案名稱一致：

    ```python
    import streamlit as st
    from utils import init_page

    init_page(page_name="your_page_name")  # 初始化頁面設定，會自動以英文命名並與檔案名稱一致

    if st.sidebar.button("↩️ 返回上一頁"):
        st.switch_page("pages/previous_page.py")

    # 這之後可以加入你的頁面內容
    st.title("Your Page Title")
    st.markdown(
        """
        這裡可以放置頁面說明或內容。
        """,
        unsafe_allow_html=True,
    )
    ```

4. 初始化規範
   - 每個分頁都需使用 init_page 並設定對應 page_name（自動以英文命名，與檔案名稱一致）。
   - init_page 需顯示該頁面的 page_title，讓使用者清楚目前所在頁面。