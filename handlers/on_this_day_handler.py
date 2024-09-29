import requests
from bs4 import BeautifulSoup
from loader import bot


def on_this_day_command(message):
    # URL главной страницы Википедии
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Находим родительский элемент
        main_itd_div = soup.find('div', id='main-itd', class_='main-block main-box')

        if main_itd_div:
            # Находим вложенный элемент с классом 'main-box-content'
            content_div = main_itd_div.find('div', class_='main-box-content')

            if content_div:
                featured_article_text = content_div.find_all('li')
                events_text = "События, произошедшие в этот день:\n\n"

                for line in featured_article_text:
                    events_text += f"- {line.text}\n" + "\n"  # Добавляем события в текст

                bot.send_message(message.chat.id, events_text)
            else:
                bot.send_message(message.chat.id, "Не удалось найти информацию о событиях.")
        else:
            bot.send_message(message.chat.id, "Не удалось найти информацию о событиях.")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка при получении данных с Википедии.")
