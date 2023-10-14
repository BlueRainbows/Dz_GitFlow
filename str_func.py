def foo():
    string = input("Введите ваш текст ").upper()
    return string


def foo_2():
    """Эта функция принимает строку и возвращает её переводя первый символ в верхний регистр"""
    string = input("Введите ваш текст ").title()
    return string
