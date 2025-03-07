# 天主教中華基督神修小會網站 (CCSC Website)

<div align="center">
  <img src="static/images/logo.png" alt="CCSC Logo" width="150" />
  <h3>
    天主教中華基督神修小會<br>
    Chinese Christian Spirit Community
  </h3>
</div>

## 📝 專案介紹

這是天主教中華基督神修小會的官方網站應用，使用Streamlit框架開發。本網站旨在提供關於小會的信息、活動和服務，並促進社區交流與聯繫。

## ✨ 功能特色

- **首頁**: 組織基本信息、聯繫方式和地理位置
- **關於我們**: 小會歷史、使命和價值觀
- **活動**: 最新活動公告和台北分會特別活動
- **服務與生活**: 展示小會的服務項目和日常生活
- **行事曆**: 小會活動行事曆和分會行事曆
- **出版品**: 提供「心泉」等出版物信息
- **搜尋**: 網站內容搜尋功能

## 🛠️ 技術架構

- **前端框架**: Streamlit
- **程式語言**: Python
- **環境配置**: Dotenv
- **視覺設計**: HTML/CSS (Streamlit自定義組件)

## 📦 安裝指南

1. 克隆此儲存庫

   ```bash
   git clone [repository-url]
   cd CCSC
   ```

2. 安裝所需套件

   ```bash
   pip install -r requirements.txt
   ```

3. 創建環境變數檔案(可選)

   ```bash
   # .env 檔案
   dev=false
   ```

## 🚀 使用說明

啟動應用程式:

```bash
streamlit run main.py
```

應用程式將在本地端啟動，通常在 <http://localhost:8501>

## 📂 專案結構

```
CCSC/
│
├── main.py                 # 主入口文件
├── requirements.txt        # 依賴套件
│
├── pages/                  # 網站各頁面
│   ├── about_us.py         # 關於我們
│   ├── activities.py       # 活動
│   ├── calendar.py         # 行事曆
│   ├── calendar_branch.py  # 分會行事曆
│   ├── culture_spread.py   # 文化福傳
│   ├── publications.py     # 出版品
│   ├── search.py           # 搜尋
│   ├── serviceslife.py     # 服務與生活
│   ├── taipei_branch.py    # 台北分會
│   ├── wellspring_of_the_soul.py  # 心泉
│   └── what_is_society.py  # 小會是什麼
│
├── static/                 # 靜態資源
│   └── images/             # 圖片資源
│       ├── banner.jpg      
│       ├── logo.png        
│       ├── logo.svg        
│       └── 背景素材.jpg
│
└── utils/                  # 工具函數
    ├── __init__.py
    ├── menu.py             # 導航菜單
    └── utils.py            # 通用工具
```

## 📞 聯絡資訊

- **總會地址**: 台北市中山區林森北路73號2樓
- **聯絡電話**: (8862) 2523-0538
- **Email**: <ccscasso@gmail.com>

## 💰 支持我們

如果您想支持我們的事工，可以透過以下方式捐款：

**捐款帳號**:  
社團法人天主教中華基督神修小會之友人文關懷與服務促進協會  
華南銀行新生分行 113-20-094051-5

## 📄 版權聲明

Copyright © 中華基督神修小會
