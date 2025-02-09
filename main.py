import streamlit as st
import streamlit.components.v1 as components


st.title("台灣地圖顯示")

# 建立範例資料 - 以台北市為中心點
# <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d7229.045699996474!2d121.525248!3d25.050262!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96f7a8026a5%3A0x98986b0570c04a8!2zMTA0OTHlj7DngaPlj7DljJfluILkuK3lsbHljYDmnpfmo67ljJfot683N-iZnw!5e0!3m2!1szh-TW!2sus!4v1739080745518!5m2!1szh-TW!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
# 顯示地圖
components.html(
    """
    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d7229.045699996474!2d121.525248!3d25.050262!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96f7a8026a5%3A0x98986b0570c04a8!2zMTA0OTHlj7DngaPlj7DljJfluILkuK3lsbHljYDmnpfmo67ljJfot683N-iZnw!5e0!3m2!
    1szh-TW!2sus!4v1739080745518!5m2!1szh-TW!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    """,
    height=500,
)
