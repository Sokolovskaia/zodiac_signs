from app.zodiac_signs import zodiac_sign


def test_zodiac_sign_aries():  # овен
    result = zodiac_sign(1, 4)
    assert "Овен" == result


def test_zodiac_sign_taurus():  # телец
    result = zodiac_sign(21, 4)
    assert "Телец" == result


def test_zodiac_sign_gemini():  # близнецы
    result = zodiac_sign(21, 6)
    assert "Близнецы" == result


def test_zodiac_sign_cancer():  # рак
    result = zodiac_sign(1, 7)
    assert "Рак" == result


def test_zodiac_sign_leo():  # лев
    result = zodiac_sign(23, 7)
    assert "Лев" == result


def test_zodiac_sign_virgo():
    result = zodiac_sign(23, 9)
    assert "Дева" == result


def test_zodiac_sign_libra():
    result = zodiac_sign(1, 10)
    assert "Весы" == result


def test_zodiac_sign_scorpio():
    result = zodiac_sign(24, 10)
    assert "Скорпион" == result


def test_zodiac_sign_sagittarius():
    result = zodiac_sign(22, 12)
    assert "Стрелец" == result


def test_zodiac_sign_capricorn():
    result = zodiac_sign(1, 1)
    assert "Козерог" == result


def test_zodiac_sign_aquarius():
    result = zodiac_sign(21, 1)
    assert "Водолей" == result


def test_zodiac_sign_pisces():
    result = zodiac_sign(20, 3)
    assert "Рыбы" == result


def test_zodiac_sign_input_error_day():
    result = zodiac_sign(40, 3)
    assert "не известен (ошибка ввода даты рождения)" == result


def test_zodiac_sign_input_error_month():
    result = zodiac_sign(1, 18)
    assert "не известен (ошибка ввода даты рождения)" == result
