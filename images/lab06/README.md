# Скриншоты ЛР6

Нужны настоящие скриншоты терминала после выполнения команд из корня проекта.
Файлы не нужно рисовать или заменять картинками с набранным вручную выводом.
Если группа команд не помещается, сделайте несколько снимков с суффиксами `_1`, `_2`.

## 1. image_text.png — cat и stats

```powershell
py -m src.lab06.cli_text cat --input data/lab05/samples/people.csv -n
py -m src.lab06.cli_text stats --input data/lab06/samples/stats.txt --top 5
```

Должны быть видны команда, строки CSV с номерами и результат статистики:
15 слов, 9 уникальных, python/слова/текст по 3 вхождения.

## 2. image_convert.png — все конвертации

```powershell
py -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/out/people.csv
py -m src.lab06.cli_convert csv2json --in data/lab05/samples/people.csv --out data/out/people.json
py -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/people.csv --out data/out/people.xlsx
Get-Content data/out/people.csv
Get-Content data/out/people.json
```

Должны быть видны три сообщения «Готово» и содержимое результатов.

## 3. image_xlsx.png — таблица

Откройте [people.xlsx](../../data/out/people.xlsx) в Excel или LibreOffice Calc.
На снимке должны быть видны Sheet1, заголовок name/age/city и 5 записей.

## 4. image_help_text.png — справка текстовых команд

```powershell
py -m src.lab06.cli_text --help
py -m src.lab06.cli_text cat --help
py -m src.lab06.cli_text stats --help
```

## 5. image_help_convert.png — справка конвертеров

```powershell
py -m src.lab06.cli_convert --help
py -m src.lab06.cli_convert json2csv --help
py -m src.lab06.cli_convert csv2json --help
py -m src.lab06.cli_convert csv2xlsx --help
```

Справку каждой подкоманды нужно проверить; при необходимости сохраните два снимка.

## 6. image_errors.png — ошибки

```powershell
py -m src.lab06.cli_text cat --input missing.txt
py -m src.lab06.cli_text stats --input data/lab06/samples/stats.txt --top abc
py -m src.lab06.cli_text stats --input data/lab06/samples/stats.txt --top -1
py -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json
```

Должны быть понятные сообщения без traceback.

## После сохранения снимков

Добавьте в раздел ЛР6 общего [README](../../README.md) изображения:

```markdown
![Вывод текста и статистика](images/lab06/image_text.png)
![Конвертации](images/lab06/image_convert.png)
![Таблица XLSX](images/lab06/image_xlsx.png)
![Справка текстовых команд](images/lab06/image_help_text.png)
![Справка конвертеров](images/lab06/image_help_convert.png)
![Обработка ошибок](images/lab06/image_errors.png)
```

Пути выше рассчитаны на общий README в корне проекта.
Если снимки разбиты на части, добавьте ссылки на каждую часть.
