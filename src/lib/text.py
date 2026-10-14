import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует строку

    Шаги: приведение к нижнему регистру (``casefold()`` или ``lower()``),
    замена ё/Ё на е/Е (если ``yo2e``), замена \\t, \\r, \\n на пробелы
    схлопывание повторяющихся пробелов и обрезка краёв
    """
    if not isinstance(text, str):
        raise TypeError("текст должен быть строкой")

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")

    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    """Разбить текст на слова

    Слово — буквы/цифры/подчёркивание допускается дефис внутри слова.
    Числа считаются словами эмодзи и прочие символы отбрасываются
    """
    if not isinstance(text, str):
        raise TypeError("текст должен быть строкой")

    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Посчитать частоты слов: слово -> количество вхождений"""
    d = {}
    for name in tokens:
        if not name in d:
            d[name] = 1
        else:
            d[name] += 1
    return d


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Вернуть топ-N пар (слово, частота).

    Сортировка по убыванию частоты при равенстве - по алфавиту слова
    """
    if n < 0:
        raise ValueError("частота должна быть >= 0")

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


if __name__ == "__main__":
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
    print("all good")

    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"aa": 2, "bb": 2, "cc": 1}

    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
    print('good')


