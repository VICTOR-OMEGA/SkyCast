from dotenv import load_dotenv
import os
import schedule
import time
import sqlite3
from backend.services.weather_service import get_current_weather

# Load .env file
load_dotenv(dotenv_path=".env")

# SQLite DB path
DB_PATH = "skycast.db"

def save_weather_to_db(data):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO weather (temperature, humidity, wind_speed, description)
            VALUES (?, ?, ?, ?)
        """, (
            data["temperature"],
            data["humidity"],
            data["wind_speed"],
            data["description"]
        ))

        conn.commit()
        conn.close()
        print("✅ Weather saved to DB")
    except Exception as e:
        print("❌ DB error:", e)

def run_scheduler():
    def job():
        print("⏳ Scheduled fetch running...")
        data = get_current_weather()
        print("✅ Fetched:", data)
        if "error" not in data:
            save_weather_to_db(data)

    job()  # Run once immediately
    schedule.every(4).hours.do(job)

    print("📅 Scheduler started (4-hour interval)")
    while True:
        schedule.run_pending()
        time.sleep(1)

