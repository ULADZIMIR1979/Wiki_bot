import telebot
from config import BOT_TOKEN



# Импортируем модели и создаем таблицы базы данных при запуске.
import database.db as db

bot = telebot.TeleBot(BOT_TOKEN)

# Создаем таблицы базы данных при запуске.
db.create_tables()

# Импортируем обработчики команд.
import handlers.start_handler as start_handler
import handlers.history_handler as history_handler
import handlers.search_handler as search_handler
import handlers.help_handler as help_handler
import handlers.on_this_day_handler as on_this_day_handler
import handlers.featured_article_handler as featured_article_handler
import handlers.image_of_the_day as image_of_the_day_handler
import handlers.know_you_handler as know_you_handler


@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler.send_start_button(bot, message.chat.id)  # Отправляем кнопку "Start"


@bot.message_handler(func=lambda message: message.text == "Start")
def handle_start(message):
    start_handler.start_command(bot, message)  # Передаем объект бота


@bot.message_handler(func=lambda message: message.text == "История запросов")
def handle_history(message):
    history_handler.history_command(message)  # Обработка истории


@bot.message_handler(func=lambda message: message.text == "Search")
def handle_search(message):
    search_handler.search_command(bot, message)  # Передаем объект бота


@bot.message_handler(func=lambda message: message.text == "Help")
def handle_help(message):
    help_handler.help_command(message)  # Обработка запроса помощи


@bot.message_handler(func=lambda message: message.text == "В этот день")
def handle_on_this_day(message):
    on_this_day_handler.on_this_day_command(message)  # Обработка события "В этот день"


@bot.message_handler(func=lambda message: message.text == "Избранная статья")
def handle_featured_article(message):
    featured_article_handler.featured_article_command(message) # Обработка события "Избранная статья"


@bot.message_handler(func=lambda message: message.text == "Изображение дня")
def handle_image_of_the_day(message):
    image_of_the_day_handler.image_of_the_day_command(message)  # Обработка изображения дня


@bot.message_handler(func=lambda message: message.text == "Знаете ли вы?")
def handle_know_you(message):
    know_you_handler.handle_know_you(message)  # Обработка фактов "Знаете ли вы?"