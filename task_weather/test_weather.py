import json
import requests
from task_weather import Coordinate, Temperature, Weather

from unittest.mock import Mock


def test_get_weather_information(mocker):
    mocker.patch.object(
        requests,
        'get',
        return_value=Mock(
            status_code = 200,
            text = json.dumps(
                {
                    "coord": {"lon": 26.85, "lat": 51.89},
                    "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds",
                                 "icon": "https://cdn.glitch.com/6e8889e5-7a72-48f0-a061-863548450de5%2F04d.png?1499366020964"}],
                    "base": "stations",
                    "main": {"temp": 5.18, "feels_like": 5.18, "temp_min": 5.18, "temp_max": 5.18, "pressure": 1015,
                             "humidity": 58, "sea_level": 1015, "grnd_level": 997},
                    "visibility": 10000,
                    "wind": {"speed": 1.03, "deg": 229, "gust": 1.25},
                    "clouds": {"all": 71},
                    "dt": 1617552182,
                    "sys": {"country": "BY", "sunrise": 1617507628, "sunset": 1617555019},
                    "timezone": 10800,
                    "id": 621277,
                    "name": "Stolin",
                    "cod": 200
                }
            )
        )
    )
    expected = Weather(
        temperature = Temperature.construct(
            temp = 41.32,
            feels_like = 5.18,
            temp_min = 5.18,
            temp_max = 5.18
        ),
        pressure = 1015,
        description = 'broken clouds',
        name = 'Stolin'
    )
    coordinate = Coordinate(51.89, 26.85)
    result = coordinate.get_weather_information()

    assert result == expected
