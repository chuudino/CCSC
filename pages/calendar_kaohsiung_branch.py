import streamlit as st
from utils import init_page

init_page(page_name="calendar_kaohsiung_branch")  # 初始化頁面設定並設置對應的 page_name

st.title("高雄分會行事曆")

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/calendar.py")

# 年度主題
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);'>
        <h2 style='color: white; text-align: center; margin: 0; font-size: 28px;'>2025年度方向</h2>
        <p style='color: white; text-align: center; font-size: 24px; margin: 10px 0 0 0; font-weight: bold; letter-spacing: 6px;'>
            攜手同行 — 靈修 • 福傳 • 共融 • 傳承
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

# 建立分頁
tab1, tab2, tab3, tab4 = st.tabs(
    ["📅 2025年行事曆", "📋 年度完整行事曆", "📖 讀書會行事曆", "💡 活動提醒"]
)

with tab1:
    st.markdown("### 第一季 (1-3月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;'>
                <h4 style='color: #2E7D32; margin-top: 0;'>👥 1月11日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>北美共融營見聞</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>總會主席陳惠姿</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>聖家會</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>顏闓明</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
                <h4 style='color: #E65100; margin-top: 0;'>⛪ 2月15日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>步履神師，愛的旅程</p>
                <p style='margin: 8px 0;'>西法朝聖分享及生活分享</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>施麗華、林櫻枝</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>林櫻枝</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E1F5FE; padding: 20px; border-radius: 10px; border-left: 5px solid #03A9F4;'>
                <h4 style='color: #01579B; margin-top: 0;'>🙏 3月8日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>越有人性，越有神性</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>李碧圓修女</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>施麗華</p>
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
            <div style='background-color: #F3E5F5; padding: 20px; border-radius: 10px; border-left: 5px solid #9C27B0;'>
                <h4 style='color: #4A148C; margin-top: 0;'>🙏 3月28-30日 (五-日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>台中分會避靜</p>
                <p style='margin: 8px 0;'><strong>神師：</strong>吳伯仁神父</p>
                <p style='margin: 8px 0;'>高雄分會8人參加</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>太平聖愛山莊</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>施麗華</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FCE4EC; padding: 20px; border-radius: 10px; border-left: 5px solid #E91E63;'>
                <h4 style='color: #880E4F; margin-top: 0;'>📖 4月26日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>從德蘭的靈修談基督徒的培育</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>蔣範華修女</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>洪艷秋</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E8EAF6; padding: 20px; border-radius: 10px; border-left: 5px solid #3F51B5;'>
                <h4 style='color: #1A237E; margin-top: 0;'>✝️ 5月24日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>成聖</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>陳德光前輔大神學院院長</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>洪艷秋</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 第二季續 & 第三季 (6-9月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #FFF9C4; padding: 20px; border-radius: 10px; border-left: 5px solid #FDD835;'>
                <h4 style='color: #F57F17; margin-top: 0;'>⛪ 6月28日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>禧年、朝聖</p>
                <p style='margin: 8px 0;'><strong>講師：</strong>吳伯仁神父</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>林俊芳</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFE0B2; padding: 20px; border-radius: 10px; border-left: 5px solid #FF6F00;'>
                <h4 style='color: #E65100; margin-top: 0;'>💬 7月12日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>生活分享</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>廖金常修女</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>翁詩貞</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E0F2F1; padding: 20px; border-radius: 10px; border-left: 5px solid #00897B;'>
                <h4 style='color: #004D40; margin-top: 0;'>👨‍👩‍👧‍👦 8月9日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>與年輕人的對話</p>
                <p style='margin: 8px 0;'>新世代、新見識</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>廖玲玲</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 第三季續 & 第四季 (9-12月)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color: #F1F8E9; padding: 20px; border-radius: 10px; border-left: 5px solid #8BC34A;'>
                <h4 style='color: #33691E; margin-top: 0;'>💬 9月13日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>生活分享</p>
                <p style='margin: 8px 0;'><strong>分享：</strong>郭青青修女</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>洪碧玉</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #F44336;'>
                <h4 style='color: #B71C1C; margin-top: 0;'>🤝 10月3-5日 (五-日)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>小會年度共融營</p>
                <p style='margin: 8px 0;'><strong>營長：</strong>朱豐榮</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>台中太平聖愛山莊</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>施麗華</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px; border-left: 5px solid #2196F3;'>
                <h4 style='color: #0D47A1; margin-top: 0;'>📋 11月8日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>前瞻與回顧</p>
                <p style='margin: 8px 0;'>繼往開來，訂定新行事曆</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>救世主堂</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>施麗華</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown(
            """
            <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
                <h4 style='color: #E65100; margin-top: 0;'>🎄 12月27日 (六)</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>聖誕餐會 (第45次)</p>
                <p style='margin: 8px 0;'><strong>地點：</strong>待定</p>
                <p style='margin: 8px 0;'><strong>負責：</strong>劉文義</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;'>
                <h4 style='color: #2E7D32; margin-top: 0;'>⛪ 5月中旬</h4>
                <p style='margin: 8px 0;'><strong>主題：</strong>教堂一日遊</p>
                <p style='margin: 8px 0;'>前往台南、嘉義、雲林等地朝聖</p>
                <p style='margin: 8px 0;'><strong>說明：</strong>詳細日期待定</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

with tab2:
    st.markdown("### 2025年高雄分會完整行事曆")

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
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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
                    <th style='width: 45%;'>內容</th>
                    <th style='width: 18%;'>地點</th>
                    <th style='width: 17%;'>負責人</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>2025/01/11 (六)</td>
                    <td>總會主席陳惠姿分享北美共融營見聞</td>
                    <td>聖家會</td>
                    <td>顏闓明</td>
                </tr>
                <tr>
                    <td>2/15 (六)</td>
                    <td>邀請施麗華：「步履神師，愛的旅程」西法朝聖分享，及林櫻枝生活分享</td>
                    <td>救世主堂</td>
                    <td>林櫻枝</td>
                </tr>
                <tr>
                    <td>3/8 (六)</td>
                    <td>邀請李碧圓修女分享「越有人性，越有神性」</td>
                    <td>救世主堂</td>
                    <td>施麗華</td>
                </tr>
                <tr>
                    <td>3/28~30 (五~日)</td>
                    <td>台中分會避靜 (太平聖愛山莊) - 吳伯仁神父主講，高雄分會8人參加</td>
                    <td>聖愛山莊</td>
                    <td>施麗華</td>
                </tr>
                <tr>
                    <td>4/26 (六)</td>
                    <td>邀請蔣範華修女分享「從德蘭的靈修談基督徒的培育」</td>
                    <td>救世主堂</td>
                    <td>洪艷秋</td>
                </tr>
                <tr>
                    <td>5/24 (六)</td>
                    <td>邀請陳德光前輔大神學院院長「成聖」</td>
                    <td>救世主堂</td>
                    <td>洪艷秋</td>
                </tr>
                <tr>
                    <td>6/28 (六)</td>
                    <td>邀請吳伯仁神父主講：「禧年、朝聖」</td>
                    <td>救世主堂</td>
                    <td>林俊芳</td>
                </tr>
                <tr>
                    <td>7/12 (六)</td>
                    <td>邀請廖金常修女生活分享</td>
                    <td>救世主堂</td>
                    <td>翁詩貞</td>
                </tr>
                <tr>
                    <td>8/9 (六)</td>
                    <td>與年輕人的對話—新世代、新見識</td>
                    <td>救世主堂</td>
                    <td>廖玲玲</td>
                </tr>
                <tr>
                    <td>9/13 (六)</td>
                    <td>邀請郭青青修女生活分享</td>
                    <td>救世主堂</td>
                    <td>洪碧玉</td>
                </tr>
                <tr>
                    <td>10/3~5 (五~日)</td>
                    <td>小會年度共融營 (台中太平聖愛山莊) - 營長：朱豐榮</td>
                    <td>聖愛山莊</td>
                    <td>施麗華</td>
                </tr>
                <tr>
                    <td>11/8 (六)</td>
                    <td>前瞻與回顧，繼往開來，訂定新行事曆</td>
                    <td>救世主堂</td>
                    <td>施麗華</td>
                </tr>
                <tr>
                    <td>12/27 (六)</td>
                    <td>聖誕餐會 (第45次)</td>
                    <td>待定</td>
                    <td>劉文義</td>
                </tr>
                <tr>
                    <td>5月中旬</td>
                    <td>前往台南、嘉義、雲林等地朝聖與教堂一日遊</td>
                    <td>台南/嘉義/雲林</td>
                    <td>待定</td>
                </tr>
            </tbody>
        </table>
    """,
        unsafe_allow_html=True,
    )

    # 幹部名單
    st.markdown("---")
    st.markdown("### 2025年度幹部名單")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #f093fb; padding-bottom: 10px;'>主要幹部</h4>
                <p style='margin: 8px 0;'><strong>輔導神師：</strong>待聘神父</p>
                <p style='margin: 8px 0;'><strong>主席：</strong>施麗華</p>
                <p style='margin: 8px 0;'><strong>參議：</strong>顏闓明</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #f5576c; padding-bottom: 10px;'>組別負責人</h4>
                <p style='margin: 8px 0;'><strong>靈修組：</strong>林櫻枝、洪碧玉、洪艷秋、謝文檉</p>
                <p style='margin: 8px 0;'><strong>秘書組：</strong>楊黎芳、郭曉薇</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #f093fb; padding-bottom: 10px;'>服務組別</h4>
                <p style='margin: 8px 0;'><strong>活動組：</strong>林俊芳、朱豐榮、翁詩貞、顏闓明</p>
                <p style='margin: 8px 0;'><strong>關懷組：</strong>劉文義、陳惠姿、李美達</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #495057; border-bottom: 2px solid #f5576c; padding-bottom: 10px;'>支援組別</h4>
                <p style='margin: 8px 0;'><strong>會計組：</strong>鐘素馨、張燕惠</p>
                <p style='margin: 8px 0;'><strong>創意組：</strong>廖玲玲、張友青</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("### 2025年高雄分會讀書會行事曆")
    st.markdown("**研讀書籍：**《聖女大德蘭的全德之路》星火文化出版，加爾默羅聖衣會譯")
    st.markdown("**時間：** 2025年1月~2025年12月")
    st.markdown("**地點：** 救世主堂")

    # 讀書會行事曆表格
    st.markdown(
        """
        <style>
            .reading-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 15px;
                box-shadow: 0 2px 15px rgba(0,0,0,0.1);
                border-radius: 10px;
                overflow: hidden;
            }
            .reading-table thead tr {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: left;
                font-weight: bold;
            }
            .reading-table th,
            .reading-table td {
                padding: 15px;
                border: 1px solid #ddd;
            }
            .reading-table tbody tr {
                border-bottom: 1px solid #ddd;
                transition: background-color 0.3s;
            }
            .reading-table tbody tr:nth-of-type(even) {
                background-color: #f8f9fa;
            }
            .reading-table tbody tr:hover {
                background-color: #e9ecef;
            }
        </style>
        
        <table class="reading-table">
            <thead>
                <tr>
                    <th style='width: 20%;'>日期</th>
                    <th style='width: 15%;'>星期</th>
                    <th style='width: 45%;'>內容</th>
                    <th style='width: 20%;'>負責人</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1/17</td>
                    <td>五</td>
                    <td>第13-14章</td>
                    <td>顏闓明</td>
                </tr>
                <tr>
                    <td>2/21</td>
                    <td>五</td>
                    <td>第15-16章</td>
                    <td>林櫻枝</td>
                </tr>
                <tr>
                    <td>3/28</td>
                    <td>五</td>
                    <td>第17-18章</td>
                    <td>謝文檉</td>
                </tr>
                <tr>
                    <td>4/11</td>
                    <td>五</td>
                    <td>第19章</td>
                    <td>楊黎芳</td>
                </tr>
                <tr>
                    <td>5/16</td>
                    <td>五</td>
                    <td>第20-21章</td>
                    <td>廖金常修女</td>
                </tr>
                <tr>
                    <td>6/20</td>
                    <td>五</td>
                    <td>第22-23章</td>
                    <td>郭曉薇</td>
                </tr>
                <tr>
                    <td>7/25</td>
                    <td>五</td>
                    <td>第24-25章</td>
                    <td>施麗華</td>
                </tr>
                <tr>
                    <td>8/22</td>
                    <td>五</td>
                    <td>第26-27章</td>
                    <td>翁詩貞</td>
                </tr>
                <tr>
                    <td>9/26</td>
                    <td>五</td>
                    <td>第28-29章</td>
                    <td>陳惠姿</td>
                </tr>
                <tr>
                    <td>10/24</td>
                    <td>五</td>
                    <td>第30-31章</td>
                    <td>鐘素馨</td>
                </tr>
                <tr>
                    <td>11/28</td>
                    <td>五</td>
                    <td>第32-33章</td>
                    <td>劉文義</td>
                </tr>
                <tr>
                    <td>12/19</td>
                    <td>五</td>
                    <td>第34-42章</td>
                    <td>洪艷秋</td>
                </tr>
            </tbody>
        </table>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #e7f3ff; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #004085;'>📚 關於《聖女大德蘭的全德之路》</h4>
            <p style='color: #004085;'>這本書是聖女大德蘭的經典著作，引領我們走向靈修的高峰。透過每月的深入研讀與分享，
            我們將一起探索基督徒靈修生活的精髓，學習如何在日常生活中實踐祈禱與默觀。</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

with tab4:
    st.markdown("### 活動參與提醒")

    st.success("✨ 歡迎所有會員踴躍參與高雄分會各項活動！")

    st.markdown(
        """
        <div style='background-color: #e7f3ff; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #004085;'>📢 參與須知</h4>
            <ul style='color: #004085;'>
                <li>大部分活動在<strong>救世主堂</strong>舉行，請提前確認地點</li>
                <li>讀書會固定在每月<strong>第三或第四個星期五</strong>舉行</li>
                <li>朝聖活動需提前報名，以便安排交通</li>
                <li>共融營為年度重點活動，歡迎全家參與</li>
                <li>若有任何問題，請聯繫該活動負責人</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #d4edda; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h4 style='color: #155724;'>🙏 高雄分會特色</h4>
            <p style='color: #155724;'>高雄分會秉持「攜手同行—靈修、福傳、共融、傳承」的年度方向，透過多元化的活動：</p>
            <ul style='color: #155724;'>
                <li><strong>靈修培育：</strong>避靜、讀書會、專題演講</li>
                <li><strong>福傳見證：</strong>朝聖分享、修女神父生活分享</li>
                <li><strong>共融交流：</strong>與年輕人對話、聖誕餐會</li>
                <li><strong>傳承使命：</strong>定期讀書會、世代交流活動</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.info(
        "💡 高雄分會特別注重深度靈修陪伴，每月讀書會研讀聖女大德蘭著作，歡迎對默觀祈禱有興趣的會員加入！"
    )
