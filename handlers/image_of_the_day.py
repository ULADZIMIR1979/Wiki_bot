import requests
from bs4 import BeautifulSoup
from loader import bot


def image_of_the_day_command(message):
    # URL страницы с изображением
    url = ('https://ru.wikipedia.org/wiki/'
           '%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

    # Загружаем HTML страницу
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим div с классом "fake-heading h2 main-header" и текстом "Изображение дня"
        div_tag = soup.find('div', class_="fake-heading h2 main-header", string="Изображение дня")

        if div_tag:
            # Ищем первое изображение внутри найденного div
            img_tag = div_tag.find_next('img')

            if img_tag:
                # Извлекаем src атрибут и конструируем полный URL изображения
                img_url = 'https:' + img_tag['src']

                # Отправляем изображение пользователю
                bot.send_photo(message.chat.id, img_url)
            else:
                bot.send_message(message.chat.id, "Изображение не найдено в данном разделе.")
        else:
            bot.send_message(message.chat.id, "Раздел 'Изображение дня' не найден.")
    else:
        bot.send_message(message.chat.id, f"Ошибка при загрузке страницы. Статус: {response.status_code}")