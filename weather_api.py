import requests
from pprint import pprint

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat: float, lon: float) -> dict:
    """
    Получает текущие погодные условия для заданной географической координаты.
    Производит запрос к внешнему API погоды (WeatherAPI)
    и обрабатывает ответ для краткой сводки погоды.

    Args:
        lat (float): Широта местоположения в десятичных градусах
                     Должна быть в диапазоне (-90, 90)
        lon (float): Долгота местоположения в десятичных градусах
                     Должна быть в диапазоне (-180, 180)
    Returns:
        dict: Словарь с текущими данными о погоде
    Raises:
        ValueError: Если широта или долгота находятся вне
                    допустимого диапазона.


    """
    try:
        if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
            raise ValueError('Указанное местоположение выходит из существующего диапазона.')

        params = {
            'key': '6d1fb8fe0672484a88a52901252911',
            'q': f'{lat},{lon}'
        }
        url = f"https://api.weatherapi.com/v1/current.json"
        response = requests.get(url, params=params)
        data = response.json()

        # Данная реализация приведена для api.weatherapi.com
        result = {
            'city': data['location']['name'],  # Город
            'time': data['current']['last_updated'],  # Время обновления данных
            'temp': data['current']['temp_c'],  # Температура
            'feels_like_temp': data['current']['feelslike_c'],  # Ощущаемая температура
            'pressure': data['current']['pressure_mb'],  # Давление
            'humidity': data['current']['humidity'],  # Влажность
            'wind_speed': data['current']['wind_kph'],  # Скорость ветра
            'wind_gust': data['current']['gust_kph'],  # Скорость порыва ветра
            'wind_dir': DIRECTION_TRANSFORM.get(data['current']['wind_dir'].lower()),  # Направление ветра
        }
        return result

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    pprint(current_weather(59.93, 30.31)) # Проверка работы для координат Санкт-Петербурга
    print()
    pprint(current_weather(99, -181))  # Проверка неправильных координат