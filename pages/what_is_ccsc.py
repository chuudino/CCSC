import streamlit as st
from utils import init_page

init_page(page_name="what_is_ccsc")  # 初始化頁面設定並設置對應的 page_name

if st.sidebar.button("↩️ 返回上一頁"):
    st.switch_page("pages/about_us.py")

st.title("小會是甚麼")
st.markdown(
    """
    <div style="font-size:20px">
    小會是一個以基督愛為中心的大家庭。在這個家庭內，每位成員須陶成為具有獨立健全人格及深厚內修基礎的成熟教友。他們隨著時代的進步，以學習、進取的態度，不斷在各方面求取進步與發展。他們之間以手足之情，彼此鼓勵，彼此幫助，使個個成為活的基督。<br><br>

    由於生活方式的不同，每個人對天主的奉獻也不一致。有的以婚姻生活達到成全，有的以獨身生活或修會生活奉獻整個生命。總之，小會期望藉著每個人不同的生活環境，在各自工作岡位上發揮自已所有的能力，以個人的身份與人合作，在人群中默默耕耘，不求浮華的名利，藉著其對周遭的影響力，使社會更臻完善。因著不斷與人接觸，與眾人並肩工作，讓天主藉著他們進入世界，基督藉他們的口、他們的心和他們的手，愛人助人。更要緊的是：使世人認識並了解上主聖愛的計劃，幫助他們承受基督的新生命。因此，不論在教會內或教會外，不論其從事於直接或間接的傳教工作，都應具有神化一切的胸襟，隨時為人群服務。<br><br>

    人類本是一體，自古至今文化正向著天主演進，因此會具應當看清並重視這一切進展，積極參與現世工作，從事各種研究。思想方面尤需努力，一面發揚中華文化的所有優長，一面吸取世界其他文化中各種特質，加以熔鑄。使東西文化匯入基督的洪流，使華夏精神在基督內發揚出來。不能在理論上探討融合的，也應該在行動中常常思索如何將基督的精神更容易讓中國人接受。<br><br>

    小會的精神是：基督的聖愛，基督的自由，基督的喜樂。基督的聖愛是小會的根本精神。這種聖愛是無條件的，是無私的，是無限的，是永恆的。這種聖愛是基督對我們每一個人的愛，這種聖愛是基督對我們每一個人的呼召。這種聖愛是基督對我們每一個人的使命。這種聖愛是基督對我們每一個人的責任。這種聖愛是基督對我們每一個人的期望。這種聖愛是基督對我們每一個人的要求。這種聖愛是基督對我們每一個人的祝福。這種聖愛是基督對我們每一個人的恩典。這種聖愛是基督對我們每一個人的救贖。這種聖愛是基督對我們每一個人的希望。這種聖愛是基督對我們每一個人的信仰。這種聖愛是基督對我們每一個人的生命。這種聖愛是基督對我們每一個人的真理。這種聖愛是基督對我們每一個人的光明。這種聖愛是基督對我們每一個人的道路。這種聖愛是基督對我們每一個人的真理。這種聖愛是基督對我們每一個人的生命。<br><br>

    因此，唯有超脫一切的精神，才能使人不受制於痛苦或失敗，喪失內心的自由。唯有真喜樂，方可逐出一切因自私而產生的憂慮，更深的體驗到基督聖愛的甘飴。在聖愛中，自由與喜樂變成會員精神的綱領；活潑的信恃，無盡的期望與忘我的愛德，成為行為的指歸。由於人性的軟弱，不停的藉聖體與主結合，潛心的祈禱，與勤領福音的啟迪，成為會員生活的活水。為此小會希望在基督內成為一個大家庭，因團體內的互愛互助，成為基督在這世上另一個有力的見證。
    </div>
    """,
    unsafe_allow_html=True,
)
