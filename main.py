import streamlit as st
import streamlit.components.v1 as components
from utils import init_page

init_page()

st.write(
    """
    <style>
        .container {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 2rem;
            padding: 1rem;
        }
        .logo {
            flex: 0 1 200px;
        }
        .logo img {
            width: 100%;
            height: auto;
            max-width: 200px;
        }
        .text {
            flex: 1 1 300px;
            font-size: 40px;
            line-height: 1.2;
        }
        @media (max-width: 768px) {
            .container {
                justify-content: center;
                text-align: center;
            }
            .logo {
                flex: 0 1 150px;
            }
            .text {
                font-size: 32px;
            }
        }
    </style>
    <div class="container">
        <div class="logo">
            <img src="app/static/images/logo.png" alt="CCSC Logo">
        </div>
        <div class="text">
            天主教<br>
            中華基督神修小會<br>
            Chinese Christian Spirit Community
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    st.write(
        """
<br>
<br>

**總會地址：** 台北市中山區林森北路73號2樓<br>
**聯絡電話：** (8862) 2523-0538<br>
**E-mail：** ccscasso@gmail.com<br>
    
#### 支持我們
**捐款帳號：**<br>
社團法人天主教中華基督神修小會之友人文關懷與服務促進協會<br>
 華南銀行新生分行 113-20-094051-5<br>
        """,
        unsafe_allow_html=True,
    )
with col2:
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
            style="border:0; width:100%; height:{300}px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
        """,
        height=300 + 50,
    )
