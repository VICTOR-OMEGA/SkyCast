import sqlite3
from datetime import datetime
from collections import defaultdict

DB_PATH = "skycast.db"

def get_weather_history(limit=10):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT timestamp, temperature, humidity, wind_speed, description
            FROM weather
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()

        history = [
            {
                "timestamp": row[0],
                "temperature": row[1],
                "humidity": row[2],
                "wind_speed": row[3],
                "description": row[4]
            }
            for row in rows
        ]

        return history

    except Exception as e:
        print("Error reading history:", e)
        return []

def get_10_day_summary(db_path="skycast.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, temperature, humidity, wind_speed, description
        FROM weather
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    summary = defaultdict(lambda: {"temp": [], "humidity": [], "wind": [], "rain": 0})

    for ts, temp, hum, wind, desc in rows:
        date = ts.split(" ")[0]
        if len(summary) >= 10 and date not in summary:
            continue

        summary[date]["temp"].append(temp)
        summary[date]["humidity"].append(hum)
        summary[date]["wind"].append(wind)
        if "rain" in desc.lower():
            summary[date]["rain"] += 1

    result = []
    for day in sorted(summary.keys()):
        values = summary[day]
        result.append({
            "date": day,
            "temperature": round(sum(values["temp"]) / len(values["temp"]), 2),
            "humidity": round(sum(values["humidity"]) / len(values["humidity"]), 2),
            "wind_speed": round(sum(values["wind"]) / len(values["wind"]), 2),
            "rain_count": values["rain"]
        })

    return result
