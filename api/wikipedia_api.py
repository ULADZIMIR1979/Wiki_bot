import wikipedia


def get_wiki_info(query):
    try:
        wikipedia.set_lang('ru')  # Установка языка
        summary = wikipedia.summary(query)
        page_url = wikipedia.page(query).url
        return summary, page_url

    except wikipedia.exceptions.WikipediaException as e:
        return None, f'{e}\nНе удалось найти информацию по запросу. Проверьте, правильно ли введён запрос.'

