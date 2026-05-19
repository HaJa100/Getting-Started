import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def fetch_weather(city: str):
    if not API_KEY:
        return None, "OpenWeatherMap API key is not configured. Set OPENWEATHER_API_KEY."

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]
        main = data["main"]
        wind = data.get("wind", {})

        return {
            "city": f"{data.get('name')}, {data['sys'].get('country')}",
            "temperature": round(main.get("temp", 0)),
            "description": weather.get("description", "Unknown").title(),
            "icon_url": f"https://openweathermap.org/img/wn/{weather.get('icon')}@2x.png",
            "humidity": main.get("humidity"),
            "pressure": main.get("pressure"),
            "wind_speed": wind.get("speed"),
        }, None
    except requests.HTTPError as http_err:
        if response.status_code == 404:
            return None, "City not found. Please check the spelling and try again."
        return None, f"Weather API error: {http_err}"
    except requests.RequestException as req_err:
        return None, f"Network error: {req_err}"
    except Exception as err:
        return None, f"Unexpected error: {err}"


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            weather, error = fetch_weather(city)
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    app.run(debug=True)
