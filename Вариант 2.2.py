import datetime


def date(date):
    d = datetime.datetime.strptime(date, '%d.%m.%Y')
    day_of_week = (d.weekday() + 1) % 7
    days = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"
    }
    return days[day_of_week]


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        return True
    return False


def year_old(date):
    d = datetime.datetime.strptime(date, '%d.%m.%Y')
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    if d.month < month:
        return year - d.year
    elif d.month == month:
        if d.day <= day:
            return year - d.year
        else:
            return year - d.year - 1
    else:
        return year - d.year - 1


a = input("Введите дату рождения: ")
numberstr = [[],[],[],[],[]]

numbers = {
    "0": [
        "****",
        "*  *",
        "*  *",
        "*  *",
        "****",
    ],

    "1": [
        "   *",
        " * *",
        "*  *",
        "   *",
        "   *",
    ],
    "2": [
        "*****",
        "    *",
        "*****",
        "*    ",
        "*****",
    ],
    "3": [
        "***",
        " * ",
        "***",
        "  *",
        "***",
    ],
    "4": [
        "*  *",
        "*  *",
        "****",
        "   *",
        "   *",
    ],
    "5": [
        "*****",
        "*    ",
        "*****",
        "    *",
        "*****",
    ],
    "6": [
        "*****",
        "*    ",
        "*****",
        "*   *",
        "*****",
    ],
    "7": [
        "*****",
        "   * ",
        "  *  ",
        " *   ",
        "*    ",
    ],
    "8": [
        "*****",
        "*   *",
        "*****",
        "*   *",
        "*****",
    ],
    "9": [
        "*****",
        "*   *",
        "*****",
        "    *",
        "*****",
    ],
    ".": [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
    ]
}
for i in a:
    for j in range(5):
        numberstr[j].append(numbers[i][j])
for i in numberstr:
    print(*i)

print(f"Вы родились в {date(a)}")

print(f"Вам {year_old(a)} лет")

n = leap_year(year := int(input("Введите год: ")))
if n:
    n = "висакосный"
else:
    n = "не висакосный"
print(f"{year} год {n}")
