from telebot import types
from api.wikipedia_api import get_wiki_info
from database.models import UserRequest


def search_command(bot, message):
    msg = bot.send_message(message.chat.id, "Введите ваш запрос :")
    bot.register_next_step_handler(msg, lambda m: process_query_input(bot, m))  # Передаем bot и сообщение


def process_query_input(bot, message):
    user_id = message.from_user.id
    query = message.text

    # Сохраняем запрос в базе данных.
    UserRequest.create(user_id=user_id, query=query)

    # Поиск в Википедии.
    summary, result_message = get_wiki_info(query)

    # Проверяем длину ответа и разбиваем его на части, если необходимо
    max_length = 4096
    if summary:
        response_text = f"Результаты поиска для  --  ({query}):\n\n{summary}\n\nСсылка на страницу: {result_message}"

        # Проверяем длину сообщения и разбиваем его на части, если необходимо
        if len(response_text) > max_length:
            for i in range(0, len(response_text), max_length):
                bot.send_message(message.chat.id, response_text[i:i + max_length])
        else:
            bot.send_message(message.chat.id, response_text)
    else:
        bot.send_message(message.chat.id, result_message)