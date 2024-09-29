import requests
from bs4 import BeautifulSoup
from loader import bot


def handle_know_you(message):
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'  # URL главной страницы
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        know_you_section = soup.find('div', id='main-dyk', class_='main-block main-box')

        if know_you_section:
            list_items = know_you_section.find_all('li')
            facts_message = "Знаете ли вы?\n\n"
            for line in list_items:
                facts_message += f"-- {line.text.strip()}\n" + "\n"

            # Отправляем сообщение с фактами
            bot.send_message(message.chat.id, facts_message)
        else:
            bot.send_message(message.chat.id, "Не удалось получить факты.")
    else:
        bot.send_message(message.chat.id, "Не удалось получить главную страницу.")