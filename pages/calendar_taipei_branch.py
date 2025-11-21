"""
台北分會行事曆頁面
展示台北分會的年度活動行事曆、月會時間和特別活動安排
"""

import streamlit as st
from utils.utils import init_page
from datetime import datetime

# 初始化頁面設定
init_page(page_name="calendar_taipei_branch")

st.title("台北分會行事曆")

# 固定聚會時間區塊
st.markdown(
    """
<div style='background-color: #ebf8ff; padding: 25px; border-radius: 10px; margin-bottom: 25px;
            border-left: 5px solid #3182ce;'>
    <h3 style='color: #2c5282; margin-top: 0;'>📅 固定聚會時間</h3>
    <div style='font-size: 1.15em; line-height: 2;'>
        <p style='margin: 10px 0;'><strong>🗓️ 月會時間：</strong>每月最後一週的星期六</p>
        <p style='margin: 10px 0;'><strong>🕒 時間安排：</strong></p>
        <ul style='list-style: none; padding-left: 20px;'>
            <li>• <strong>下午 3:00</strong> - 全會聚會</li>
            <li>• <strong>下午 5:00</strong> - 共融彌撒</li>
            <li>• <strong>下午 6:00</strong> - 簡餐共融</li>
        </ul>
        <p style='margin: 10px 0;'><strong>📍 小組聚會：</strong>各小組另行安排（每週至每月不等）</p>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# 使用 tabs 來組織內容
tab1, tab2, tab3, tab4 = st.tabs(
    ["📆 2025年行事曆", "📋 114年度完整行事曆", "📝 2024年回顧", "🔔 活動提醒"]
)

with tab1:
    st.subheader("2025年（114年）年度活動規劃")

    # 年度主題橫幅
    st.markdown(
        """
    <div style='background-color: #fff5f7; padding: 20px; border-radius: 10px; margin-bottom: 25px;
                border-left: 5px solid #e53e3e; text-align: center;'>
        <h2 style='color: #c53030; margin: 0; font-size: 1.8em;'>🎯 年度主題</h2>
        <h3 style='color: #e53e3e; margin: 10px 0; font-size: 1.5em;'>靈修 • 福傳 • 共融 • 傳承</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 第一季
    st.markdown("### 🌸 第一季（1-3月）")

    q1_events = [
        {
            "date": "1/19 (日)",
            "event": "享受祈禱，祈禱享受！",
            "speaker": "譚璧輝老師",
            "group": "溫安組",
            "type": "月會",
            "icon": "✨",
            "color": "#e6f7ff",
        },
        {
            "date": "2/9 (日)",
            "event": "台灣 Camino 朝聖之旅暨春節團拜",
            "speaker": "姜樂義老師",
            "group": "大安組",
            "type": "朝聖",
            "icon": "🚶",
            "color": "#f6ffed",
        },
        {
            "date": "3/28-30 (五-日)",
            "event": "四旬期避靜",
            "speaker": "李碧圓修女",
            "group": "文化組",
            "type": "避靜",
            "icon": "🙏",
            "color": "#f9f0ff",
        },
    ]

    for event in q1_events:
        speaker_info = (
            f"<br><span style='color: #718096; font-size: 0.9em;'>主講：{event['speaker']}</span>"
            if event["speaker"]
            else ""
        )
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #4299e1;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>{speaker_info}
                    <div style='color: #4a5568; font-size: 0.85em; margin-top: 5px;'>📋 {event['group']}</div>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background-color: #4299e1; color: white; padding: 4px 10px; border-radius: 10px; font-size: 0.8em;'>{event['type']}</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 第二季
    st.markdown("### ☀️ 第二季（4-6月）")

    q2_events = [
        {
            "date": "4/5 (六)",
            "event": "烏來法蒂瑪堂朝聖",
            "speaker": "",
            "group": "木柵組",
            "type": "朝聖",
            "icon": "⛪",
            "color": "#e6f7ff",
        },
        {
            "date": "5/18 (日)",
            "event": "原來，我的編輯生涯是趟朝聖之旅！",
            "speaker": "黃長春",
            "group": "溫安組",
            "type": "月會",
            "icon": "📖",
            "color": "#fff7e6",
        },
        {
            "date": "6/15 (日)",
            "event": "天主聖三節會慶",
            "speaker": "胡國楨神父",
            "group": "大安組",
            "type": "慶典",
            "icon": "🎉",
            "color": "#f6ffed",
        },
    ]

    for event in q2_events:
        speaker_info = (
            f"<br><span style='color: #718096; font-size: 0.9em;'>主講：{event['speaker']}</span>"
            if event["speaker"]
            else ""
        )
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #48bb78;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>{speaker_info}
                    <div style='color: #4a5568; font-size: 0.85em; margin-top: 5px;'>📋 {event['group']}</div>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background-color: #48bb78; color: white; padding: 4px 10px; border-radius: 10px; font-size: 0.8em;'>{event['type']}</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 第三季
    st.markdown("### 🍂 第三季（7-9月）")

    q3_events = [
        {
            "date": "7/20 (日)",
            "event": "傳愛一生、幸福一生 做個世界好公民",
            "speaker": "陳春山教授",
            "group": "溫安組、木柵組",
            "type": "講座",
            "icon": "🌍",
            "color": "#e6f7ff",
        },
        {
            "date": "8/31 (日)",
            "event": "在愛中成長工作坊",
            "speaker": "劉家正神父",
            "group": "大安組",
            "type": "工作坊",
            "icon": "💝",
            "color": "#fff7e6",
        },
        {
            "date": "9/14 (日)",
            "event": "雷公追思15週年",
            "speaker": "總會戎巧復",
            "group": "總會",
            "type": "追思",
            "icon": "🕯️",
            "color": "#f9f0ff",
        },
    ]

    for event in q3_events:
        speaker_info = (
            f"<br><span style='color: #718096; font-size: 0.9em;'>主講：{event['speaker']}</span>"
            if event["speaker"]
            else ""
        )
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #ed8936;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>{speaker_info}
                    <div style='color: #4a5568; font-size: 0.85em; margin-top: 5px;'>📋 {event['group']}</div>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background-color: #ed8936; color: white; padding: 4px 10px; border-radius: 10px; font-size: 0.8em;'>{event['type']}</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 第四季
    st.markdown("### ❄️ 第四季（10-12月）")

    q4_events = [
        {
            "date": "10/3-5 (五-日)",
            "event": "共融營（台中聖愛山莊）",
            "speaker": "高雄分會",
            "group": "總會",
            "type": "共融營",
            "icon": "⛺",
            "color": "#e6f7ff",
        },
        {
            "date": "11/16 (日)",
            "event": "快樂賀爾蒙 & 漫談 AI",
            "speaker": "劉佩珊博士、趙方麟博士",
            "group": "文化組",
            "type": "講座",
            "icon": "🧠",
            "color": "#fff7e6",
        },
        {
            "date": "12/14 (日)",
            "event": "慶祝聖誕",
            "speaker": "",
            "group": "文化組、邀青壯組",
            "type": "慶典",
            "icon": "🎄",
            "color": "#f6ffed",
        },
    ]

    for event in q4_events:
        speaker_info = (
            f"<br><span style='color: #718096; font-size: 0.9em;'>主講：{event['speaker']}</span>"
            if event["speaker"]
            else ""
        )
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #9f7aea;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>{speaker_info}
                    <div style='color: #4a5568; font-size: 0.85em; margin-top: 5px;'>📋 {event['group']}</div>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background-color: #9f7aea; color: white; padding: 4px 10px; border-radius: 10px; font-size: 0.8em;'>{event['type']}</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div style='background-color: #fffaf0; padding: 15px; border-radius: 8px; margin-top: 20px;'>
        <p style='margin: 0; color: #744210; font-size: 0.95em;'>
            <strong>📌 注意：</strong>活動時間若有異動，將另行通知。<br>
            詳細活動資訊請關注各月通知或聯繫分會負責人。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with tab2:
    st.subheader("114年度完整行事曆與幹部名單")

    # 完整行事曆表格
    st.markdown("#### 📅 114年度活動行事曆")

    st.markdown(
        """
    <div style='background-color: #f7fafc; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #4299e1; color: white;'>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd;'>日期</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>活動名稱</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>主講人/負責人</th>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd;'>負責組別</th>
                </tr>
            </thead>
            <tbody>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>1/19 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>享受祈禱，祈禱享受！</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>譚璧輝老師</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>溫安組</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>2/9 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>台灣 Camino 朝聖之旅暨春節團拜</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>姜樂義老師</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>大安組</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>3/28-30</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>四旬期避靜（新竹納匝肋靈修中心）</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>李碧圓修女</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>文化組</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>4/5 (六)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>烏來法蒂瑪堂朝聖</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>-</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>木柵組</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>5/18 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>原來，我的編輯生涯是趟朝聖之旅！</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>黃長春</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>溫安組</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>6/15 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>天主聖三節會慶</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>胡國楨神父</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>大安組</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>7/20 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>傳愛一生、幸福一生 做個世界好公民</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>陳春山教授</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>溫安組、木柵組</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>8/31 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>在愛中成長工作坊</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>劉家正神父</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>大安組</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>9/14 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>雷公追思15週年</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>總會戎巧復</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>總會</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>10/3-5</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>共融營（台中聖愛山莊）</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>高雄分會</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>總會</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>11/16 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>快樂賀爾蒙 & 漫談 AI</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>劉佩珊博士、趙方麟博士</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>文化組</td>
                </tr>
                <tr style='background-color: #f7fafc;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>12/14 (日)</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>慶祝聖誕</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>-</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>文化組、邀青壯組</td>
                </tr>
            </tbody>
        </table>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # 幹部名單
    st.markdown("#### 👥 114年度台北分會幹部名單")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div style='background-color: #ebf8ff; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
            <h4 style='color: #2c5282; margin-top: 0;'>🎯 核心幹部</h4>
            <div style='line-height: 2;'>
                <p><strong>會長：</strong>待更新</p>
                <p><strong>副會長：</strong>待更新</p>
                <p><strong>秘書：</strong>待更新</p>
                <p><strong>財務：</strong>待更新</p>
            </div>
        </div>
        
        <div style='background-color: #f0fff4; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #22543d; margin-top: 0;'>📋 大安組</h4>
            <div style='line-height: 2;'>
                <p><strong>組長：</strong>待更新</p>
                <p><strong>副組長：</strong>待更新</p>
                <p><strong>成員數：</strong>約 XX 人</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style='background-color: #fffaf0; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
            <h4 style='color: #744210; margin-top: 0;'>📋 溫安組</h4>
            <div style='line-height: 2;'>
                <p><strong>組長：</strong>待更新</p>
                <p><strong>副組長：</strong>待更新</p>
                <p><strong>成員數：</strong>約 XX 人</p>
            </div>
        </div>
        
        <div style='background-color: #fff5f7; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #742a2a; margin-top: 0;'>📋 木柵組</h4>
            <div style='line-height: 2;'>
                <p><strong>組長：</strong>待更新</p>
                <p><strong>副組長：</strong>待更新</p>
                <p><strong>成員數：</strong>約 XX 人</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div style='background-color: #f9f0ff; padding: 20px; border-radius: 10px; margin-top: 15px;'>
        <h4 style='color: #44337a; margin-top: 0;'>📋 文化組</h4>
        <div style='line-height: 2;'>
            <p><strong>組長：</strong>待更新</p>
            <p><strong>副組長：</strong>待更新</p>
            <p><strong>成員數：</strong>約 XX 人</p>
            <p><strong>負責事項：</strong>避靜、講座、出版品等文化活動</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.info("💡 詳細幹部名單與聯絡方式，請洽各組組長或分會秘書")

with tab3:
    st.subheader("2024年（113年）活動回顧")

    col1, col2 = st.columns(2)

    activities_2024 = [
        {"month": "1月", "event": "胡淑琴修女演講", "date": "01/21", "icon": "📖"},
        {"month": "2月", "event": "春節頤福園拜年", "date": "02/12", "icon": "🧧"},
        {"month": "2月", "event": "新春談小會未來", "date": "02/18", "icon": "🎊"},
        {"month": "3月", "event": "四旬期避靜", "date": "03月", "icon": "🙏"},
        {"month": "4月", "event": "吳伯仁神父座談會", "date": "04/14", "icon": "💬"},
        {"month": "6月", "event": "天使教堂朝聖之旅", "date": "06/29", "icon": "⛪"},
        {
            "month": "7月",
            "event": "芯媒體鍾瑪竇弟兄講座",
            "date": "07/20",
            "icon": "🎬",
        },
        {
            "month": "8月",
            "event": "好好愛自己-陳惠姿演講",
            "date": "08/18",
            "icon": "💪",
        },
        {
            "month": "9月",
            "event": "雷煥章神父逝世14周年追思",
            "date": "09/08",
            "icon": "🕯️",
        },
        {"month": "10月", "event": "共融營 - 台北分會", "date": "10月", "icon": "⛺"},
        {
            "month": "11月",
            "event": "大德蘭與超越性自我實現",
            "date": "11月",
            "icon": "📚",
        },
        {"month": "12月", "event": "聖誕月會暨補奉獻", "date": "12/17", "icon": "🎄"},
    ]

    for idx, activity in enumerate(activities_2024):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(
                f"""
            <div style='background-color: #f7fafc; padding: 15px; border-radius: 8px; 
                        margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.08);'>
                <div style='display: flex; align-items: center; margin-bottom: 8px;'>
                    <span style='font-size: 2em; margin-right: 12px;'>{activity['icon']}</span>
                    <span style='background-color: #667eea; color: white; padding: 4px 12px; 
                                 border-radius: 12px; font-size: 0.85em; font-weight: bold;'>
                        {activity['month']}
                    </span>
                </div>
                <h4 style='color: #2d3748; margin: 8px 0; font-size: 1.05em;'>{activity['event']}</h4>
                <p style='color: #718096; margin: 0; font-size: 0.85em;'>📅 {activity['date']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.success("✅ 2024年共舉辦12場主要活動，涵蓋靈修、朝聖、講座、追思等多元類型")

with tab4:
    st.subheader("活動提醒與參與須知")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        ### 📢 報名方式
        
        <div style='background-color: #f0fff4; padding: 15px; border-radius: 8px; margin-top: 10px;'>
            <p><strong>1. 月會活動</strong></p>
            <ul>
                <li>固定活動無需報名</li>
                <li>自由參加，歡迎攜伴</li>
            </ul>
            
            <p><strong>2. 特別活動</strong></p>
            <ul>
                <li>需事前報名</li>
                <li>注意報名截止日期</li>
                <li>朝聖活動請提前準備</li>
            </ul>
            
            <p><strong>3. 聯絡方式</strong></p>
            <ul>
                <li>透過分會負責人</li>
                <li>各小組組長</li>
                <li>關注月會通知</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        ### 🎯 活動類型說明
        
        <div style='background-color: #fffaf0; padding: 15px; border-radius: 8px; margin-top: 10px;'>
            <p><strong>🙏 避靜活動</strong><br>
            深度靈修體驗，通常為期1-3天</p>
            
            <p><strong>⛪ 朝聖之旅</strong><br>
            參訪聖地，結合信仰與交流</p>
            
            <p><strong>📖 講座分享</strong><br>
            邀請講師分享信仰與生活智慧</p>
            
            <p><strong>🎉 慶典活動</strong><br>
            會慶、聖誕等重要節日慶祝</p>
            
            <p><strong>🕯️ 追思禮儀</strong><br>
            紀念已亡會員與神長</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        ### 💡 參與小提醒
        
        <div style='background-color: #ebf8ff; padding: 15px; border-radius: 8px; margin-top: 10px;'>
            <p><strong>✅ 出席前</strong></p>
            <ul>
                <li>確認活動時間與地點</li>
                <li>了解活動主題與講師</li>
                <li>做好心靈準備</li>
            </ul>
            
            <p><strong>✅ 參與時</strong></p>
            <ul>
                <li>準時出席</li>
                <li>積極參與互動</li>
                <li>尊重講師與其他會員</li>
            </ul>
            
            <p><strong>✅ 活動後</strong></p>
            <ul>
                <li>與組員分享心得</li>
                <li>實踐所學所得</li>
                <li>邀請新朋友參加</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        ### 🤝 共融理念
        
        <div style='background-color: #fff5f7; padding: 15px; border-radius: 8px; margin-top: 10px;'>
            <p style='font-style: italic; color: #c53030; line-height: 1.8;'>
                「每個會員的出席是凝聚團體動力的最好方式。越少參加活動的會員越需要大家鼓勵。
                我們希望活動安排能符合大家在信仰福傳及靈修上實質的需要，<strong>願意參與才是最重要的</strong>。」
            </p>
            <p style='text-align: right; margin-top: 15px; color: #c53030;'>
                主祐平安！
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # 聯絡資訊
    st.markdown(
        """
    <div style='background-color: #f7fafc; padding: 20px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #2d3748; margin-top: 0;'>📞 需要更多資訊？</h4>
        <p style='color: #718096; margin-bottom: 0;'>
            請聯繫您的小組組長或分會負責人<br>
            我們隨時歡迎您的參與和建議！
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 頁尾返回按鈕
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("↩️ 返回行事曆總覽", use_container_width=True):
        st.switch_page("pages/calendar.py")
