## CCSC 網站開發指南

這是一個使用 Streamlit 開發的天主教中華基督神修小會官方網站。以下是協助開發的重要資訊：

### 專案架構
- 核心入口: `main.py` - 網站主要入口點
- 頁面結構: `pages/` 目錄包含所有子頁面，依功能分類:
  - 關於我們系列: `about_us*.py`
  - 活動相關: `activities*.py`
  - 行事曆: `calendar*.py`
  - 出版品: `publications*.py`
  - 服務生活: `serviceslife*.py`
- 共用元件: `utils/` 目錄包含核心功能:
  - `utils.py`: 頁面初始化和共用函數
  - `menu.py`: 導航系統
- 靜態資源: `static/images/` 存放圖片資源

### 關鍵開發模式
1. **頁面初始化模式**
```python
from utils.utils import init_page

def main():
    init_page(page_name="about_us")  # 必須在頁面頂部調用
```

2. **導航系統整合**
- 所有頁面必須透過 `init_page()` 整合到導航系統
- 導航狀態透過 `st.session_state.page_name` 維護

3. **分會頁面模式**
- 總會/分會頁面採用一致的命名模式:
  - 主頁面: `activities.py`, `calendar.py`
  - 分會頁面: `activities_taipei_branch.py`, `calendar_taipei_branch.py`

### 重要工作流程
1. **本地開發**
```powershell
pip install -r requirements.txt  # 安裝依賴
streamlit run main.py           # 啟動開發伺服器
```

2. **環境設定**
- 使用 `.env` 文件管理環境變數 (可選)
- 設定 `dev=false` 用於生產環境

### 整合要點
1. **頁面間通訊**
- 使用 `st.session_state` 共享輕量級狀態
- 避免跨頁面的複雜狀態管理

2. **自定義風格**
- 使用 `st.markdown(..., unsafe_allow_html=True)` 實現自定義布局
- 圖片路徑使用相對路徑: `static/images/logo.png`

### 注意事項
- 保持 API 穩定性: 不要更改 `init_page` 或 `menu` 的公共介面
- 同步修改: 修改共用函數時需更新所有相關頁面
- 單一職責: 每個頁面模組專注於單一功能領域
- 無資料庫依賴: 目前為純靜態內容，加入外部整合時使用環境變數

遇到問題？請先查看 `README.md` 或聯繫專案維護者。
