from unittest import result
import requests
from bs4 import BeautifulSoup   # импортируем библиотеку которая берет на вход строку хтмл док и преобразует его в дерево элементов где можно делать поиск

def get_html(url):  #создаем ФУНКЦИЯ КОТОРАЯ ПРИНИМАЕТ юрл
    try:   #создаем исключения
        result = requests.get(url)   #переменая которая получает (юрл)
        result.raise_for_status()   
        return result.text #  елси все хорошо возвращаем текст
    except(requests.RequestException, ValueError):  # если сетевая проблема и если ошибка сервера
        print('Сетевая ошибка')
        return False

def get_python_news():
    html = get_html('https://www.python.org/blogs/')  #вот сам юрл в переменной html
    if html:
        soup = BeautifulSoup(html, 'html.parser')  
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')  #делаем поиск юрл класс и лист
        # all_news = all_news.findAll('li')
        # print(all_news)
        result_news = []
        for news in all_news:
            title = news.find('a').text #делаем поиск по отдельности 
            url = news.find('a')['href']   #делаем поиск по отдельности 
            published = news.find('time').text   #делаем поиск по отдельности 
            result_news.append({
                'title': title,
                'url': url,
                'published': published
            })  
        return result_news
    return False
            # print(title)
            # print(url)
            # print(published)
 
# if __name__ == '__main__':
    # if html:
    #     news = get_python_news(html)
    #     print(news)

