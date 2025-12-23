import streamlit as st
from weather_api import get_current_weather, get_forecast

st.set_page_config(page_title="Weather Details", layout="centered")

def apply_dark_mode():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    .stApp {
        background-color: #020617;
    }

    h1, h2, h3, h4, h5, h6, p, span {
        color: #ffffff !important;
    }

    .card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

dark_mode = st.session_state.get("dark", False)
if dark_mode:
    apply_dark_mode()

if "city" not in st.session_state:
    st.error("No city selected")
    st.stop()

city = st.session_state["city"]

weather = get_current_weather(city)
hourly, five_day = get_forecast(city)

if weather is None:
    st.error("Weather data not found")
    st.stop()

icon_url = f"https://openweathermap.org/img/wn/{weather['icon']}@2x.png"

# ===== Current Weather Box =====
st.markdown(f"""
<div class="card" style="max-width:400px; margin:auto;">
    <h2>{weather['city']}, {weather['country']}</h2>
    <img src="{icon_url}" style="width:100px; height:100px;">
    <h1>{weather['temp']}°C</h1>
    <p style="font-size:18px;">{weather['desc']}</p>
    <p style="font-size:16px;">Humidity: {weather['humidity']}%</p>
    <p style="font-size:16px;">Wind Speed: {weather['wind']} m/s</p>
</div>
""", unsafe_allow_html=True)

# ===== Hourly Forecast =====
st.subheader("Today's Weather")
cols = st.columns(len(hourly))
for col, h in zip(cols, hourly):
    with col:
        icon = f"https://openweathermap.org/img/wn/{h['icon']}@2x.png"
        st.markdown(f"""
        <div class="card">
            <p>{h['time']}</p>
            <img src="{icon}" style="width:60px; height:60px;">
            <p>{h['temp']}°C</p>
        </div>
        """, unsafe_allow_html=True)

# ===== 5-Day Forecast =====
st.subheader("5-Day Forecast")
cols = st.columns(5)
for col, (day, info) in zip(cols, five_day.items()):
    with col:
        icon = f"https://openweathermap.org/img/wn/{info['icon']}@2x.png"
        st.markdown(f"""
        <div class="card">
            <p>{day}</p>
            <img src="{icon}" style="width:60px; height:60px;">
            <p>{info['temp']}°C</p>
        </div>
        """, unsafe_allow_html=True)
