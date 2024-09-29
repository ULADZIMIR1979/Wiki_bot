# import requests
# from bs4 import BeautifulSoup
# from loader import bot
# from database.models import UserRequest
#
#
# def get_dictionary_info(query):
#     url = f'https://ru.wiktionary.org/wiki/{query}'  # Формируем URL для запроса
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Извлекаем нужную информацию из страницы
#         definition_section = soup.find('div', class_='mw-parser-output')
#
#         if definition_section:
#             definitions = []
#             for item in definition_section.find_all(['ol', 'ul']):
#                 for li in item.find_all('li'):
#                     definitions.append(li.text.strip())
#             return definitions if definitions else ["Определение не найдено."]
#
#     return ["Ошибка при получении данных. Проверьте правильность введённых данных"]
#
#
# def handle_dictionary(message):
#     msg = bot.send_message(message.chat.id, "Введите слово для поиска:")
#     bot.register_next_step_handler(msg, process_dictionary_input)
#
#
# def process_dictionary_input(message):
#     query = message.text.strip()  # Получаем текст запроса
#     definitions = get_dictionary_info(query)
#     user_id = message.from_user.id
#
#     # Сохраняем запрос в базе данных.
#     UserRequest.create(user_id=user_id, query=query)
#
#     # Формируем сообщение с определениями
#     definitions_message = f"Результаты для слова '{query}':\n\n" + "\n".join(definitions)
#
#     max_length = 4096
#     if len(definitions_message) > max_length:
#         for i in range(0, len(definitions_message), max_length):
#             bot.send_message(message.chat.id, definitions_message[i:i + max_length])
#     else:
#         bot.send_message(message.chat.id, definitions_message)