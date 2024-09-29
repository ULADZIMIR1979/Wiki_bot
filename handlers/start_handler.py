from telebot import types
from database.models import User
from keyboards.ReplyKeyboard import create_reply_keyboard


def create_user(user_id, username):
    user, created = User.get_or_create(user_id=user_id, defaults={'username': username})
    return user, created


def start_command(bot, message):
    user_id = message.from_user.id
    username = message.from_user.first_name

    # Регистрация пользователя в базе данных.
    user, created = create_user(user_id, username)

    markup = create_reply_keyboard()

    if created:
        bot.send_message(message.chat.id, f"Добро пожаловать! Вы зарегистрированы как <b>{username}</b>.\n"
                                          f"Я бот, который, по заданному слову или словосочетанию, "
                                          f"выдаёт информацию из Википедии.\n"
                                          f"Что бы узнать больше информации о том, как я работаю, "
                                          f"нажмите на кнопку <b>Help</b>.",
                         reply_markup=markup, parse_mode="HTML"
                         )
    else:
        bot.send_message(message.chat.id, f"Рад снова приветствовать вас, <b>{username}</b> !\n"
                                          f"Нажмите на кнопку  <b>Help</b>,  если вам нужна помощь.",
                         reply_markup=markup, parse_mode="HTML"
                         )


def send_start_button(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Start")
    markup.add(start_button)

    bot.send_message(chat_id, "Нажмите кнопку  <b>Start</b>  для регистрации:",
                     reply_markup=markup, parse_mode="HTML"
                     )
