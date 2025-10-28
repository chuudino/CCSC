import streamlit as st
from utils import init_page

# 統一 key
init_page(page_name="about_us_timeline_ccsc")  # 初始化頁面設定

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/about_us.py")

# 這之後可以加入你的頁面內容
st.title("大事年表")
# 使用 HTML table，並設定第一欄固定寬度及不換行，避免年份在寬度不足時換行
st.markdown(
    """
    <style>
      .timeline-table { width: 100%; border-collapse: collapse; font-size:20px; }
      .timeline-table th, .timeline-table td { padding: 10px 12px; vertical-align: top; }
      .timeline-table col.year-col { width: 120px; }
      /* 西元欄改為靠左對齊，並在左側保留少許內距 */
      .timeline-table th.year-col, .timeline-table td.year-col { white-space: nowrap; text-align: left; padding-left: 10px; }
      .timeline-table td.event-col { white-space: normal; }
      .timeline-table th { text-align: left; }
      .timeline-container { font-size:20px; }
    </style>
    <div class="timeline-container">
    <p>2024.12.17修訂<br>2025.03.17修定</p>
    <table class="timeline-table">
      <colgroup>
        <col class="year-col" />
        <col />
      </colgroup>
      <thead>
        <tr><th class="year-col">西元</th><th>紀事</th></tr>
      </thead>
      <tbody>
        <tr><td class="year-col">一九六二</td><td class="event-col">王志奘偕同幾位教友草創於臺北市天主教聖母會服務中心<br>十一月十二日臺北小組(即今臺北分會)立定規模</td></tr>
        <tr><td class="year-col">一九六五</td><td class="event-col">臺中成立小組(即今臺中分會)</td></tr>
        <tr><td class="year-col">一九六六</td><td class="event-col">總會成立(設於臺北)；十二位會員首度奉獻</td></tr>
        <tr><td class="year-col">一九六七</td><td class="event-col">七月一日於淡水聖本篤修女會會院通過會章草案</td></tr>
        <tr><td class="year-col">一九七〇</td><td class="event-col">三月三十日於陽明山福音園通過會章<br>成立心泉編輯小組編印《心泉》小會刊物</td></tr>
        <tr><td class="year-col">一九七三</td><td class="event-col">九月 總會設立專任秘書</td></tr>
        <tr><td class="year-col">一九七四</td><td class="event-col">北美分會成立<br>高雄分會成立<br>八月 宗旨精神輔助說明草本〇稿<br>九月 總會設立專任輔導，同時撤銷專任秘書<br>九月廿一日於臺北耕莘文教院舉行首度〇身奉獻典禮七位臺北分會會員</td></tr>
        <tr><td class="year-col">一九七五</td><td class="event-col">八月 《會員手冊》初版</td></tr>
        <tr><td class="year-col">一九七八</td><td class="event-col">九月 總會恢復專任秘書<br>九月 成立基金會</td></tr>
        <tr><td class="year-col">一九七九</td><td class="event-col">一月 〈<strong>神修小會簡介</strong>〉印行<br>四月 北美分會祈禱同工設立<br>十月 總會設立專職工作人員</td></tr>
        <tr><td class="year-col">一九八〇</td><td class="event-col">八月 〈<strong>神修小會會徽</strong>〉通過<br>九月 北美分會首度終身奉獻 五位會員</td></tr>
        <tr><td class="year-col">一九八一</td><td class="event-col">五月 小會會員首度晉鐸〇胡國楨神父<br>十二月小會陶成訓練計畫完稿印行</td></tr>
        <tr><td class="year-col">一九八三</td><td class="event-col">十月 臺北分會設立區會</td></tr>
        <tr><td class="year-col">一九八四</td><td class="event-col">八月 《會員手冊》章程修改通過<br>包括會員代表大會、總會主席人選及任期、分會<br>主席及〇議任期、奉獻分類等項</td></tr>
        <tr><td class="year-col">一九八六</td><td class="event-col">十月 訂立「會員代表大會遴選會員代表辦法」</td></tr>
        <tr><td class="year-col">一九九〇</td><td class="event-col">《會員手冊》章程修改通過<br>總會主席由奉獻三年以上會員中提名</td></tr>
        <tr><td class="year-col">一九九一</td><td class="event-col">一月 臺中分會設立「善牧基金會」<br>三月 臺北分會設立「天音慕道小組」<br>四月 高雄分會設立「四維諮詢中心」<br>九月 臺中分會首度終身奉獻 一位會員</td></tr>
        <tr><td class="year-col">一九九三</td><td class="event-col">八月 《會員手冊》會章上篇及前言通過<br>八月 會員代表大會通過天主聖三為小會主保，並以 「天主聖三節」為小會會慶日</td></tr>
        <tr><td class="year-col">一九九四</td><td class="event-col">六月 臺中分會設立「天主教活泉福傳工作室」<br>七月 獨身奉獻陶成資料「聖三之路」文集編輯</td></tr>
        <tr><td class="year-col">一九九六</td><td class="event-col">八月 基金章程修改通過<br>九月 高雄分會首度終身奉獻 二位會員</td></tr>
        <tr><td class="year-col">二〇〇〇</td><td class="event-col">一月 陶成資料〈<strong>心泉文選</strong〉〉目錄完稿</td></tr>
        <tr><td class="year-col">二〇〇二</td><td class="event-col">一月 北美分會祈禱通訊正式上網<br>介紹小會的資料首次放在網路上 (主教團網站)</td></tr>
        <tr><td class="year-col">二〇〇三</td><td class="event-col">電子信箱ccsc.ccsc@msa.hinet.net.net 設立</td></tr>
        <tr><td class="year-col">二〇〇六</td><td class="event-col">六月 〈<strong>神修小會簡介</strong〉〉重新編印發行；通過小會會旗與精神標誌旗幟<br>九月 北美分會成立「芥子園部落格」</td></tr>
        <tr><td class="year-col">二〇〇八</td><td class="event-col">八月 小會成立〈<strong>祈禱go</strong〉〉部落格<br>八月 《會員手冊》會章上篇修訂通過<br>十月 北美分會刊物〈<strong>芥子</strong〉〉網路版刊登在芥子園部落格</td></tr>
        <tr><td class="year-col">二〇一〇</td><td class="event-col">八月 《會員手冊》會章下篇修訂通過</td></tr>
        <tr><td class="year-col">二〇一一</td><td class="event-col">四月 芥子停止印行實體板</td></tr>
        <tr><td class="year-col">二〇一二</td><td class="event-col">八月 《會員手冊》修訂重新編印發行<br>十二月總會辦公室由震旦中心遷入康泰基金會辦公室</td></tr>
        <tr><td class="year-col">二〇一三</td><td class="event-col">五月 總會辦公室由康泰基金會遷入長安天主堂<br>八月 總會成立專門輔導小組編寫〈<strong>神修溯源手冊</strong〉〉推動神修小會溯源行動<br>九月 祈禱go與芥子園合併成立「神修小會共融園地部落格」</td></tr>
        <tr><td class="year-col">二〇一四</td><td class="event-col">十月 內政部許可設立「社團法人天主教中華基督神修小會之友人文關懷與服務促進協會」(以下簡稱小會之友協會)<br>增設專用電子信箱 ccscasso@gmail.com<br>十二月總會網站由青年組成員與研發組主持下開始籌劃文化福傳組開始約稿，並建立文化福傳網站(之後併入總會網站)</td></tr>
        <tr><td class="year-col">二〇一五</td><td class="event-col">二月 總會網站開始使用 http://ccsc.org.tw<br>向內政部登記設立「社團法人天主教中華基督神修<br>小會之友人文關懷與服務促進協會」<br>七月 小會之友協會與長安天主堂合作向台北市政府社會局申請成立第一個社區老人關懷服務據點</td></tr>
        <tr><td class="year-col">二〇一七</td><td class="event-col">五月 小會首度進行「團體分辨」<br>五月 小會青壯組同〇層360度團體成立，定期舉辦講座</td></tr>
        <tr><td class="year-col">二〇一九</td><td class="event-col">十月 臨時會員代表大會決議：<br>小會基金分批移轉至協會的基金帳戶<br>小會分會主席與分會選任參議的任期由二年改為三年，同總會主席</td></tr>
        <tr><td class="year-col">二〇二〇</td><td class="event-col">四月 小會之友協會與台北瑪利亞方濟傳教修女會合作向台北市政府社會局申請成立第二個社區老人關懷服務據點</td></tr>
        <tr><td class="year-col">二〇二二</td><td class="event-col">五月 〈<strong>神修小會簡介</strong〉〉第三版<br>六月十二日小會成立六十周年鍾安住總主教於台北古亭聖心堂主持感恩彌撒<br>十月 小會慶祝60周年特刊心泉第一〇〇期</td></tr>
        <tr><td class="year-col">二〇二三</td><td class="event-col">二月 慶祝小會成立六十周年於高雄真福山舉辦全球共融營</td></tr>
        <tr><td class="year-col">二〇二四</td><td class="event-col">七月 高雄分會由高雄四維文教中心遷出<br>十一月總會成立工作小組，啟動修訂《會員手冊》</td></tr>
      </tbody>
    </table>
    </div>
    """,
    unsafe_allow_html=True,
)
