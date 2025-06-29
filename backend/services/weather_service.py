from dotenv import load_dotenv
import os
import requests

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city="Abuja"):
    if not API_KEY:
        print("API key not found")
        return {"error": "API key missing"}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title()
        }

        return weather

    except Exception as e:
        print("Fetch error:", e)
        return {"error": "Failed to fetch weather"}

