"""Конвертация CSV в XLSX через openpyxl."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from .json_csv import check_extension, read_csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Создаёт Sheet1 с шириной колонок по тексту, минимум 8 символов."""
    check_extension(xlsx_path, ".xlsx")
    header, rows = read_csv(csv_path)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"
    for row in [header, *rows]:
        sheet.append(row)
    for row in sheet:
        for cell in row:
            cell.data_type = "s"  # Сохраняем CSV как текст, включая строки с '='.
    for number, column in enumerate(zip(header, *rows), start=1):
        width = max(len(line) for value in column for line in (value.splitlines() or [""]))
        sheet.column_dimensions[get_column_letter(number)].width = min(255, max(8, width + 2))
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    workbook.save(xlsx_path)
    workbook.close()


def main() -> None:
    """Примеры преобразования CSV в XLSX."""
    csv_to_xlsx("data/lab05/samples/people.csv", "data/lab05/out/people.xlsx")
    print("people.csv -> people.xlsx")
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")
    print("cities.csv -> cities.xlsx")


if __name__ == "__main__":
    main()
