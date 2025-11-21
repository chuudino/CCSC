import streamlit as st
from utils import init_page

init_page(
    page_name="calendar_northamerica_branch"
)  # 初始化頁面設定並設置對應的 page_name

st.title("北美分會行事曆")

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/calendar.py")

# 年度主題
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);'>
        <h2 style='color: white; text-align: center; margin: 0; font-size: 28px;'>2025年度主題</h2>
        <p style='color: white; text-align: center; font-size: 24px; margin: 10px 0 0 0; font-weight: bold; letter-spacing: 8px;'>
            默觀祈禱 • 神修溯源 • 線上共融
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

# 建立分頁
tab1, tab2, tab3, tab4 = st.tabs(
    ["📅 2025年行事曆", "📋 年度完整行事曆", "🌟 北美分會特色", "💡 活動提醒"]
)

with tab1:
    st.markdown("### 第一季 (1-3月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;'>
                <h4 style='color: #2E7D32; margin-top: 0;'>💬 1月2日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>中華天主教早期在地化及未來發展的觀察</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>古偉瀛</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
                <h4 style='color: #E65100; margin-top: 0;'>📖 1月23日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(八)</p>
                <p style='margin: 8px 0;'>使命的完成</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>陳著釧/高方寧</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E1F5FE; padding: 20px; border-radius: 10px; border-left: 5px solid #03A9F4;'>
                <h4 style='color: #01579B; margin-top: 0;'>💬 2月6日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>非暴力溝通</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>楊世弘</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FCE4EC; padding: 20px; border-radius: 10px; border-left: 5px solid #E91E63;'>
                <h4 style='color: #880E4F; margin-top: 0;'>📖 2月27日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(九)</p>
                <p style='margin: 8px 0;'>基督的精神—愛</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>吳懷瑜/王利華</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #F3E5F5; padding: 20px; border-radius: 10px; border-left: 5px solid #9C27B0;'>
                <h4 style='color: #4A148C; margin-top: 0;'>🙏 3月14日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>四旬期避靜講</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>任安道神父</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E8EAF6; padding: 20px; border-radius: 10px; border-left: 5px solid #3F51B5;'>
                <h4 style='color: #1A237E; margin-top: 0;'>📖 3月27日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十)</p>
                <p style='margin: 8px 0;'>實踐基督愛的精神</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>羅慧敏/賴經緯</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
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
            <div style='background-color: #FFF9C4; padding: 20px; border-radius: 10px; border-left: 5px solid #FDD835;'>
                <h4 style='color: #F57F17; margin-top: 0;'>💬 4月10日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>分享喜愛的書</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>北美小會會員</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFE0B2; padding: 20px; border-radius: 10px; border-left: 5px solid #FF6F00;'>
                <h4 style='color: #E65100; margin-top: 0;'>📖 4月24日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十一)</p>
                <p style='margin: 8px 0;'>我們生活態度的源泉—信仰</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>侯振中/葛寧意</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E0F2F1; padding: 20px; border-radius: 10px; border-left: 5px solid #00897B;'>
                <h4 style='color: #004D40; margin-top: 0;'>🎬 5月1日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>電影欣賞</p>
                <p style='margin: 8px 0;'><strong>主辦：</strong>工作室</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### ")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #F44336;'>
                <h4 style='color: #B71C1C; margin-top: 0;'>📖 5月22日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十二)</p>
                <p style='margin: 8px 0;'>超脫和喜樂</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>杜曉雲/徐琪</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px; border-left: 5px solid #2196F3;'>
                <h4 style='color: #0D47A1; margin-top: 0;'>🌸 6月5日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>花藝與詩詞</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>周文漣</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
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
            <div style='background-color: #F1F8E9; padding: 20px; border-radius: 10px; border-left: 5px solid #8BC34A;'>
                <h4 style='color: #33691E; margin-top: 0;'>📖 6月26日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十三)</p>
                <p style='margin: 8px 0;'>進取</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>陸蔚虹/鍾安娜</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFF9C4; padding: 20px; border-radius: 10px; border-left: 5px solid #FDD835;'>
                <h4 style='color: #F57F17; margin-top: 0;'>🥗 7月3日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>介紹健康營養餐</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>杜曉雲</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #FFE0B2; padding: 20px; border-radius: 10px; border-left: 5px solid #FF6F00;'>
                <h4 style='color: #E65100; margin-top: 0;'>📖 7月24日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十四)</p>
                <p style='margin: 8px 0;'>合作與服務</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>馮克芳/劉千惠</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #E0F2F1; padding: 20px; border-radius: 10px; border-left: 5px solid #00897B;'>
                <h4 style='color: #004D40; margin-top: 0;'>📜 8月7日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>中國詩詞欣賞</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>韓蒂月/杜曉峰/馮克芳</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #F44336;'>
                <h4 style='color: #B71C1C; margin-top: 0;'>📖 8月28日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十五)</p>
                <p style='margin: 8px 0;'>小會內的合作</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>顏慧怡/孫長安</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px; border-left: 5px solid #2196F3;'>
                <h4 style='color: #0D47A1; margin-top: 0;'>🖼️ 9月10日 (三)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>聖母圖像</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>徐明徳神父</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
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
            <div style='background-color: #F1F8E9; padding: 20px; border-radius: 10px; border-left: 5px solid #8BC34A;'>
                <h4 style='color: #33691E; margin-top: 0;'>🤖 10月2日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>人工智能學習</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>賴經緯</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFF9C4; padding: 20px; border-radius: 10px; border-left: 5px solid #FDD835;'>
                <h4 style='color: #F57F17; margin-top: 0;'>📖 10月23日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>神修溯源(十六)</p>
                <p style='margin: 8px 0;'>小會外的合作</p>
                <p style='margin: 8px 0;'><strong>帶領：</strong>葛寧意/王毅鳴</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #FFE0B2; padding: 20px; border-radius: 10px; border-left: 5px solid #FF6F00;'>
                <h4 style='color: #E65100; margin-top: 0;'>💬 11月6日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>小會初心</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>許建德</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### ")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='background-color: #E0F2F1; padding: 20px; border-radius: 10px; border-left: 5px solid #00897B;'>
                <h4 style='color: #004D40; margin-top: 0;'>🙏 12月4日 (四)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聊天室</p>
                <p style='margin: 8px 0;'>降臨期避靜講座</p>
                <p style='margin: 8px 0;'><strong>主講：</strong>任盤基神父</p>
                <p style='margin: 8px 0;'><strong>方式：</strong>線上進行</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

