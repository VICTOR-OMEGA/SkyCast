from flask import Blueprint, render_template, request, Response
from backend.services.weather_service import get_current_weather
from backend.services.history_service import get_weather_history, get_10_day_summary

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def dashboard():
    city = request.args.get("city", "Abuja")
    current = get_current_weather(city=city)
    history = get_weather_history(limit=10)
    summary = get_10_day_summary()

    return render_template("dashboard.html", data=current, history=history, city=city, summary=summary )

@main.route("/history")
def full_history():
    from backend.services.history_service import get_weather_history
    history = get_weather_history(limit=1000)
    return render_template("history.html", history=history)

@main.route("/export")
def export_csv():
    import csv
    import io
    from backend.services.history_service import get_weather_history

    history = get_weather_history(limit=10000)
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Description"])
    for row in history:
        writer.writerow([
            row["timestamp"],
            row["temperature"],
            row["humidity"],
            row["wind_speed"],
            row["description"]
        ])

    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=skycast_weather.csv"})

@main.route("/trends")
def weather_trends():
    from backend.services.history_service import get_10_day_summary
    summary = get_10_day_summary()
    return render_template("trends.html", summary=summary)

