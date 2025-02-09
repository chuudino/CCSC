import streamlit as st
import streamlit.components.v1 as components

st.title("台灣地圖顯示")


hight_size = st.slider("地圖高度", 300, 800, 450)

# 顯示地圖
components.html(
    f"""
    <style>
        .map-container {{
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
            background: white;
            margin: 25px 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .map-container:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
        }}
        iframe {{
            border-radius: 16px;
            width: 100%;
            border: none;
        }}
    </style>
    <div class="map-container">
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d7229.045699996474!2d121.525248!3d25.050262!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a96f7a8026a5%3A0x98986b0570c04a8!2zMTA0OTHlj7DngaPlj7DljJfluILkuK3lsbHljYDmnpfmo67ljJfot683N-iZnw!5e0!3m2!1szh-TW!2sus!4v1739080745518!5m2!1szh-TW!2sus" 
        style="border:0; width:100%; height:{hight_size}px;" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade">
        </iframe>
    </div>
    """,
    height=hight_size + 50,
)