with tab2:
    st.markdown("### 2025年度北美分會完整行事曆")

    # 默觀祈禱說明
    st.markdown(
        """
        <div style='background-color: #e7f3ff; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #0288d1;'>
            <h4 style='color: #01579b;'>🙏 每日默觀祈禱</h4>
            <p style='color: #004085; margin: 10px 0;'><strong>時間：</strong>週一至週五 下午4:00 (美東時間)</p>
            <p style='color: #004085; margin: 10px 0;'><strong>帶領人員：</strong></p>
            <ul style='color: #004085;'>
                <li>週一：李秀萍</li>
                <li>週二：葛寧意</li>
                <li>週三：許建徳</li>
                <li>週四：馮克芳</li>
                <li>週五：孫愛珠</li>
            </ul>
            <p style='color: #004085; margin: 10px 0;'><strong>方式：</strong>線上進行</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 每月特別活動")

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
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
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
                    <th style='width: 15%;'>日期</th>
                    <th style='width: 20%;'>活動類型</th>
                    <th style='width: 40%;'>活動內容</th>
                    <th style='width: 25%;'>主講/帶領</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1/2 (四)</td>
                    <td>聊天室</td>
                    <td>中華天主教早期在地化及未來發展的觀察</td>
                    <td>古偉瀛</td>
                </tr>
                <tr>
                    <td>1/9 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>1/16 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>1/23 (四)</td>
                    <td>神修溯源(八)</td>
                    <td>使命的完成</td>
                    <td>陳著釧/高方寧</td>
                </tr>
                <tr>
                    <td>2/6 (四)</td>
                    <td>聊天室</td>
                    <td>非暴力溝通</td>
                    <td>楊世弘</td>
                </tr>
                <tr>
                    <td>2/27 (四)</td>
                    <td>神修溯源(九)</td>
                    <td>基督的精神—愛</td>
                    <td>吳懷瑜/王利華</td>
                </tr>
                <tr>
                    <td>3/7 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>3/14 (四)</td>
                    <td>聊天室</td>
                    <td>四旬期避靜講</td>
                    <td>任安道神父</td>
                </tr>
                <tr>
                    <td>3/21 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>3/27 (四)</td>
                    <td>神修溯源(十)</td>
                    <td>實踐基督愛的精神</td>
                    <td>羅慧敏/賴經緯</td>
                </tr>
                <tr>
                    <td>4/10 (四)</td>
                    <td>聊天室</td>
                    <td>分享喜愛的書</td>
                    <td>北美小會會員</td>
                </tr>
                <tr>
                    <td>4/24 (四)</td>
                    <td>神修溯源(十一)</td>
                    <td>我們生活態度的源泉—信仰</td>
                    <td>侯振中/葛寧意</td>
                </tr>
                <tr>
                    <td>5/1 (四)</td>
                    <td>聊天室</td>
                    <td>電影欣賞</td>
                    <td>工作室</td>
                </tr>
                <tr>
                    <td>5/8 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>5/15 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>5/22 (四)</td>
                    <td>神修溯源(十二)</td>
                    <td>超脫和喜樂</td>
                    <td>杜曉雲/徐琪</td>
                </tr>
                <tr>
                    <td>6/5 (四)</td>
                    <td>聊天室</td>
                    <td>花藝與詩詞</td>
                    <td>周文漣</td>
                </tr>
                <tr>
                    <td>6/26 (四)</td>
                    <td>神修溯源(十三)</td>
                    <td>進取</td>
                    <td>陸蔚虹/鍾安娜</td>
                </tr>
                <tr>
                    <td>7/3 (四)</td>
                    <td>聊天室</td>
                    <td>介紹健康營養餐</td>
                    <td>杜曉雲</td>
                </tr>
                <tr>
                    <td>7/10 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>7/17 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>7/24 (四)</td>
                    <td>神修溯源(十四)</td>
                    <td>合作與服務</td>
                    <td>馮克芳/劉千惠</td>
                </tr>
                <tr>
                    <td>8/7 (四)</td>
                    <td>聊天室</td>
                    <td>中國詩詞欣賞</td>
                    <td>韓蒂月/杜曉峰/馮克芳</td>
                </tr>
                <tr>
                    <td>8/28 (四)</td>
                    <td>神修溯源(十五)</td>
                    <td>小會內的合作</td>
                    <td>顏慧怡/孫長安</td>
                </tr>
                <tr>
                    <td>9/4 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>9/10 (三)</td>
                    <td>聊天室</td>
                    <td>聖母圖像</td>
                    <td>徐明徳神父</td>
                </tr>
                <tr>
                    <td>9/18 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>10/2 (四)</td>
                    <td>聊天室</td>
                    <td>人工智能學習</td>
                    <td>賴經緯</td>
                </tr>
                <tr>
                    <td>10/23 (四)</td>
                    <td>神修溯源(十六)</td>
                    <td>小會外的合作</td>
                    <td>葛寧意/王毅鳴</td>
                </tr>
                <tr>
                    <td>11/6 (四)</td>
                    <td>聊天室</td>
                    <td>小會初心</td>
                    <td>許建德</td>
                </tr>
                <tr>
                    <td>11/13 (四)</td>
                    <td>工作室會議</td>
                    <td>工作室會議</td>
                    <td>趙世熙</td>
                </tr>
                <tr>
                    <td>11/20 (四)</td>
                    <td>公念玫瑰經</td>
                    <td>公念玫瑰經</td>
                    <td>王利華</td>
                </tr>
                <tr>
                    <td>12/4 (四)</td>
                    <td>聊天室</td>
                    <td>降臨期避靜講座</td>
                    <td>任盤基神父</td>
                </tr>
            </tbody>
        </table>
    """,
        unsafe_allow_html=True,
    )

