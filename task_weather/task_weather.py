import requests, json
from pydantic import BaseModel, validator, Extra

class Temperature(BaseModel):
    class Config:
        extra = Extra.forbid
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @validator('temp')
    def c_in_f(cls, value):
        return round(value * 9/5 + 32, 2)      # temp*9/5+32 (temp*1,8)

class Weather(BaseModel):
    temperature: Temperature    # температура
    pressure: int               # давление
    description: str            # описание
    name: str                   # название

class Coordinate:

    def __init__(self, latitude, longitude):
        self.__longitude = longitude
        self.__latitude = latitude

    def get_weather_information(self):
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/'
                                    f'current?lat={self.__latitude}&lon={self.__longitude}')
        try:
            if r.status_code != 200:
                raise Exception(f'Error request (status code: {r.status_code})')
            j_data = json.loads(r.text)
            try:
                _feels_like_ = j_data.get['main']['feels_like']
            except:
                _feels_like_ = 0
            data = {
                'temperature': {
                    'temp': j_data['main']['temp'],
                    'feels_like': _feels_like_,
                    'temp_min': j_data['main']['temp_min'],
                    'temp_max': j_data['main']['temp_max']
                },
                'pressure': j_data['main']['pressure'],
                'description': j_data['weather'][0]['description'],
                'name': j_data['name']
            }
        except:
            return None
        return Weather(**data)


coordinate = Coordinate(51.89, 26.85)    #Stolin
weather = coordinate.get_weather_information()
print(f'In {weather.name} {weather.temperature.temp} F')
