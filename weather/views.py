import os

import pytz
from dateutil import parser
from django.shortcuts import render

from config.settings import TIME_ZONE

from .weather import Weather


def home(request):
    return render(request, "pages/home.html")


def index(request):
    location = request.GET.get("location")
    api_key = os.getenv("api_key")
    weather = Weather(api_key, location).get_weather_data()
    air_quality = Weather(api_key).get_air_quality()
    taiwan_timezone = pytz.timezone(TIME_ZONE)
    reference_time = weather.reference_time(timeformat="iso")

    time = (
        parser.isoparse(reference_time)
        .astimezone(taiwan_timezone)
        .strftime("%Y-%m-%d %H:%M:%S")
    )
    status = weather.status
    detailed_status = weather.detailed_status
    temp_f = weather.temperature("fahrenheit")
    temp_c = weather.temperature("celsius")
    humidity = weather.humidity
    wind_miles_hour = weather.wind(unit="miles_hour")
    wind_knots = weather.wind(unit="knots")
    wind_beaufort = weather.wind(unit="beaufort")
    rain_1 = weather.rain.get("1h", 0)
    rain_3 = weather.rain.get("3h", 0)
    press_metric = weather.barometric_pressure()["press"]
    press_imperial = weather.barometric_pressure(unit="inHg")["press"]
    visibility_metric = weather.visibility()
    visibility_imperial = weather.visibility(unit="miles")
    sunrise = (
        weather.sunrise_time(timeformat="date")
        .astimezone(taiwan_timezone)
        .strftime("%Y-%m-%d %H:%M:%S")
    )
    sunset = (
        weather.sunset_time(timeformat="date")
        .astimezone(taiwan_timezone)
        .strftime("%Y-%m-%d %H:%M:%S")
    )

    content = {
        "location": location,
        "time": time,
        "status": status,
        "detailed_status": detailed_status,
        "temp_f": temp_f,
        "temp_c": temp_c,
        "humidity": humidity,
        "wind_miles_hour": wind_miles_hour,
        "wind_knots": wind_knots,
        "wind_beaufort": wind_beaufort,
        "rain_1": rain_1,
        "rain_3": rain_3,
        "press_metric": press_metric,
        "press_imperial": press_imperial,
        "visibility_metric": visibility_metric,
        "visibility_imperial": visibility_imperial,
        "sunrise": sunrise,
        "sunset": sunset,
        "air_quality": air_quality,
    }
    return render(request, "pages/index.html", content)
