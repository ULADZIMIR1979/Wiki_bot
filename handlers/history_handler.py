from loader import bot
from database.models import UserRequest


def history_command(message):
    user_id = message.from_user.id

    # Получаем последние 10 запросов пользователя из базы данных.
    requests = UserRequest.select().where(UserRequest.user_id == user_id).order_by(UserRequest.timestamp.desc()).limit(
10)

    if requests:
        history_text = "Последние ваши запросы:\n\n"
        for req in requests:
            # Формируем текст с гиперссылкой на каждый запрос
            history_text += (f"- [Запрос: {req.query}](https://ru.wikipedia.org/wiki/{req.query.replace(' ', '_')}) "
                             f"(время: {req.timestamp})\n")

        bot.send_message(message.chat.id, history_text, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "У вас нет истории запросов.")