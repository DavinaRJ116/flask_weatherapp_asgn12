from flask import Flask, render_template, request

app = Flask(__name__)

dummy_weather = {
    "Chennai": {"temp": 32, "humidity": 70, "desc": "Sunny"},
    "Mumbai": {"temp": 29, "humidity": 80, "desc": "Rainy"},
    "Bangalore": {"temp": 25, "humidity": 60, "desc": "Cloudy"},
    "Delhi": {"temp": 34, "humidity": 65, "desc": "Hot"},
    "Kolkata": {"temp": 30, "humidity": 75, "desc": "Humid"}
}

dummy_forecast = {
    "Chennai": [
        {"date": "2025-09-20", "min": 27, "max": 34, "icon": "☀️"},
        {"date": "2025-09-21", "min": 26, "max": 33, "icon": "☁️"},
        {"date": "2025-09-22", "min": 28, "max": 35, "icon": "🌧️"},
        {"date": "2025-09-23", "min": 27, "max": 34, "icon": "☀️"},
        {"date": "2025-09-24", "min": 26, "max": 33, "icon": "⛅"},
    ],
    "Mumbai": [
        {"date": "2025-09-20", "min": 25, "max": 30, "icon": "🌧️"},
        {"date": "2025-09-21", "min": 24, "max": 31, "icon": "⛅"},
        {"date": "2025-09-22", "min": 26, "max": 32, "icon": "🌧️"},
        {"date": "2025-09-23", "min": 25, "max": 29, "icon": "🌩️"},
        {"date": "2025-09-24", "min": 26, "max": 30, "icon": "🌧️"},
    ],
    "Bangalore": [
        {"date": "2025-09-20", "min": 20, "max": 26, "icon": "☁️"},
        {"date": "2025-09-21", "min": 19, "max": 27, "icon": "🌧️"},
        {"date": "2025-09-22", "min": 21, "max": 28, "icon": "⛅"},
        {"date": "2025-09-23", "min": 20, "max": 27, "icon": "☁️"},
        {"date": "2025-09-24", "min": 21, "max": 29, "icon": "☀️"},
    ],
}

@app.route("/", methods=["GET", "POST"])
def weather():
    city = None
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = dummy_weather.get(city)
    return render_template(
        "weather.html",
        cities=dummy_weather.keys(),
        city=city,
        weather=weather
    )

@app.route("/forecast/<city>")
def forecast(city):
    forecast_data = dummy_forecast.get(city, [])
    return render_template(
        "forecast.html",
        city=city,
        forecast=forecast_data
    )

if __name__ == "__main__":
    app.run(debug=True)
