from src.lib import text 

table_flag = True

def table_print(top: list[tuple[str, int]]) -> None:
    """Печатает топ слов в виде таблицы

    Ширина первого столбца равна длине самого длинного слова в топе
    (но не меньше длины заголовка "слово")
    """
    width = len("слово")
    for key, value in top:
        if len(key) > width:
            width = len(key)

    print(f"{'слово':<{width}} | частота")
    print("-" * (width + 10))
    for key, value in top:
        print(f"{key:<{width}} | {value}")


def main(data: str) -> None:
    """Считает статистику текста и печатает результат

    Нормализует и разбивает строку на слова, считает всего слов, уникальные
    слова и топ-5 самых частых. Формат вывода зависит от table_flag:
    таблица или обычные строки слово:кол-во
    """
    norm_data = text.normalize(data)
    tokens = text.tokenize(norm_data)
    length = len(tokens)

    freq = text.count_freq(tokens)
    unique_words = len(freq)

    top = text.top_n(freq, 5)

    print(f"Всего слов: {length}\nУникальных слов: {unique_words}\nТоп-5:")
    if not table_flag:
        for key, value in top:
            print(f"{key}:{value}")
    else:
        table_print(top)

main(input())