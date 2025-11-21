"""
總會行事曆頁面
展示總會的年度工作行事曆、青壯組活動和服務協調角色
"""

import streamlit as st
from utils.utils import init_page
from datetime import datetime

# 初始化頁面設定
init_page(page_name="calendar_head_office")

st.title("總會行事曆")

# 總會角色說明區塊
st.markdown(
    """
<div style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
            padding: 25px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #f59e0b;'>
    <h3 style='color: #78350f; margin-top: 0;'>🏛️ 總會服務角色</h3>
    <div style='font-size: 1.15em; line-height: 2; color: #78350f;'>
        <p style='margin: 10px 0;'><strong>📍 核心任務：</strong>協調各分會、推動整體發展、服務全體會員</p>
        <p style='margin: 10px 0;'><strong>🎯 2025年度主題：</strong>靈修、福傳、共融、傳承</p>
        <p style='margin: 10px 0;'><strong>📋 主要工作：</strong>幹事會 2次 | 研發組 4次 | 陶成組 8次 | 共融營 2次</p>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# 使用 tabs 來組織內容
tab1, tab2, tab3, tab4 = st.tabs(
    ["📅 2025年行事曆", "📋 總會工作行事曆", "👨‍👩‍👧‍👦 青壯組行事曆", "💡 活動說明"]
)

with tab1:
    st.subheader("2025年總會重點活動")

    # 年度主題橫幅
    st.markdown(
        """
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; margin-bottom: 25px; text-align: center;'>
        <h2 style='color: white; margin: 0; font-size: 1.8em;'>🎯 2025年度主題</h2>
        <h3 style='color: #ffd700; margin: 10px 0; font-size: 1.5em;'>靈修 • 福傳 • 共融 • 傳承</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 第一季
    st.markdown("### 🌸 第一季（1-3月）")

    q1_events = [
        {
            "date": "2/28 (五)",
            "event": "參贊會（線上）",
            "type": "會議",
            "icon": "💼",
            "color": "#fff7ed",
        },
        {
            "date": "3/6 (四)",
            "event": "聯合陶成組預備會議（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "3/17 (一)",
            "event": "第三次會員手冊修訂委員會會議（線上）",
            "type": "委員會",
            "icon": "📝",
            "color": "#f5f3ff",
        },
        {
            "date": "3/21~23 (五-日)",
            "event": "青壯組共識營（台東）",
            "type": "共融營",
            "icon": "⛺",
            "color": "#ecfdf5",
        },
    ]

    for event in q1_events:
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; 
                    margin-bottom: 12px; border-left: 4px solid #f59e0b;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; 
                                font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                                 color: #78350f; padding: 4px 10px; border-radius: 10px; font-size: 0.8em; font-weight: bold;'>
                        {event['type']}
                    </span>
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
            "date": "4/10 (四)",
            "event": "第一次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "4/15 (二)",
            "event": "第四次會員手冊修訂委員會會議（線上）",
            "type": "委員會",
            "icon": "📝",
            "color": "#f5f3ff",
        },
        {
            "date": "4/30 (三)",
            "event": "103期心泉截稿",
            "type": "出版",
            "icon": "✍️",
            "color": "#fef3c7",
        },
        {
            "date": "5/6 (二)",
            "event": "第五次會員手冊修訂委員會會議",
            "type": "委員會",
            "icon": "📝",
            "color": "#f5f3ff",
        },
        {
            "date": "5/8 (四)",
            "event": "第二次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "6/12 (四)",
            "event": "第三次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
    ]

    for event in q2_events:
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; 
                    margin-bottom: 12px; border-left: 4px solid #f59e0b;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; 
                                font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                                 color: #78350f; padding: 4px 10px; border-radius: 10px; font-size: 0.8em; font-weight: bold;'>
                        {event['type']}
                    </span>
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
            "date": "7/8 (二)",
            "event": "幹事會",
            "type": "幹事會",
            "icon": "🏛️",
            "color": "#fff7ed",
        },
        {
            "date": "7/10 (四)",
            "event": "第四次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "8/7 (四)",
            "event": "第五次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "8/23 (六)",
            "event": "參贊參議會（台北長安堂）",
            "type": "會議",
            "icon": "💼",
            "color": "#fff7ed",
        },
        {
            "date": "9/11 (四)",
            "event": "第六次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
    ]

    for event in q3_events:
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; 
                    margin-bottom: 12px; border-left: 4px solid #f59e0b;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; 
                                font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                                 color: #78350f; padding: 4px 10px; border-radius: 10px; font-size: 0.8em; font-weight: bold;'>
                        {event['type']}
                    </span>
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
            "date": "10/3~5 (五-日)",
            "event": "總會共融營（台中聖愛山莊）",
            "type": "共融營",
            "icon": "⛺",
            "color": "#ecfdf5",
        },
        {
            "date": "10/9 (四)",
            "event": "第七次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "10/10 (五)",
            "event": "103期心泉出刊",
            "type": "出版",
            "icon": "📖",
            "color": "#fef3c7",
        },
        {
            "date": "11/6 (四)",
            "event": "第八次聯合陶成組（線上）",
            "type": "陶成",
            "icon": "📚",
            "color": "#f0f9ff",
        },
        {
            "date": "12/9 (二)",
            "event": "幹事會",
            "type": "幹事會",
            "icon": "🏛️",
            "color": "#fff7ed",
        },
    ]

    for event in q4_events:
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 15px; border-radius: 8px; 
                    margin-bottom: 12px; border-left: 4px solid #f59e0b;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 1.8em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.1em; color: #2d3748;'>{event['event']}</strong>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 6px 14px; border-radius: 15px; 
                                font-size: 0.85em; color: #2d3748; font-weight: bold; margin-bottom: 5px;'>
                        {event['date']}
                    </div>
                    <span style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                                 color: #78350f; padding: 4px 10px; border-radius: 10px; font-size: 0.8em; font-weight: bold;'>
                        {event['type']}
                    </span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div style='background-color: #fffbeb; padding: 15px; border-radius: 8px; margin-top: 20px;'>
        <p style='margin: 0; color: #78350f; font-size: 0.95em;'>
            <strong>📌 注意：</strong>線上會議將透過 Zoom 或 Google Meet 進行，會議連結將於活動前發送。<br>
            實體活動請留意各分會通知，共融營等大型活動將提前發布報名資訊。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with tab2:
    st.subheader("2025年總會工作行事曆")

    st.markdown(
        """
    <div style='background-color: #fffbeb; padding: 20px; border-radius: 10px; margin-bottom: 20px; 
                border-left: 5px solid #f59e0b;'>
        <h4 style='color: #78350f; margin-top: 0;'>📊 2025年總會工作統計</h4>
        <div style='line-height: 2; color: #78350f;'>
            <p style='margin: 10px 0;'><strong>🏛️ 幹事會：</strong>2次（7月、12月）</p>
            <p style='margin: 10px 0;'><strong>🔬 研發組：</strong>4次（2月、4月、5月、8月）</p>
            <p style='margin: 10px 0;'><strong>📚 陶成組：</strong>8次（4-11月，每月一次）</p>
            <p style='margin: 10px 0;'><strong>⛺ 共融營：</strong>2次（3月青壯組、10月總會）</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 完整行事曆表格
    st.markdown("#### 📅 完整工作行事曆")

    st.markdown(
        """
    <div style='background-color: #f7fafc; padding: 20px; border-radius: 10px; margin-bottom: 20px; overflow-x: auto;'>
        <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);'>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd; color: #78350f;'>日期</th>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd; color: #78350f;'>星期</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd; color: #78350f;'>活動名稱</th>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd; color: #78350f;'>類別</th>
                    <th style='padding: 12px; text-align: center; border: 1px solid #ddd; color: #78350f;'>形式</th>
                </tr>
            </thead>
            <tbody>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>2/11</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W2</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第一次研發組會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dbeafe; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>研發組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>2/28</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W5</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>參贊會</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fef3c7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>會議</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>3/6</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>聯合陶成組預備會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>3/17</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W1</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第三次會員手冊修訂委員會會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #f3e8ff; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>委員會</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>3/21-23</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>五-日</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>青壯組共識營（台東）</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fce7f3; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>共融營</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>4/10</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第一次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>4/12</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W6</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第二次研發組會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dbeafe; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>研發組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>4/15</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W2</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第四次會員手冊修訂委員會會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #f3e8ff; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>委員會</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>4/30</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W3</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>103期心泉截稿</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fed7aa; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>出版</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>-</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>5/6</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W2</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第五次會員手冊修訂委員會會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #f3e8ff; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>委員會</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>5/8</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第二次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>5/29</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W6</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第三次研發組會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dbeafe; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>研發組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>6/12</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第三次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>7/8</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W2</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'><strong>幹事會</strong></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fef3c7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold;'>幹事會</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>7/10</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第四次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>8/2</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W6</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第四次研發組會議</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dbeafe; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>研發組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>8/7</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第五次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>8/23</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W6</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>參贊參議會（台北長安堂）</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fef3c7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>會議</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>9/11</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第六次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>10/3-5</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>五-日</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'><strong>總會共融營（台中聖愛山莊）</strong></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fce7f3; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold;'>共融營</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>10/9</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第七次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>10/10</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>五</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>103期心泉出刊</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fed7aa; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>出版</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>-</td>
                </tr>
                <tr style='background-color: #ffffff;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>11/6</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W4</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'>第八次聯合陶成組</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #dcfce7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em;'>陶成組</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>線上</td>
                </tr>
                <tr style='background-color: #fffbeb;'>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>12/9</td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>W2</td>
                    <td style='padding: 10px; border: 1px solid #ddd;'><strong>幹事會</strong></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'><span style='background-color: #fef3c7; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold;'>幹事會</span></td>
                    <td style='padding: 10px; text-align: center; border: 1px solid #ddd;'>實體</td>
                </tr>
            </tbody>
        </table>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.info(
        "💡 **W2/W4/W6** 表示該月份的第幾週。線上會議將透過 Zoom 或 Google Meet 進行。"
    )

