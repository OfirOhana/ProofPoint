from datetime import datetime

import requests

APP_ID = "b9946950ade344f6ea4bdbf487a16346"
GET_WEATHER_INFO_URL = "https://api.openweathermap.org/data/2.5/weather?q={location}&appid={app_id}"


def get_city_weather_status(location: str) -> dict:
    """
    Get the given location weather status by OpenWeatherMap API.

    :param location: city to search for it weather status.
    :return: weather status as dict.
    """
    complete_api_link = GET_WEATHER_INFO_URL.format(location=location, app_id=APP_ID)

    resp = requests.get(complete_api_link)

    if resp.ok:
        return resp.json()
    print("Invalid request to weather API server.")


def parser_weather_data(weather_data: dict) -> dict:
    """
    Parse weather data from JSON structure.

    :param weather_data: Full dictionary data given from API response.
    :return: Dict that contains only the important weather information for our application.
    """
    date = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    temperature = weather_data['main']['temp'] - 273.15
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']

    return dict(date=date, temperature=temperature, description=description, wind_speed=wind_speed, humidity=humidity)


def print_weather_info(info: dict):
    print('\n', info['date'])
    print('-----------------------------------')
    print("The temperature is    : {:.2f} deg C".format(info['temperature']))
    print("Weather description   : {}".format(info['description']))
    print("Humidity              : {} %".format(info['humidity']))
    print("Wind Speed            : {} kmph".format(info['wind_speed']))


def get_weather_by_city_name():
    city_name = input("Enter the city name: ")
    weather_data = get_city_weather_status(city_name)

    if weather_data is not None:
        if weather_data["cod"] == "404":
            print("Please check again your city name, maybe there was a typo.")
        else:
            parsed_data = parser_weather_data(weather_data)
            print_weather_info(parsed_data)


if __name__ == '__main__':
    get_weather_by_city_name()
