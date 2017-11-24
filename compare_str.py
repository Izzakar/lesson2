'''Задание: Написать функцию, которая принимает на вход две строки.
    Если строки одинаковые, возвращает 1.
    Если строки разные и первая длиннее, возвращает 2.
    Если строки разные и вторая строка 'learn', возвращает 3.'''


def compare_strings():
    str_one = input("Введите первую строку:")
    str_two = input("Введите вторую строку:")
    if str_one == str_two:
        print(1)
    else:
        if len(str_one) > len(str_two):
            print(2)
        elif str_two == "Learn":
            print(3)
        else:
            print(None)
compare_strings()
