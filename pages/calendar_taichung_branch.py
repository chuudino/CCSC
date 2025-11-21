import streamlit as st
from utils import init_page

init_page(page_name="calendar_taichung_branch")  # 初始化頁面設定並設置對應的 page_name

st.title("台中分會行事曆")

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/calendar.py")

# 年度主題
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);'>
        <h2 style='color: white; text-align: center; margin: 0; font-size: 28px;'>114年度主題</h2>
        <p style='color: white; text-align: center; font-size: 24px; margin: 10px 0 0 0; font-weight: bold; letter-spacing: 8px;'>
            靈修 • 福傳 • 共融 • 傳承
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

# 建立分頁
tab1, tab2, tab3, tab4 = st.tabs(
    ["📅 2025年行事曆", "📋 114年度完整行事曆", "🎯 2024年回顧", "💡 活動提醒"]
)

with tab1:
    st.markdown("### 第一季 (1-3月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;'>
                <h4 style='color: #2E7D32; margin-top: 0;'>📖 1月5日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>錢玲珠老師分享</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>劉素梅</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
                <h4 style='color: #E65100; margin-top: 0;'>🎊 2月16日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>新春團拜</p>
                <p style='margin: 8px 0;'>閱讀心泉分享、氣功養生分享</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>雷成明</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E1F5FE; padding: 20px; border-radius: 10px; border-left: 5px solid #03A9F4;'>
                <h4 style='color: #01579B; margin-top: 0;'>🙏 3月28-30日 (五-日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>避靜</p>
                <p style='margin: 8px 0;'><strong>神師：</strong>吳伯仁神父</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>聖愛山莊</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>傅美華</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 第二季 (4-6月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FCE4EC; padding: 20px; border-radius: 10px; border-left: 5px solid #E91E63;'>
                <h4 style='color: #880E4F; margin-top: 0;'>🎨 4月27日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聖畫像</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>王端敏老師</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>張育英</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #F3E5F5; padding: 20px; border-radius: 10px; border-left: 5px solid #9C27B0;'>
                <h4 style='color: #4A148C; margin-top: 0;'>⛪ 5月17日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>淡水天主堂朝聖</p>
                <p style='margin: 8px 0;'>拜訪焦寶進、譚碧輝</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>淡水</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>陳瑞蘭</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E8EAF6; padding: 20px; border-radius: 10px; border-left: 5px solid #3F51B5;'>
                <h4 style='color: #1A237E; margin-top: 0;'>🎉 6月15日 (日) 10:50-12:00</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>會慶</p>
                <p style='margin: 8px 0;'>好好愛自己，迎接美好的未來</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>陳惠姿</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂 (與雙十堂合辦)</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>陳淑月</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 第三季 (7-9月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FFF9C4; padding: 20px; border-radius: 10px; border-left: 5px solid #FDD835;'>
                <h4 style='color: #F57F17; margin-top: 0;'>📚 7月20日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>讀書分享</p>
                <p style='margin: 8px 0;'>《在愛中成長》劉家正神父新書</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>黃瑞華</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFE0B2; padding: 20px; border-radius: 10px; border-left: 5px solid #FF6F00;'>
                <h4 style='color: #E65100; margin-top: 0;'>🏠 8月17日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>設計靜宜宿舍甘苦談</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>陳潔</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>陳潔家</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>巫郁玫</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E0F2F1; padding: 20px; border-radius: 10px; border-left: 5px solid #00897B;'>
                <h4 style='color: #004D40; margin-top: 0;'>🤖 9月21日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>AI課程研習</p>
                <p style='margin: 8px 0;'>參與上智活動</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>上智文教院</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>游照美</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 第四季 (10-12月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #F44336;'>
                <h4 style='color: #B71C1C; margin-top: 0;'>🤝 10月3-5日</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>共融營</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>聖愛山莊</p>
                <p style='margin: 8px 0;'><strong>參與：</strong>全體</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px; border-left: 5px solid #2196F3;'>
                <h4 style='color: #0D47A1; margin-top: 0;'>🌏 11月16日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>天人合一</p>
                <p style='margin: 8px 0;'>旅遊分享</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>何富寶</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>雙十堂</p>
                <p style='margin: 8px 0;'><strong>主持：</strong>蔡熙</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #F1F8E9; padding: 20px; border-radius: 10px; border-left: 5px solid #8BC34A;'>
                <h4 style='color: #33691E; margin-top: 0;'>🎄 12月21日 (日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聖誕Party</p>
                <p style='margin: 8px 0;'><strong>主辦：</strong>青年組</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>待定</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

with tab2:
    st.markdown("### 114年度台中分會完整行事曆")
    st.markdown("114.1 - 114.12")

    # 完整行事曆表格
    st.markdown(
        """
        <style>
            .calendar-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 15px;
                box-shadow: 0 2px 15px rgba(0,0,0,0.1);
                border-radius: 10px;
                overflow: hidden;
            }
            .calendar-table thead tr {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: left;
                font-weight: bold;
            }
            .calendar-table th,
            .calendar-table td {
                padding: 15px;
                border: 1px solid #ddd;
            }
            .calendar-table tbody tr {
                border-bottom: 1px solid #ddd;
                transition: background-color 0.3s;
            }
            .calendar-table tbody tr:nth-of-type(even) {
                background-color: #f8f9fa;
            }
            .calendar-table tbody tr:hover {
                background-color: #e9ecef;
            }
        </style>
        
        <table class="calendar-table">
            <thead>
                <tr>
                    <th style='width: 20%;'>日期</th>
                    <th style='width: 40%;'>活動內容</th>
                    <th style='width: 20%;'>地點</th>
                    <th style='width: 20%;'>主持人</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>114.1.5 (日)</td>
                    <td>錢玲珠老師分享</td>
                    <td>雙十堂</td>
                    <td>劉素梅</td>
                </tr>
                <tr>
                    <td>114.2.16 (日)</td>
                    <td>新春團拜 - 閱讀心泉分享、氣功養生分享</td>
                    <td>雙十堂</td>
                    <td>雷成明</td>
                </tr>
                <tr>
                    <td>114.3.28-3.30 (五-日)</td>
                    <td>避靜 (神師: 吳伯仁神父)</td>
                    <td>聖愛山莊</td>
                    <td>傅美華</td>
                </tr>
                <tr>
                    <td>114.4.27 (日)</td>
                    <td>邀請王端敏老師 - 聖畫像</td>
                    <td>雙十堂</td>
                    <td>張育英</td>
                </tr>
                <tr>
                    <td>114.5.17 (六)</td>
                    <td>淡水天主堂朝聖 - 拜訪焦寶進、譚碧輝</td>
                    <td>淡水</td>
                    <td>陳瑞蘭</td>
                </tr>
                <tr>
                    <td>114.6.15 (日) 10:50-12:00</td>
                    <td>會慶 — 陳惠姿 (好好愛自己，迎接美好的未來 — 與雙十堂合辦演講)</td>
                    <td>雙十堂</td>
                    <td>陳淑月</td>
                </tr>
                <tr>
                    <td>114.7.20 (日)</td>
                    <td>讀書分享 (在愛中成長) 劉家正神父新書</td>
                    <td>雙十堂</td>
                    <td>黃瑞華</td>
                </tr>
                <tr>
                    <td>114.8.17 (日)</td>
                    <td>設計靜宜宿舍甘苦談 (陳潔)</td>
                    <td>陳潔家</td>
                    <td>巫郁玫</td>
                </tr>
                <tr>
                    <td>114.9.21 (日)</td>
                    <td>AI課程研習 (參與上智活動)</td>
                    <td>上智文教院</td>
                    <td>游照美</td>
                </tr>
                <tr>
                    <td>114.10.3-10.5</td>
                    <td>共融營</td>
                    <td>聖愛山莊</td>
                    <td>全體</td>
                </tr>
                <tr>
                    <td>114.11.16 (日)</td>
                    <td>天人合一 旅遊分享 (何富寶)</td>
                    <td>雙十堂</td>
                    <td>蔡熙</td>
                </tr>
                <tr>
                    <td>114.12.21 (日)</td>
                    <td>聖誕Party</td>
                    <td>待定</td>
                    <td>青年組</td>
                </tr>
            </tbody>
        </table>
    """,
        unsafe_allow_html=True,
    )

    # 幹部名單
    st.markdown("---")
    st.markdown("### 114年度幹部名單")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #667eea; padding-bottom: 10px;'>主要幹部</h4>
                <p style='margin: 8px 0;'><strong>指導司鐸：</strong>吳伯仁神父</p>
                <p style='margin: 8px 0;'><strong>分會主席：</strong>傅美華</p>
                <p style='margin: 8px 0;'><strong>秘書加資訊：</strong>巫郁玫</p>
                <p style='margin: 8px 0;'><strong>參議：</strong>游照美</p>
                <p style='margin: 8px 0;'><strong>會計：</strong>黃瑞華</p>
                <p style='margin: 8px 0;'><strong>連絡：</strong>張育英</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #764ba2; padding-bottom: 10px;'>組別負責人</h4>
                <p style='margin: 8px 0;'><strong>靈修：</strong>劉素梅、蔡熙</p>
                <p style='margin: 8px 0;'><strong>康樂：</strong>郭良玉、何富寶</p>
                <p style='margin: 8px 0;'><strong>總務：</strong>陳瑞蘭</p>
                <p style='margin: 8px 0;'><strong>健康諮詢：</strong>雷成明、陳淑月</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("### 2024年活動回顧")

    st.info("📝 本頁面預留 2024年活動回顧內容，可於年底更新時補充相關照片與心得分享。")

    st.markdown(
        """
        <div style='background-color: #fff3cd; padding: 20px; border-radius: 10px; border-left: 5px solid #ffc107;'>
            <h4 style='color: #856404;'>2024年重點活動</h4>
            <ul style='color: #856404;'>
                <li>台中榮總醫護人員物資捐贈</li>
                <li>各項靈修培育活動</li>
                <li>教堂朝聖活動</li>
                <li>會員共融聚會</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

with tab4:
    st.markdown("### 活動參與提醒")

    st.success("✨ 歡迎所有會員踴躍參與台中分會各項活動！")

    st.markdown(
        """
        <div style='background-color: #e7f3ff; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #004085;'>📢 參與須知</h4>
            <ul style='color: #004085;'>
                <li>請提前報名，以便主辦單位安排</li>
                <li>若有任何問題，請聯繫該活動主持人</li>
                <li>部分活動需要車資或餐費，請留意通知</li>
                <li>歡迎攜帶家人朋友一同參加</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #d4edda; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #155724;'>🙏 靈修方向</h4>
            <p style='color: #155724;'>台中分會秉持「靈修、福傳、共融、傳承」的精神，透過多元化的活動設計，包括：</p>
            <ul style='color: #155724;'>
                <li><strong>靈修培育：</strong>避靜、讀書分享、祈禱聚會</li>
                <li><strong>福傳行動：</strong>朝聖、見證分享</li>
                <li><strong>共融聚會：</strong>團拜、聖誕Party、共融營</li>
                <li><strong>傳承使命：</strong>與青年組合作、新會員培育</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )
