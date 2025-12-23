import requests

def get_city_from_ip():
    try:
        res = requests.get("https://ipinfo.io/json", timeout=5)
        return res.json().get("city")
    except:
        return None
