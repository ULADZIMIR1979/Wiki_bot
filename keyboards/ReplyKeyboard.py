from telebot import types


def create_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Start")
    help_button = types.KeyboardButton("Help")
    search_button = types.KeyboardButton("Search")
    history_button = types.KeyboardButton("История запросов")
    on_this_day_button = types.KeyboardButton("В этот день")
    featured_article_button = types.KeyboardButton("Избранная статья")
    image_of_the_day_button = types.KeyboardButton("Изображение дня")
    know_you_button = types.KeyboardButton("Знаете ли вы?")

    markup.add(start_button, help_button, search_button, history_button,
               on_this_day_button, featured_article_button, image_of_the_day_button, know_you_button)
    return markup
