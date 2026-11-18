"""CLI-оболочка над конвертерами ЛР5."""

import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертация JSON, CSV и XLSX")
    commands = parser.add_subparsers(dest="command", required=True)
    json_parser = commands.add_parser("json2csv", help="Преобразовать JSON в CSV")
    json_parser.add_argument("--in", dest="input", required=True, help="Входной JSON")
    json_parser.add_argument("--out", dest="output", required=True, help="Выходной CSV")

    csv_parser = commands.add_parser("csv2json", help="Преобразовать CSV в JSON")
    csv_parser.add_argument("--in", dest="input", required=True, help="Входной CSV")
    csv_parser.add_argument("--out", dest="output", required=True, help="Выходной JSON")

    xlsx_parser = commands.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")
    xlsx_parser.add_argument("--in", dest="input", required=True, help="Входной CSV")
    xlsx_parser.add_argument("--out", dest="output", required=True, help="Выходной XLSX")
    args = parser.parse_args()
    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except ValueError as error:
        parser.error(str(error))
    print(f"Готово: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
