from dotenv import load_dotenv
import schedule
import time
from backend.services.weather_service import get_current_weather

load_dotenv()
def run_scheduler():
    def job():
        print("⏳ Scheduled fetch running...")
        data = get_current_weather()
        print("✅ Fetched:", data)
    job()
    schedule.every(4).hours.do(job)

    print("📅 Scheduler started (4-hour interval)")
    while True:
        schedule.run_pending()
        time.sleep(1)

