import datetime


def get_month_number(month_input):
    """Преобразует текст или число в номер месяца."""
    months_map = {
        "январь": 1, "января": 1, "февраль": 2, "февраля": 2,
        "март": 3, "марта": 3, "апрель": 4, "апреля": 4,
        "май": 5, "мая": 5, "июнь": 6, "июня": 6,
        "июль": 7, "июля": 7, "август": 8, "августа": 8,
        "сентябрь": 9, "сентября": 9, "октябрь": 10, "октября": 10,
        "ноябрь": 11, "ноября": 11, "декабрь": 12, "декабря": 12
    }
    val = month_input.strip().lower()
    if val.isdigit():
        return int(val)
    return months_map.get(val, 0)


def get_day_info(d, m, y):
    """Возвращает день недели, признак високосности и возраст."""
    date_obj = datetime.date(y, m, d)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    today = datetime.date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))

    return days[date_obj.weekday()], is_leap, age


def print_digital_date(d, m, y):
    """Рисует дату на табло, используя визуальные шаблоны из кода."""
    # Цифры прописаны так, что их силуэт виден сразу
    templates = {
        '0': [" *** ",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        '1': ["  *  ",
              " **  ",
              "  *  ",
              "  *  ",
              " *** "],
        '2': [" *** ",
              "    *",
              " *** ",
              "*    ",
              " *** "],
        '3': [" *** ",
              "    *",
              " *** ",
              "    *",
              " *** "],
        '4': ["*   *",
              "*   *",
              " *** ",
              "    *",
              "    *"],
        '5': [" *** ",
              "*    ",
              " *** ",
              "    *",
              " *** "],
        '6': [" *** ",
              "*    ",
              " *** ",
              "*   *",
              " *** "],
        '7': [" *** ",
              "    *",
              "   * ",
              "  *  ",
              " *   "],
        '8': [" *** ",
              "*   *",
              " *** ",
              "*   *",
              " *** "],
        '9': [" *** ",
              "*   *",
              " *** ",
              "    *",
              " *** "],
        ' ': ["     ",
              "     ",
              "     ",
              "     ",
              "     "]
    }

    date_str = f"{d:02d} {m:02d} {y:04d}"

    for row in range(5):
        line = ""
        for char in date_str:
            line += templates[char][row] + "  "
        print(line)


# Запуск программы
try:
    day_in = int(input("Введите день: "))
    month_raw = input("Введите месяц (число или название): ")
    year_in = int(input("Введите год: "))

    month_in = get_month_number(month_raw)

    # Проверка на существование даты (например, 31 июня выдаст ошибку)
    day_week, leap, age = get_day_info(day_in, month_in, year_in)

    print(f"\n--- Результаты ---")
    print(f"День недели: {day_week}")
    print(f"Високосный год: {'Да' if leap else 'Нет'}")
    print(f"Возраст: {age} лет")
    print(f"------------------\n")

    print_digital_date(day_in, month_in, year_in)

except (ValueError, TypeError):
    print("Ошибка: Введена некорректная дата или месяц.")
