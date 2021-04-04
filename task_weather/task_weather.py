from typing import Optional

import json
import requests
from pydantic import BaseModel, validator, Extra


class Temperature(BaseModel):
    class Config:
        extra = Extra.forbid

    temp: float
    feels_like: Optional[float]
    temp_min: float
    temp_max: float

    @validator('temp')
    def c_in_f(cls, value: float) -> float:
        return round(value * 9 / 5 + 32, 2)


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: Optional[str]
    name: str


class Coordinate:

    def __init__(self, latitude: float, longitude: float) -> Weather:
        self.__longitude = longitude
        self.__latitude = latitude

    def get_weather_information(self):
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/'
                         f'current?lat={self.__latitude}&lon={self.__longitude}')
        try:
            if r.status_code != 200:
                raise Exception(f'Error request (status code: {r.status_code})')
            j_data = json.loads(r.text)
            data = {
                'temperature': {
                    'temp': j_data['main']['temp'],
                    'feels_like': j_data['main']['feels_like'] if j_data['main']['feels_like'] else 0,
                    'temp_min': j_data['main']['temp_min'],
                    'temp_max': j_data['main']['temp_max']
                },
                'pressure': j_data['main']['pressure'],
                'description': j_data['weather'][0]['description'] if j_data['weather'] else None,
                'name': j_data['name']
            }
        except Exception as e:
            return
        return Weather(**data)


coordinate = Coordinate(51.89, 26.85)  # Stolin
weather = coordinate.get_weather_information()

if weather:
    print(f'In {weather.name} {weather.temperature.temp} F')
    print(f'Feels like: {weather.temperature.feels_like} C')
