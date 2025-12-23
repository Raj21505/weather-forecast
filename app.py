import streamlit as st
from location import get_city_from_ip

st.set_page_config(page_title="Weather App", layout="centered")

def apply_dark_mode():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    .stApp {
        background-color: #0f172a;
    }

    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }

    input {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }

    button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

dark_mode = st.toggle("Dark Mode")

if dark_mode:
    apply_dark_mode()

st.title("Weather Application")
st.write("Search weather by city or use auto-detected location")

default_city = get_city_from_ip()
city = st.text_input("Enter City Name", value=default_city if default_city else "")

if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("Please enter a city name")
    else:
        st.session_state["city"] = city
        st.session_state["dark"] = dark_mode
        st.switch_page("pages/1_Weather_Details.py")
