import wikipedia


def get_wiki_info(query):
    try:
        wikipedia.set_lang('ru')  # Установка языка
        summary = wikipedia.summary(query)
        page_url = wikipedia.page(query).url
        return summary, page_url

    except wikipedia.exceptions.WikipediaException:
        return None, (f'Не удалось найти информацию по вашему запросу.\n'
                      f'Проверьте, правильно ли введён запрос.\n'
                      f'Нажмите на кнопку **Search** и введите ваш запрос ещё раз.')

