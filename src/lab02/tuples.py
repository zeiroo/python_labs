def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента в строку.

    rec: кортеж (fio, group, gpa).
    Возвращает строку вида 'Иванов И.И., гр. BIVT-25, GPA 4.60'.
    ФИО может состоять из 2 или 3 слов, лишние пробелы убираются,
    фамилия приводится к виду 'Фамилия', инициалы - в верхнем регистре.

    Исключения:
        TypeError  - rec не кортеж, fio или group не str, либо gpa не float;
        ValueError - в rec не 3 элемента, пустое ФИО или группа,
                     в ФИО не 2-3 слова, GPA вне диапазона 0..5.
    """
    if type(rec) != tuple:
        raise TypeError("запись должна быть кортежем tuple")
    if len(rec) != 3:
        raise ValueError("в записи должно быть ровно 3 элемента: fio, group, gpa")

    fio, group, gpa = rec

    if type(fio) != str:
        raise TypeError("fio должно быть строкой (str)")
    if type(group) != str:
        raise TypeError("group должна быть строкой (str)")
    if type(gpa) != float:
        raise TypeError("gpa должен быть числом типа float")

    parts = fio.split()
    group = group.strip()

    if not parts:
        raise ValueError("пустое ФИО")
    if not group:
        raise ValueError("пустая группа")
    if len(parts) < 2:
        raise ValueError("в fio меньше 2 слов")
    if len(parts) > 3:
        raise ValueError("в fio больше 3 слов")
    if not (0 <= gpa <= 5):
        raise ValueError("GPA вне диапазона 0..5")

    surname = parts[0].capitalize()
    initials = "".join(name[0].upper() + "." for name in parts[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
