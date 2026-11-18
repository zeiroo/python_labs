# Скриншоты ЛР6

Четыре снимка терминала, как в отчёте Артемия: текст, конвертации, справка, ошибки.
Все команды выполнять из корня проекта. Перед каждым блоком можно выполнить `cls`.
На снимке должны быть видны введённые команды и их вывод. При необходимости увеличьте
высоту терминала или уменьшите его шрифт, чтобы весь блок поместился.

## 1. image_text.png — текстовые команды

```powershell
py -m src.lab06.cli_text cat --input data/lab05/samples/people.csv -n
py -m src.lab06.cli_text stats --input data/lab06/samples/stats.txt --top 5
```

На снимке: CSV с номерами строк и статистика текста — 15 слов, 9 уникальных,
python/слова/текст по 3 вхождения.

## 2. image_convert.png — конвертации

```powershell
py -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/out/people.csv
py -m src.lab06.cli_convert csv2json --in data/lab05/samples/people.csv --out data/out/people.json
py -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/people.csv --out data/out/people.xlsx
```

На снимке: три команды и три сообщения «Готово». Отдельный снимок Excel для
четырёх снимков по образцу Артемия не нужен.

## 3. image_help.png — справка

```powershell
py -m src.lab06.cli_convert --help
py -m src.lab06.cli_text stats --help
```

На снимке: перечень трёх конвертаций и параметры stats, включая --input и --top.
Это те же два примера справки, что показаны в отчёте Артемия.
Справку остальных подкоманд также нужно проверить — команды перечислены в общем отчёте,
но помещать всю справку на этот снимок не требуется.

## 4. image_errors.png — ошибки

```powershell
py -m src.lab06.cli_text cat --input missing.txt
py -m src.lab06.cli_text stats --input data/lab06/samples/stats.txt --top abc
```

На снимке: сообщение об отсутствующем файле и об ошибке преобразования --top в int.
Эти ошибки ожидаются: для снимка их исправлять не нужно.

## Куда сохранить

Сохранить четыре PNG в эту папку с указанными именами. Например, через Win+Shift+S,
затем сохранить снимок, а не только скопировать в буфер обмена.
Ссылки уже добавлены в соответствующие разделы общего [README](../../README.md).
После сохранения файлов они появятся в отчёте без дополнительных правок Markdown.
