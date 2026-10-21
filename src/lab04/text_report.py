"""ЛР4, задание B: отчёт по частотам слов из текстового файла.

Читает текст, считает частоты функциями из ЛР3 (src/lib/text.py),
сохраняет все слова в CSV и печатает краткое резюме в консоль.

Запуск из корня проекта:
    py -m src.lab04.text_report
    py -m src.lab04.text_report --in data/lab04/input.txt --out data/lab04/report.csv
"""

from src.lib import text
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
import argparse
import sys

def prepare_pargs() -> argparse.Namespace:
    """Разобрать аргументы командной строки.

    Returns:
        Namespace с полями input, output и encoding.
    """
    parser = argparse.ArgumentParser(
        description="Считает частоты слов в текстовом файле и сохраняет отчёт в CSV."
    )
    # dest="input", потому что args.in - синтаксическая ошибка (in - ключевое слово)
    parser.add_argument("--in", dest="input", default="data/lab04/input.txt",
                        help="входной текстовый файл (по умолчанию data/lab04/input.txt)")
    parser.add_argument("--out", dest="output", default="data/lab04/report.csv",
                        help="CSV-отчёт word,count (по умолчанию data/lab04/report.csv)")
    parser.add_argument("--encoding", dest="encoding", default="utf-8",
                        help="кодировка входного файла (по умолчанию utf-8), например cp1251")
    return parser.parse_args()

def get_text(path: str, encoding: str) -> str:
    """Прочитать входной файл, а при ошибке сообщить причину и выйти с кодом 1.

    read_text ошибки не перехватывает, это делаем здесь, чтобы пользователь
    увидел понятное сообщение вместо трассировки.

    Args:
        path: путь к входному файлу.
        encoding: кодировка файла.

    Returns:
        Содержимое файла.
    """
    try:
        return read_text(path, encoding=encoding)
    except FileNotFoundError:
        print(f"Файл не найден: {path}", file=sys.stderr)
    except UnicodeDecodeError:
        print(f"Файл {path} не читается в кодировке {encoding}", file=sys.stderr)
    sys.exit(1)

def main() -> None:
    """Прочитать файл, посчитать частоты, записать CSV и вывести резюме."""
    args = prepare_pargs()

    raw = get_text(args.input, args.encoding)

    tokens = text.tokenize(text.normalize(raw))
    freq = text.count_freq(tokens)
    all_pairs = text.top_n(freq, len(freq))

    ensure_parent_dir(args.output)
    write_csv(all_pairs, args.output, ("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in text.top_n(freq, 5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
