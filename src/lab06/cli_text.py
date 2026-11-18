import argparse

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text

def run_cat(path: str, numbered: bool) -> None:
    """Выводит UTF-8 файл построчно, при необходимости с номерами."""
    lines = read_text(path).splitlines()
    for number, line in enumerate(lines, start=1):
        if numbered:
            print(f"{number}: {line}")
        else:
            print(line)

def run_stats(path: str, top: int) -> None:
    """Печатает общее число слов, число уникальных и топ слов."""
    content = read_text(path)

    normalized = normalize(content)
    words = tokenize(normalized)
    frequencies = count_freq(words)
    popular = top_n(frequencies, top)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print(f"Топ-{top}:")

    for word, count in popular:
        print(f"{word}:{count}")

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к UTF-8 файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к UTF-8 файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов в топе (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "stats" and args.top <= 0:
        parser.error("--top должен быть положительным числом")

    try:
        if args.command == "cat":
            run_cat(args.input, args.n)
        elif args.command == "stats":
            run_stats(args.input, args.top)
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except UnicodeDecodeError:
        parser.error("Входной файл должен быть в кодировке UTF-8")


if __name__ == "__main__":
    main()
