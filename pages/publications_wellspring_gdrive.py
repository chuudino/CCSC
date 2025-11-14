"""
心泉期刊頁面
此頁面用於顯示心泉期刊的 PDF 檔案,從 Google Drive 讀取並顯示。
"""

import streamlit as st
from utils.utils import init_page
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 初始化頁面設定
init_page(page_name="publications_wellspring_gdrive")

# Google Drive API 存取範圍
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
FOLDER_ID = "11JN4xCs2UIGoLpoGILrw_GuPKbciyJwk"  # 心泉期刊的 Google Drive 資料夾 ID


def get_google_drive_service():
    """
    初始化並返回 Google Drive API 服務

    Returns:
        service: Google Drive API 服務實例,如果初始化失敗則返回 None
    """
    try:
        # 從 Streamlit Secrets 或本地檔案讀取憑證
        try:
            # 優先使用 Streamlit Secrets (用於雲端部署)
            credentials_info = dict(st.secrets["gcp_service_account"])
            credentials = service_account.Credentials.from_service_account_info(
                credentials_info, scopes=SCOPES
            )
        except (FileNotFoundError, KeyError):
            # 本地開發時使用 JSON 檔案
            credentials = service_account.Credentials.from_service_account_file(
                "ace-computer-451607-a1-9c4b30a7b822.json", scopes=SCOPES
            )

        # 建立 Google Drive API 服務
        service = build("drive", "v3", credentials=credentials)
        return service
    except Exception as e:
        st.error(f"初始化 Google Drive 服務時發生錯誤：{str(e)}")
        return None


st.title("心泉")

# 初始化 Google Drive 服務
service = get_google_drive_service()

# 指定要讀取的資料夾 ID
folder_id = "11JN4xCs2UIGoLpoGILrw_GuPKbciyJwk"

# 初始化字典
wellspring_issues = {}

# 檢查服務是否成功初始化
if service is None:
    st.error("無法初始化 Google Drive 服務。請稍後再試。")
else:
    # 初始化字典以存儲檔案資訊
    wellspring_issues = {}

    try:
        # 獲取資料夾中的檔案
        with st.spinner("正在讀取心泉期刊列表..."):
            results = (
                service.files()
                .list(
                    q=f"'{folder_id}' in parents and mimeType='application/pdf'",
                    pageSize=100,
                    fields="files(id, name)",
                    orderBy="name desc",  # 依檔名排序，最新的排在前面
                )
                .execute()
            )

        # 將檔案資訊存入字典
        for file in results.get("files", []):
            try:
                # 假設檔案名稱格式為 "第 XXX 期:標題"
                wellspring_issues[file["name"]] = (
                    f"https://drive.google.com/file/d/{file['id']}/preview"
                )
            except Exception as e:
                st.warning(
                    f"處理檔案 '{file.get('name', '未知')}' 時發生錯誤：{str(e)}"
                )
                continue

        if not wellspring_issues:
            st.warning("在指定的資料夾中沒有找到任何 PDF 檔案。")

    except Exception as e:
        st.error(f"讀取檔案列表時發生錯誤：{str(e)}")
        wellspring_issues = {}

if wellspring_issues:
    selected_issue = st.sidebar.selectbox(
        "請選擇期數：", list(wellspring_issues.keys())
    )
    st.write(f"### {selected_issue}")

    # 顯示 Google Drive PDF 內容
    st.components.v1.iframe(wellspring_issues[selected_issue], height=600)
else:
    st.warning(
        "目前沒有可用的期刊。請確認 Google Drive 資料夾 ID 是否正確，以及資料夾中是否有 PDF 檔案。"
    )

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/publications.py")
