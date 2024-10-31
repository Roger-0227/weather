from pyowm.owm import OWM
from requests import Timeout
from pyowm.owm import OWM
from dateutil import parser
import pytz
import json
from config.settings import TIME_ZONE


class Weather:
    def __init__(self, owm_api_key=None):
        self._owm_api_key = owm_api_key
        self._location = TIME_ZONE.split("/")[1]
        self._owm = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def get_owm(self):
        try:
            if not self._owm:
                self._owm = OWM(self._owm_api_key)
        except Timeout as err:
            print(f"WeatherStation owm fail with TimeOut error :\n{err}")
        return self._owm

    def get_weather_data(self):
        mgr = self.get_owm.weather_manager()
        weather = mgr.weather_at_place(self._location + ",TW").weather
        return weather

    def get_air_quality(self):
        location = self.get_owm.city_id_registry().ids_for(
            self._location, country="TW", matching="exact"
        )[0]
        mgr = self.get_owm.airpollution_manager()
        try:
            air_quality = mgr.air_quality_at_coords(location[-2], location[-1])
        except:
            print("Error")
        return air_quality
