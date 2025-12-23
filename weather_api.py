import requests
import streamlit as st
from datetime import datetime

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_current_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(CURRENT_URL, params=params)

    if r.status_code != 200:
        return None

    d = r.json()
    return {
        "city": d["name"],
        "country": d["sys"]["country"],
        "temp": d["main"]["temp"],
        "desc": d["weather"][0]["description"].title(),
        "icon": d["weather"][0]["icon"],
        "humidity": d["main"]["humidity"],
        "wind": d["wind"]["speed"]
    }


def get_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(FORECAST_URL, params=params)

    if r.status_code != 200:
        return None

    data = r.json()["list"]
    today = datetime.now().date()

    hourly_today = []
    five_day = {}

    for item in data:
        dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
        date = dt.date()

        if date == today:
            hourly_today.append({
                "time": dt.strftime("%I %p"),
                "temp": item["main"]["temp"],
                "icon": item["weather"][0]["icon"]
            })

        if date not in five_day and len(five_day) < 5:
            five_day[date.strftime("%d %b")] = {
                "temp": item["main"]["temp"],
                "icon": item["weather"][0]["icon"]
            }

    return hourly_today, five_day
