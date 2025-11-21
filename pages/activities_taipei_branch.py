"""
台北分會活動頁面
展示台北分會的各項活動資訊、聚會方式和小組狀況
"""

import streamlit as st
from utils.utils import init_page

# 初始化頁面設定
init_page(page_name="activities_taipei_branch")

st.title("台北分會活動")

# 簡介區塊
st.markdown(
    """
<div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h3 style='color: #2c5282; margin-top: 0;'>📍 聚會方式</h3>
    <p style='font-size: 1.1em; line-height: 1.8;'>
        除會慶及特別活動外，每月最後一週的星期六下午舉行全會：<br>
        🕒 <strong>下午 3:00</strong> - 全會<br>
        🕔 <strong>下午 5:00</strong> - 共融彌撒<br>
        🕕 <strong>下午 6:00</strong> - 簡餐共融<br><br>
        平時則分組聚會，各小組活動從每週一次、每月一次至不定期聚會都有。
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# 使用 tabs 來組織內容
tab1, tab2, tab3 = st.tabs(["📅 近期活動", "👥 小組介紹", "🎯 活動願景"])

with tab1:
    st.subheader("2025年（114年）活動紀錄")

    activities_2025 = [
        {
            "month": "9月",
            "title": "雷公逝世15周年泰澤追思祈禱",
            "date": "2025/10/12",
            "icon": "🕯️",
        },
        {
            "month": "8月",
            "title": "劉家正神父在愛中成長工作坊",
            "date": "2025/08/31",
            "icon": "💝",
        },
        {
            "month": "7月",
            "title": "做個世界好公民 - 陳春山教授暨易利利追思",
            "date": "2025/07/08",
            "icon": "🌍",
        },
        {
            "month": "6月",
            "title": "台北分會慶祝會慶",
            "date": "2025/06/15",
            "icon": "🎉",
        },
        {"month": "5月", "title": "月會 - 黃長春", "date": "2025/05/18", "icon": "📖"},
        {
            "month": "4月",
            "title": "烏來法蒂瑪朝聖地暨北美會員補奉獻",
            "date": "2025/05/10",
            "icon": "⛪",
        },
        {
            "month": "3月",
            "title": "四旬期避靜（李碧圓修女）",
            "date": "2025/05/10",
            "icon": "🙏",
        },
        {
            "month": "3月",
            "title": "歡迎北美會員於典藏咖啡館",
            "date": "2025/03/16",
            "icon": "☕",
        },
        {
            "month": "2月",
            "title": "台灣Camino朝聖之旅（姜樂義老師）暨春節團拜",
            "date": "2025/03/25",
            "icon": "🚶",
        },
        {"month": "2月", "title": "頤福園春節拜年", "date": "2025/03/25", "icon": "🧧"},
        {
            "month": "1月",
            "title": "享受祈禱；祈禱享受！（譚璧輝老師）",
            "date": "2025/03/25",
            "icon": "✨",
        },
    ]

    col1, col2 = st.columns(2)

    for idx, activity in enumerate(activities_2025):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(
                f"""
            <div style='background-color: white; padding: 15px; border-left: 4px solid #4299e1; 
                        margin-bottom: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='display: flex; align-items: center; margin-bottom: 8px;'>
                    <span style='font-size: 2em; margin-right: 10px;'>{activity['icon']}</span>
                    <span style='background-color: #4299e1; color: white; padding: 4px 12px; 
                                 border-radius: 12px; font-size: 0.85em; font-weight: bold;'>
                        {activity['month']}
                    </span>
                </div>
                <h4 style='color: #2d3748; margin: 10px 0 8px 0; font-size: 1.1em;'>{activity['title']}</h4>
                <p style='color: #718096; margin: 0; font-size: 0.9em;'>📅 {activity['date']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    st.subheader("2024年（113年）精選活動")

    activities_2024 = [
        {"title": "聖誕月會暨補奉獻", "date": "2023/12/17", "icon": "🎄"},
        {
            "title": "大德蘭與馬斯洛的超越性自我實現（陳美琴教授）",
            "date": "2023/11/19",
            "icon": "📚",
        },
        {"title": "共融營 - 台北分會", "date": "2023/10", "icon": "⛺"},
        {"title": "雷煥章神父逝世14周年追思", "date": "2024/09/08", "icon": "🕯️"},
        {
            "title": "好好愛自己 - 迎接未來精彩的十年（陳惠姿）",
            "date": "2024/08/18",
            "icon": "💪",
        },
        {"title": "芯媒體鍾瑪竇弟兄講座", "date": "2024/07/20", "icon": "🎬"},
        {"title": "天使教堂朝聖之旅", "date": "2024/06/29", "icon": "⛪"},
        {"title": "吳伯仁神父座談會", "date": "2024/04/14", "icon": "💬"},
        {"title": "四旬期避靜", "date": "2024/03", "icon": "🙏"},
        {"title": "新春談小會未來", "date": "2024/02/18", "icon": "🎊"},
    ]

    cols = st.columns(3)
    for idx, activity in enumerate(activities_2024):
        with cols[idx % 3]:
            st.markdown(
                f"""
            <div style='background-color: #f7fafc; padding: 12px; border-radius: 8px; 
                        margin-bottom: 10px; text-align: center; min-height: 120px;'>
                <div style='font-size: 2.5em; margin-bottom: 8px;'>{activity['icon']}</div>
                <div style='font-size: 0.95em; color: #2d3748; font-weight: 500; margin-bottom: 5px;'>
                    {activity['title']}
                </div>
                <div style='font-size: 0.8em; color: #718096;'>{activity['date']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

with tab2:
    st.subheader("各小組介紹")

    groups = [
        {
            "name": "新竹小組",
            "leader": "熊瑾瑜",
            "schedule": "每兩週聚會一次",
            "time": "星期一 7:30-9:30 PM",
            "location": "新竹市西門街天主堂",
            "description": "在耶穌會神父指導下研讀聖經，目前研讀《馬太福音注釋》",
            "icon": "📖",
        },
        {
            "name": "家庭組",
            "leader": "蕭淑美",
            "schedule": "不定期聚會",
            "time": "彈性安排",
            "location": "會員家中",
            "description": "推動「家庭查經列車」，在會員家中查經並邀請周邊會員參加",
            "icon": "👨‍👩‍👧‍👦",
        },
        {
            "name": "活糧組",
            "leader": "譚璧輝",
            "schedule": "每月第二個星期一",
            "time": "5:00-7:00 PM",
            "location": "神學院",
            "description": "現有十餘人，研讀、分享增修之會章",
            "icon": "🍞",
        },
        {
            "name": "大陸關懷組",
            "leader": "古偉瀛",
            "schedule": "每2-3個月聚會",
            "time": "當月第一個星期六晚上",
            "location": "會員家中",
            "description": "關注大陸教會現況、中梵關係，建立正向共識",
            "icon": "🤝",
        },
        {
            "name": "靜觀讀經組",
            "leader": "姜其蘭",
            "schedule": "定期聚會",
            "time": "待定",
            "location": "待定",
            "description": "一小時靜觀，一小時讀瑪竇福音",
            "icon": "🧘",
        },
        {
            "name": "藝術組",
            "leader": "陳雲珍",
            "schedule": "不定期",
            "time": "待定",
            "location": "待定",
            "description": "透過藝術活動深化信仰體驗",
            "icon": "🎨",
        },
        {
            "name": "終身奉獻組",
            "leader": "丘玉珍",
            "schedule": "配合全會活動",
            "time": "待定",
            "location": "待定",
            "description": "未參加其他小組的終身奉獻會員，組長負責聯絡與傳達消息",
            "icon": "✝️",
        },
        {
            "name": "陶成組",
            "leader": "李宇之",
            "schedule": "配合個別需求",
            "time": "彈性安排",
            "location": "待定",
            "description": "針對觀察會員及新朋友提供個別輔導與陶成",
            "icon": "🌱",
        },
    ]

    for group in groups:
        with st.expander(f"{group['icon']} {group['name']} - 組長：{group['leader']}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(
                    f"""
                **📝 活動內容：**  
                {group['description']}
                
                **📅 聚會頻率：** {group['schedule']}  
                **🕐 聚會時間：** {group['time']}  
                **📍 聚會地點：** {group['location']}
                """
                )
            with col2:
                st.info(f"**聯絡人**\n\n組長：{group['leader']}")

with tab3:
    st.subheader("台北分會的願景與使命")

    st.markdown(
        """
    <div style='background-color: #fff5f5; padding: 25px; border-radius: 10px; 
                border-left: 5px solid #e53e3e; margin-bottom: 20px;'>
        <h4 style='color: #c53030; margin-top: 0;'>🎯 年度主題：在聖三內合一</h4>
        <p style='line-height: 1.8; color: #2d3748;'>
            我們致力於在聖父、聖子、聖神的愛內，建立一個相互支持、共同成長的信仰團體。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 主要活動方向")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        #### 📚 信仰培育
        - **個人讀經與小組讀經活動**  
          鼓勵會員就近加入讀經小組
        
        - **靈修書籍閱讀**  
          推薦《靈魂的渴望》等靈修好書
        
        - **參訪修會靈修方式**  
          辦理參訪、座談等交流活動
        
        - **避靜活動**  
          三月份定期舉辦避靜
        """
        )

        st.markdown(
            """
        #### 🙏 禮儀與祈禱
        - **共融彌撒**  
          每月最後週六下午5:00
        
        - **追思祈禱**  
          紀念已亡會員，保持屬靈共融
        
        - **朝聖之旅**  
          五峰旗聖母山莊、烏來法蒂瑪等地朝聖
        """
        )

    with col2:
        st.markdown(
            """
        #### 🤝 共融與服務
        - **聖誕送愛心活動**  
          各小組自由募款，服務弱勢團體
        
        - **會慶慶祝活動**  
          凝聚團體向心力
        
        - **春節團拜**  
          探訪頤福園，關懷年長會員
        """
        )

        st.markdown(
            """
        #### 🌱 新會員陶成
        - **陶成小組**  
          針對新朋友辦理陶成課程
        
        - **老會員陪伴**  
          邀請與陪伴新會員融入團體
        
        - **個別輔導**  
          提供一對一的信仰成長支持
        """
        )

    st.markdown("---")

    st.markdown(
        """
    <div style='background-color: #f0fff4; padding: 20px; border-radius: 10px; 
                border-left: 5px solid #38a169; margin-top: 20px;'>
        <h4 style='color: #2f855a; margin-top: 0;'>💡 我們的期許</h4>
        <p style='line-height: 1.8; font-size: 1.05em; color: #2d3748;'>
            「越少參加活動的會員越需要大家鼓勵。」每個會員的出席是凝聚團體動力的最好方式，
            我們希望活動安排能符合大家在信仰福傳及靈修上實質的需要，<strong>願意參與才是最重要的</strong>。
        </p>
        <p style='text-align: right; font-style: italic; color: #2f855a; margin-bottom: 0;'>
            主祐平安！
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 頁尾返回按鈕
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("↩️ 返回活動總覽", use_container_width=True):
        st.switch_page("pages/activities.py")