with tab3:
    st.subheader("2025年青壯組行事曆")

    # 青壯組核心價值
    st.markdown(
        """
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; margin-bottom: 25px; text-align: center;'>
        <h3 style='color: white; margin: 0; font-size: 1.5em;'>💪 青壯組核心價值</h3>
        <h2 style='color: #ffd700; margin: 10px 0; font-size: 1.8em;'>生命有限，幫助更多的人</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 青壯組活動列表
    youth_events = [
        {
            "date": "3/15 (六)",
            "event": "青年門徒聚會",
            "location": "台中秋山堂~美術館餐廳",
            "icon": "👥",
            "color": "#f0f9ff",
        },
        {
            "date": "3/16 (日)",
            "event": "台北長安堂與台北、北美小會共融",
            "location": "台北長安堂",
            "icon": "🤝",
            "color": "#f5f3ff",
        },
        {
            "date": "3/21-23 (五-日)",
            "event": "台東青年共融營",
            "location": "台東",
            "icon": "⛺",
            "color": "#ecfdf5",
        },
        {
            "date": "4月",
            "event": "四旬期街友關懷服務工作",
            "location": "待定",
            "icon": "❤️",
            "color": "#fef3c7",
        },
        {
            "date": "6月",
            "event": "參觀新勤美術館",
            "location": "台中",
            "icon": "🎨",
            "color": "#fff7ed",
        },
        {
            "date": "8月",
            "event": "陳潔分享工作甘苦談",
            "location": "同步 ZOOM 線上",
            "icon": "💼",
            "color": "#f0f9ff",
        },
        {
            "date": "10月",
            "event": "台中蘇主教與青年交談",
            "location": "同步 ZOOM 線上",
            "icon": "⛪",
            "color": "#f5f3ff",
        },
        {
            "date": "12月",
            "event": "慶祝聖誕節，分享愛做公益",
            "location": "待定",
            "icon": "🎄",
            "color": "#fce7f3",
        },
    ]

    for event in youth_events:
        st.markdown(
            f"""
        <div style='background-color: {event['color']}; padding: 18px; border-radius: 8px; 
                    margin-bottom: 15px; border-left: 4px solid #8b5cf6; box-shadow: 0 2px 4px rgba(0,0,0,0.08);'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='flex: 1;'>
                    <span style='font-size: 2em; margin-right: 12px;'>{event['icon']}</span>
                    <strong style='font-size: 1.15em; color: #2d3748;'>{event['event']}</strong>
                    <div style='color: #718096; font-size: 0.9em; margin-top: 8px;'>📍 {event['location']}</div>
                </div>
                <div style='text-align: right;'>
                    <div style='background-color: white; padding: 8px 16px; border-radius: 15px; 
                                font-size: 0.9em; color: #2d3748; font-weight: bold;'>
                        {event['date']}
                    </div>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # 青壯組特色說明
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div style='background-color: #f0fdf4; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #166534; margin-top: 0;'>🎯 活動特色</h4>
            <ul style='line-height: 2; color: #166534;'>
                <li><strong>靈修成長：</strong>門徒聚會、主教交談</li>
                <li><strong>社會關懷：</strong>街友服務、公益活動</li>
                <li><strong>文化體驗：</strong>美術館參訪、藝文交流</li>
                <li><strong>共融交流：</strong>跨分會共融、青年營隊</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #78350f; margin-top: 0;'>💡 參與方式</h4>
            <ul style='line-height: 2; color: #78350f;'>
                <li><strong>對象：</strong>45歲以下青年會員</li>
                <li><strong>彈性參與：</strong>依個人時間自由參加</li>
                <li><strong>線上同步：</strong>部分活動提供線上參與</li>
                <li><strong>新朋友：</strong>歡迎邀請朋友一同參加</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.success(
        "✨ 青壯組致力於培育年輕世代的信仰生活，透過多元活動實踐「生命有限，幫助更多的人」的核心價值"
    )

with tab4:
    st.subheader("總會角色與活動說明")

    # 總會角色
    st.markdown("### 🏛️ 總會的角色與功能")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div style='background-color: #fff7ed; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
            <h4 style='color: #c2410c; margin-top: 0;'>📍 核心職能</h4>
            <ul style='line-height: 2; color: #c2410c;'>
                <li><strong>協調服務：</strong>統籌各分會運作與交流</li>
                <li><strong>政策制定：</strong>研發小會整體發展方向</li>
                <li><strong>陶成培育：</strong>推動會員靈修與成長</li>
                <li><strong>資源整合：</strong>管理小會共同資源</li>
            </ul>
        </div>
        
        <div style='background-color: #f0f9ff; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #075985; margin-top: 0;'>🔬 研發組</h4>
            <p style='line-height: 1.8; color: #075985;'>
                負責小會政策研究、發展規劃、會員手冊修訂等工作，
                確保小會與時俱進，符合現代會員需求。
            </p>
            <p style='margin: 10px 0; color: #075985;'><strong>2025年重點：</strong></p>
            <ul style='color: #075985;'>
                <li>會員手冊全面修訂</li>
                <li>小會發展策略研擬</li>
                <li>跨分會交流機制</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style='background-color: #ecfdf5; padding: 20px; border-radius: 10px; margin-bottom: 15px;'>
            <h4 style='color: #065f46; margin-top: 0;'>📚 聯合陶成組</h4>
            <p style='line-height: 1.8; color: #065f46;'>
                <strong>目的：</strong>透過定期聚會，深化會員靈修生活，
                培養信仰默觀與實踐能力，促進靈性成長。
            </p>
            <p style='margin: 10px 0; color: #065f46;'><strong>2025年運作：</strong></p>
            <ul style='color: #065f46;'>
                <li>每月一次線上聚會（共8次）</li>
                <li>主題式靈修分享</li>
                <li>跨分會經驗交流</li>
                <li>個人靈修指導</li>
            </ul>
        </div>
        
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #78350f; margin-top: 0;'>🏛️ 幹事會</h4>
            <p style='line-height: 1.8; color: #78350f;'>
                總會最高決策單位，由各分會會長、總會幹部組成，
                負責重大事項決策、年度計畫審議等。
            </p>
            <p style='margin: 10px 0; color: #78350f;'><strong>2025年召開：</strong></p>
            <ul style='color: #78350f;'>
                <li>7月：上半年檢討與下半年規劃</li>
                <li>12月：年度總結與次年計畫</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # 心泉期刊
    st.markdown("### 📖 心泉期刊")

    st.markdown(
        """
    <div style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                padding: 25px; border-radius: 10px; margin-bottom: 20px;'>
        <h4 style='color: #78350f; margin-top: 0;'>✍️ 關於心泉</h4>
        <p style='line-height: 1.8; color: #78350f; font-size: 1.05em;'>
            《心泉》是天主教中華基督神修小會的官方期刊，每年出刊一期（103期預定2025年10月10日出刊）。
            期刊內容涵蓋靈修文章、會員分享、活動報導等，是小會重要的文字福傳與靈修陶成工具。
        </p>
        <div style='background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 8px; margin-top: 15px;'>
            <p style='margin: 8px 0; color: #78350f;'><strong>📅 103期時程：</strong></p>
            <ul style='color: #78350f; margin-top: 10px;'>
                <li><strong>截稿日期：</strong>2025年4月30日</li>
                <li><strong>出刊日期：</strong>2025年10月10日</li>
                <li><strong>徵稿對象：</strong>全體會員</li>
                <li><strong>稿件類型：</strong>靈修心得、信仰見證、活動報導、藝文創作</li>
            </ul>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 共融營說明
    st.markdown("### ⛺ 共融營")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div style='background-color: #fce7f3; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #9f1239; margin-top: 0;'>👨‍👩‍👧‍👦 青壯組共融營</h4>
            <p style='line-height: 1.8; color: #9f1239;'>
                <strong>日期：</strong>3/21-23（五-日）<br>
                <strong>地點：</strong>台東<br>
                <strong>對象：</strong>45歲以下青年會員<br>
                <strong>主題：</strong>青年門徒培育與共融
            </p>
            <p style='margin-top: 15px; color: #9f1239;'>
                <strong>特色：</strong>深度信仰交流、戶外活動、
                團體建立、青年領袖培育
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #3730a3; margin-top: 0;'>🏛️ 總會共融營</h4>
            <p style='line-height: 1.8; color: #3730a3;'>
                <strong>日期：</strong>10/3-5（五-日）<br>
                <strong>地點：</strong>台中聖愛山莊<br>
                <strong>對象：</strong>全體會員<br>
                <strong>主題：</strong>年度主題深化與全體共融
            </p>
            <p style='margin-top: 15px; color: #3730a3;'>
                <strong>特色：</strong>跨分會交流、靈修避靜、
                年度檢討、未來展望
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # 參與方式
    st.markdown(
        """
    <div style='background-color: #f7fafc; padding: 20px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #2d3748; margin-top: 0;'>🤝 如何參與總會活動</h4>
        <p style='color: #718096; line-height: 1.8; margin-bottom: 15px;'>
            總會活動以各分會會長、幹部為主要參與對象，但陶成組、共融營等活動歡迎全體會員參加。<br>
            詳細資訊將透過各分會發布，或關注《心泉》期刊與總會通知。
        </p>
        <p style='color: #4299e1; font-weight: bold;'>
            有任何問題，歡迎聯繫您所屬分會會長或總會秘書
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
