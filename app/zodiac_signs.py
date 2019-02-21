def zodiac_sign(day, month):
    if month == 3 and 21 <= day <= 31 or month == 4 and 1 <= day <= 20:
        return "Овен"
    elif month == 4 and 21 <= day <= 30 or month == 5 and 1 <= day <= 21:
        return "Телец"
    elif month == 5 and 22 <= day <= 31 or month == 6 and 1 <= day <= 21:
        return "Близнецы"
    elif month == 6 and 22 <= day <= 30 or month == 7 and 1 <= day <= 22:
        return "Рак"
    elif month == 7 and 23 <= day <= 31 or month == 8 and 1 <= day <= 21:
        return "Лев"
    elif month == 8 and 22 <= day <= 31 or month == 9 and 1 <= day <= 23:
        return "Дева"
    elif month == 9 and 24 <= day <= 30 or month == 10 and 1 <= day <= 23:
        return "Весы"
    elif month == 10 and 24 <= day <= 31 or month == 11 and 1 <= day <= 22:
        return "Скорпион"
    elif month == 11 and 23 <= day <= 30 or month == 12 and 1 <= day <= 22:
        return "Стрелец"
    elif month == 12 and 23 <= day <= 31 or month == 1 and 1 <= day <= 20:
        return "Козерог"
    elif month == 1 and 21 <= day <= 31 or month == 2 and 1 <= day <= 19:
        return "Водолей"
    elif month == 2 and 20 <= day <= 29 or month == 3 and 1 <= day <= 20:
        return "Рыбы"

    return "Ошибка ввода даты рождения"

