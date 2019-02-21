from app.zodiac_signs import zodiac_sign


def test_zodiac_sign_aries():
    assert "Овен" == zodiac_sign(1, 4)


def test_zodiac_sign_taurus():
    assert "Телец" == zodiac_sign(21, 4)


def test_zodiac_sign_gemini():
    assert "Близнецы" == zodiac_sign(21, 6)


def test_zodiac_sign_cancer():
    assert "Рак" == zodiac_sign(1, 7)


def test_zodiac_sign_leo():
    assert "Лев" == zodiac_sign(23, 7)


def test_zodiac_sign_virgo():
    assert "Дева" == zodiac_sign(23, 9)


def test_zodiac_sign_libra():
    assert "Весы" == zodiac_sign(1, 10)


def test_zodiac_sign_scorpio():
    assert "Скорпион" == zodiac_sign(24, 10)


def test_zodiac_sign_sagittarius():
    assert "Стрелец" == zodiac_sign(22, 12)


def test_zodiac_sign_capricorn():
    assert "Козерог" == zodiac_sign(1, 1)


def test_zodiac_sign_aquarius():
    assert "Водолей" == zodiac_sign(21, 1)


def test_zodiac_sign_pisces():
    assert "Рыбы" == zodiac_sign(20, 3)


def test_zodiac_sign_input_error_day():
    assert "Ошибка ввода даты рождения" == zodiac_sign(40, 3)
