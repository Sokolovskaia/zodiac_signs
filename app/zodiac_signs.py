def zodiac_sign(day, month):
    if month == 3 and 21 <= day <= 31 or month == 4 and 1 <= day <= 20:
        result = "Овен"
    elif month == 4 and 21 <= day <= 30 or month == 5 and 1 <= day <= 21:
        result = "Телец"
    elif month == 5 and 22 <= day <= 31 or month == 6 and 1 <= day <= 21:
        result = "Близнецы"
    elif month == 6 and 22 <= day <= 30 or month == 7 and 1 <= day <= 22:
        result = "Рак"
    elif month == 7 and 23 <= day <= 31 or month == 8 and 1 <= day <= 21:
        result = "Лев"
    elif month == 8 and 22 <= day <= 31 or month == 9 and 1 <= day <= 23:
        result = "Дева"
    elif month == 9 and 24 <= day <= 30 or month == 10 and 1 <= day <= 23:
        result = "Весы"
    elif month == 10 and 24 <= day <= 31 or month == 11 and 1 <= day <= 22:
        result = "Скорпион"
    elif month == 11 and 23 <= day <= 30 or month == 12 and 1 <= day <= 22:
        result = "Стрелец"
    elif month == 12 and 23 <= day <= 31 or month == 1 and 1 <= day <= 20:
        result = "Козерог"
    elif month == 1 and 21 <= day <= 31 or month == 2 and 1 <= day <= 19:
        result = "Водолей"
    elif month == 2 and 20 <= day <= 29 or month == 3 and 1 <= day <= 20:
        result = "Рыбы"
    else:
        result = "не известен (ошибка ввода даты рождения)"
    return result


print(zodiac_sign(30, 8))

#print("Ваш знак Зодиака: ", zodiac_sign(day=int(input("Введите день вашего рождения (от 1 до 31): ")),
                                     #    month=int(input("Введите месяц вашего рождения (от 1 до 12): "))))