with tab3:
    st.markdown("### 北美分會特色")

    st.markdown(
        """
        <div style='background-color: #e8f4f8; padding: 25px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #0288d1;'>
            <h4 style='color: #01579b;'>🌐 線上聚會模式</h4>
            <p style='color: #004085;'>北美分會因應疫情後的新常態，所有活動均採用線上進行的方式。這讓散居北美各地的會員們能夠突破地理限制，持續保持緊密的靈修共融。</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #fff3e0; padding: 25px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #f57c00;'>
            <h4 style='color: #e65100;'>🙏 每日默觀祈禱</h4>
            <p style='color: #bf360c;'>北美分會最具特色的活動是每週一至週五下午4:00（美東時間）的默觀祈禱。由五位會員輪流帶領，形成穩定的靈修節奏，幫助會員在忙碌的生活中保持與主的連結。</p>
            <ul style='color: #bf360c;'>
                <li><strong>週一：</strong>李秀萍</li>
                <li><strong>週二：</strong>葛寧意</li>
                <li><strong>週三：</strong>許建徳</li>
                <li><strong>週四：</strong>馮克芳</li>
                <li><strong>週五：</strong>孫愛珠</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #f3e5f5; padding: 25px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #7b1fa2;'>
            <h4 style='color: #4a148c;'>📖 神修溯源系列</h4>
            <p style='color: #4a148c;'>2025年度持續進行神修溯源系列研讀，從第八講到第十六講，系統性地探討基督神修小會的核心精神：</p>
            <ul style='color: #4a148c;'>
                <li>使命的完成</li>
                <li>基督的精神—愛</li>
                <li>實踐基督愛的精神</li>
                <li>信仰、超脫和喜樂</li>
                <li>進取、合作與服務</li>
                <li>小會內外的合作</li>
            </ul>
            <p style='color: #4a148c;'>每次由兩位會員共同帶領，促進深度交流與學習。</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #e8f5e9; padding: 25px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #388e3c;'>
            <h4 style='color: #1b5e20;'>💬 多元化的聊天室活動</h4>
            <p style='color: #2e7d32;'>北美分會特別安排了豐富多元的聊天室主題，涵蓋：</p>
            <ul style='color: #2e7d32;'>
                <li><strong>信仰與靈修：</strong>四旬期避靜講、降臨期避靜講座、聖母圖像</li>
                <li><strong>文化與藝術：</strong>中國詩詞欣賞、花藝與詩詞</li>
                <li><strong>生活與成長：</strong>非暴力溝通、健康營養餐、人工智能學習</li>
                <li><strong>共融與分享：</strong>分享喜愛的書、電影欣賞、小會初心</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #fce4ec; padding: 25px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #c2185b;'>
            <h4 style='color: #880e4f;'>🎯 四個工作方向</h4>
            <p style='color: #ad1457;'>北美分會採用工作室模式，透過四個主要方向推動小會使命：</p>
            <ul style='color: #ad1457;'>
                <li><strong>靈修培育：</strong>默觀祈禱、神修溯源、公念玫瑰經</li>
                <li><strong>知識學習：</strong>各類聊天室主題分享</li>
                <li><strong>共融聯誼：</strong>線上聚會、經驗分享</li>
                <li><strong>服務傳承：</strong>工作室會議、經驗傳承</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

with tab4:
    st.markdown("### 活動參與提醒")

    st.success("✨ 歡迎所有北美地區的會員踴躍參與線上活動！")

    st.markdown(
        """
        <div style='background-color: #e7f3ff; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #004085;'>🌐 線上參與方式</h4>
            <ul style='color: #004085;'>
                <li><strong>平台：</strong>所有活動皆透過線上視訊平台進行</li>
                <li><strong>連結：</strong>活動前會透過電郵或通訊群組發送連結</li>
                <li><strong>設備：</strong>需要有網路連線的電腦、平板或手機</li>
                <li><strong>建議：</strong>使用耳機麥克風以獲得更好的通話品質</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #e65100;'>⏰ 時區說明</h4>
            <p style='color: #bf360c;'><strong>重要提醒：</strong>所有活動時間均為美東時間（ET）</p>
            <ul style='color: #bf360c;'>
                <li><strong>美東時間（ET）：</strong>下午4:00</li>
                <li><strong>美中時間（CT）：</strong>下午3:00</li>
                <li><strong>美山時間（MT）：</strong>下午2:00</li>
                <li><strong>美西時間（PT）：</strong>下午1:00</li>
                <li><strong>台灣時間：</strong>隔日凌晨4:00或5:00（視日光節約時間而定）</li>
            </ul>
            <p style='color: #bf360c;'>請會員們留意自己所在地的時區轉換，準時參與。</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #e8f5e9; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #2e7d32;'>📅 活動規律性</h4>
            <p style='color: #1b5e20;'>北美分會活動具有高度規律性，幫助會員養成穩定的靈修習慣：</p>
            <ul style='color: #1b5e20;'>
                <li><strong>每日默觀：</strong>週一至週五下午4:00（美東時間）</li>
                <li><strong>每月聚會：</strong>大部分特別活動安排在週四</li>
                <li><strong>神修溯源：</strong>約每月一次，系統性研讀</li>
                <li><strong>工作室會議：</strong>定期召開，協調各項事務</li>
                <li><strong>玫瑰經：</strong>定期公念，培養祈禱習慣</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #f3e5f5; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #4a148c;'>💡 參與建議</h4>
            <ul style='color: #6a1b9a;'>
                <li>建議提前5-10分鐘進入線上會議室，測試設備</li>
                <li>可將常態活動加入個人行事曆，建立提醒</li>
                <li>若無法參加，建議提前向帶領人告知</li>
                <li>歡迎邀請有興趣的朋友參與開放性活動</li>
                <li>鼓勵會員間多交流、多分享、多祈禱</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #fce4ec; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #880e4f;'>🙏 靈修方向</h4>
            <p style='color: #ad1457;'>北美分會透過線上平台，持續實踐基督神修小會的核心價值：</p>
            <ul style='color: #ad1457;'>
                <li><strong>默觀祈禱：</strong>每日與主相遇，培養內在生命</li>
                <li><strong>神修溯源：</strong>深入理解小會精神，紮根信仰</li>
                <li><strong>共融分享：</strong>跨越距離，建立信仰團體</li>
                <li><strong>服務見證：</strong>在生活中實踐基督的愛</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )
