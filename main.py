import math
import random




def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 2 * (a+b)
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = 10 * 20
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * (r**2)
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = (2 * math.pi) * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """
    random.seed("Word")
    l1 = random.randint(0, 100)
    l2 = random.randint(0, 100)
    l3 = random.randint(0, 100)
    l4 = random.randint(0, 100)
    l5 = random.randint(0, 100)
    l6 = random.randint(0, 100)
    l7 = random.randint(0, 100)
    l8 = random.randint(0, 100)
    l9 = random.randint(0, 100)
    l10 = random.randint(0, 100)
    l = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
    # TODO создайте список
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    a = set(l)
    l = list(a)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print(list(d.values()))

    assert isinstance(d, dict)
    assert len(d) == 5


