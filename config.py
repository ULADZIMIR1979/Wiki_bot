import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Получаем токен из переменной окружения
