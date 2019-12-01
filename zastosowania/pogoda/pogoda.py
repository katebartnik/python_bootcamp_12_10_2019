from textwrap import dedent

import requests
from collections import namedtuple

# https://www.metaweather.com/api/location/search/?query=warsaw
# https://www.metaweather.com/api/location/44418/


fields = ["id", "weather_state_name", "weather_state_abbr", "wind_direction_compass", "created", "applicable_date",
          "min_temp", "max_temp", "the_temp", "wind_speed", "wind_direction", "air_pressure", "humidity", "visibility",
          "predictability"]

Weather = namedtuple('Weather', fields)


def get_location_id(location_name):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}")
    if resp.status_code == 200:
        location_id = resp.json()[0]["woeid"]
        return location_id
    raise Exception("Niepoprawny response code z api. Być moze serwis nie działa?")


def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    weather = resp.json()['consolidated_weather'][0]
    weather = Weather(**weather)
    return weather

def prepare_weather_report(weather, location_name):
    report = f""" 
    Pogoda w lokalizacji: {location_name}
    średnia temperatura: {weather.the_temp} C
    wilgotność: {weather.humidity} %
    ciśnienie powietrza: {weather.air_pressure} hPa
    """

    return dedent(report)