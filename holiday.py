import requests


API_KEY = "be8ac074-0dae-47e7-939d-9ca141937053"
URL = "https://www.holidayapi.com/v1/holidays"


class HolidayAPI:

    def __init__(self, api_key=API_KEY, url=URL):
        self.api_key = api_key
        self.url = url

    def get_holidays(self, country, year, month=None, language="ru"):

        params = {
            "key": self.api_key,
            "country": country,
            "year": year,
            "language": language
        }

        if month:
            params["month"] = month

        res = requests.get(self.url, params=params)

        if res.ok:
            data = res.json()

            result = []

            for holiday in data["holidays"]:
                info = {
                    "name": holiday["name"],
                    "date": holiday["date"],
                    "observed": holiday["observed"],
                    "country": holiday["country"],
                    "public": holiday["public"],
                    "weekday": holiday["weekday"]["date"]["name"],
                    "uuid": holiday["uuid"]
                }

                result.append(info)

            return result

        else:
            print("Ошибка:", res.status_code)
            return None


if __name__ == "__main__":

    api = HolidayAPI()

    holidays = api.get_holidays("RU", "2025", 5, "ru")

    if holidays:

        print("Праздники:\n")

        for holiday in holidays[:5]:

            print(f"Название: {holiday['name']}")
            print(f"Дата: {holiday['date']}")
            print(f"День недели: {holiday['weekday']}")
            print(f"Наблюдается: {holiday['observed']}")
            print(f"Страна: {holiday['country']}")
            print(f"Государственный: {holiday['public']}")
            print("-" * 40)