import requests
from bs4 import BeautifulSoup
from loader import bot


def featured_article_command(message):
    # URL главной страницы Википедии
    url = ('https://ru.wikipedia.org/wiki/'
           '%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

    try:
        # Отправляем GET-запрос
        response = requests.get(url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Создаем объект BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            featured_article_div = soup.find('div', class_='main-box-content')

            if featured_article_div:
                featured_article_text = featured_article_div.text.strip()
                bot.send_message(message.chat.id, f"Избранная статья:\n{featured_article_text}"
                                                  f"\nСсылка на статью:\n{url}")
            else:
                bot.send_message(message.chat.id, "Не удалось найти избранную статью.")
        else:
            bot.send_message(message.chat.id, "Произошла ошибка при получении данных с Википедии.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")