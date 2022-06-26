# import re
# import weakref
from distutils.command.config import config
from flask import Flask, render_template

from webapp.python_org_news import get_python_news  #импортируем функция
from webapp.weather import weather_by_city  #из weakref import weather__city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Новости Python'  # заголовок страницы
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        # weather = weather_by_city('Moscow,Russia')  # тут мы добавили погоду по контретному городу
        news_list = get_python_news() # в переменную news_list импортировали функцию из файла python_org_news
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list) 
        
    return app
        # weather = False
        # if weather:
        #     weather_text = f"Погода: {weather['temp_C']}, ощущаеться как {weather['FeelsLikeC']}"
        # else:
        #     weather_text = 'Сервер погоды временно не доступен'

# if __name__ == '__main__':
#     app.run(debug=True)


# тройные ковычки означают что будет перенос строк
# пишем тег открылся<html> тег закрылся</html> между ними тег <head>заголовок страницы которую мы не видим
# тег тайтл с большой буквы
# тег <body> тело то что будет выводиить прогноз погоды например 
# тег <h1> есть несколько уровней заголовок 1,2,3,4,5
# тег <ol> нумерованный список
# тег <li> зоздает лист 
# это шаблон для упрощения кода сюда передаем готовые данные (index.html)
# <html>
#         <head>  
#             <title>{{ page_title }}</title>  передае6м название переменных внутрь шаблона
#         </head>
#         <body>
#             <h1>
#             {%  if weather %}  делаем проверку 
#                 Погода: {{ weather.temp_C }}, ощущаеться как {{weather. FeelsLikeC }}  в круглых скобках это обращение к переменной и значения вызываем через точку
#             {% else %}
#                 Сервер погоды временно не доступен
#             {% endif %} это закрывающий тег для всего if
#         </body>
# </html>
# импортиркуем render_template передаем название шаблона
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
# джава скрипты чтобы работал bootstrap
# <div class='col-8'> это для новостей отклонения 
#    <h2>Новости</h2>
# </div>
# <div class='col-4'> это для прогноза погоды
#    <h2>Прогноз погоды</h2> это колонки так как bootstrap имеет всего 12 колонок