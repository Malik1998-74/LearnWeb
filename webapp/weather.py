# import json
# from sqlite3 import paramstyle
# from unittest import result
from flask import current_app
import requests   # импортируем библдиотеку (запрос)

def weather_by_city(city_name): # создаем функция которая принимает название города
    weather_url = current_app.config['WEATHER_URL'] #добовляем сайт (базу) где будем брать данные вместо юрл сделали current_aoo.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': '1',
        'lang': 'ru'
    }   # создаем словарь параметры ключ значение
    try:  #(ищем исключения)
        result = requests.get(weather_url, params=params)  #создаем результат получения URL и параметров
        result.raise_for_status() #(сходить на сервер вернуть результат)Он сгенерирует исключение если сервер ответил кодом, начинающимся с 4xx или 5xx
        weather = result.json()  # json текстовый формат переделывает в питоновский формат
        if 'data' in weather:  #проверка есть ли секция в weather
            if 'current_condition' in weather['data']: #проверка есть ли секция в weather
                try:
                    return weather['data']['current_condition'][0]  # возвращаем нулевой элемент
                except(IndexError, TypeError):  # вызываем ошибку если ошибка индекса и если current_condition не список
                    return False
    except(requests.RequestException, ValueError): # проверка есть ли нету конекта с сервером (интернетом)
        print('Сетевая ошибка')
        return False
    return False


if __name__ == '__main__':
    w = weather_by_city('Moscow,Russia')
    print(w)

