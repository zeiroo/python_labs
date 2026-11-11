"""Запуск всех примеров пятой лабораторной."""

from .json_csv import main as json_csv_main
from .csv_xlsx import main as csv_xlsx_main


def main() -> None:
    json_csv_main()
    csv_xlsx_main()


if __name__ == "__main__":
    main()
