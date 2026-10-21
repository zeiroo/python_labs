import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл целиком и возвращает его содержимое одной строкой.

    Args:
        path: путь к файлу (строка или Path).
        encoding: кодировка файла, по умолчанию "utf-8". Если файл в другой
            кодировке, передайте её явно, например:
            read_text("data/lab04/input.txt", encoding="cp1251").

    Returns:
        Содержимое файла. Для пустого файла возвращается пустая строка "".

    Raises:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если файл нельзя декодировать в указанной кодировке.
    """
    return Path(path).read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории файла, если их ещё нет.

    Args:
        path: путь к файлу, для которого нужна родительская папка.
            Если папка уже существует, ничего не происходит.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл (разделитель ",", кодировка utf-8).

    Args:
        rows: строки данных (кортежи или списки); все одной длины.
        path: путь к CSV-файлу. Недостающие родительские папки создаются.
        header: необязательный заголовок, записывается первой строкой.

    Raises:
        ValueError: если строки в rows (или header) имеют разную длину.
            В этом случае файл не создаётся.

    Notes:
        Пустой rows и header=None дают пустой файл (0 строк).
        Пустой rows и заданный header дают файл только с заголовком.
    """
    rows = list(rows)

    if header is not None:
        expected_len = len(header)
    elif len(rows) > 0:
        expected_len = len(rows[0])
    else:
        expected_len = 0

    for row in rows:
        if len(row) != expected_len:
            raise ValueError("Все строки должны быть одной длины")

    ensure_parent_dir(path)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for row in rows:
            w.writerow(row)

if __name__ == "__main__":
    write_csv([("привет", 2), ("мир", 1)], "data/lab04/check.csv", header=("word", "count"))
    write_csv([], "data/lab04/empty.csv")
    write_csv([], "data/lab04/header_only.csv", header=("a", "b"))
    try:
        write_csv([("a", 1), ("b",)], "data/lab04/bad.csv")
    except ValueError as e:
        print("ValueError:", e)