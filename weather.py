import requests


WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

API_KEY = ''


class WeatherModel:
    def __init__(self, api=API_KEY, url=WEATHER_URL):
        self.api = api
        self.ulr = url

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api,
            "units": "metric",
            "lang": "ru"
        }

        res = requests.get(self.ulr, params=params)

        if res.ok:
            data = res.json()
            pressure_hpa = data["main"]["pressure"]
            pressure_mmhg = round(pressure_hpa * 0.75006)
            weather = {
                "city": data["name"],
                "description": data["weather"][0]["description"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": pressure_mmhg
            }

            return weather
        else:
            print("Ошибка:", res.status_code)
            return ''



if __name__ == '__main__':
    weather_model = WeatherModel()
    answer = weather_model.get_weather("Москва")
    print("Город:", answer["city"])
    print("Погода:", answer["description"])
    print("Температура:", answer["temp"], "°C")
    print("Влажность:", answer["humidity"], "%")
    print("Давление:", answer["pressure"], "мм рт. ст.")
