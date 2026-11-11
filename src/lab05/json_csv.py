from pathlib import Path
import csv, json

from src.lab04.io_txt_csv import ensure_parent_dir

def check_extension(path: str | Path, extension: str):
    if Path(path).suffix.lower() != extension:
        raise ValueError(f"Ожидается файл {extension}: {path}")

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Колонки идут в порядке первого появления ключей.
    """

    check_extension(json_path, ".json")
    check_extension(csv_path, ".csv")

    text = Path(json_path).read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    data = json.loads(text)
    if not isinstance(data, list) or not data or not all(isinstance(row, dict) for row in data):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    header = []
    for item in data:
        for key in item:
            if not key.strip() or isinstance(item[key], (list, dict)):
                raise ValueError("Ожидаются непустые ключи и плоские значения")
            if key not in header:
                header.append(key)

    if not header:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    ensure_parent_dir(csv_path)
    with Path(csv_path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, restval="")
        w.writeheader()
        w.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    check_extension(csv_path, ".csv")
    check_extension(json_path, ".json")

    header, records = read_csv(csv_path)
    rows = [dict(zip(header, row)) for row in records]

    ensure_parent_dir(json_path)
    with Path(json_path).open("w", encoding="utf-8", newline="") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

def read_csv(csv_path: str | Path) -> tuple[list[str], list[list[str]]]:
    """Читает CSV: запятая, UTF-8, уникальные заголовки, одинаковая длина строк."""
    check_extension(csv_path, ".csv")
    try:
        with Path(csv_path).open(encoding="utf-8", newline="") as file:
            reader = csv.reader(file, strict=True)
            header = next(reader, None)
            if not header or any(not name.strip() for name in header):
                raise ValueError("CSV пуст или содержит пустые названия колонок")
            if len(set(header)) != len(header):
                raise ValueError("Названия колонок должны быть уникальными")
            rows = []
            for row in reader:
                if not row:
                    continue
                if len(row) != len(header):
                    raise ValueError("Количество полей не совпадает с заголовком")
                rows.append(row)
    except csv.Error as error:
        raise ValueError("Некорректный CSV") from error
    if not rows:
        raise ValueError("CSV не содержит записей")
    return header, rows


def main() -> None:
    """Демонстрация JSON-CSV: py -m src.lab05.json_csv."""
    samples = "data/lab05/samples"
    out = "data/lab05/out"
    json_to_csv(f"{samples}/people.json", f"{out}/people_from_json.csv")
    print("people.json -> people_from_json.csv")
    csv_to_json(f"{samples}/people.csv", f"{out}/people_from_csv.json")
    print("people.csv -> people_from_csv.json")
    json_to_csv(f"{samples}/students.json", f"{out}/students_from_json.csv")
    print("students.json -> students_from_json.csv")
    csv_to_json(f"{samples}/cities.csv", f"{out}/cities_from_csv.json")
    print("cities.csv -> cities_from_csv.json")


if __name__ == "__main__":
    main()
