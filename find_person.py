'''Задание: Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.'''


def find_person(name):
    list_users = ["Вася", "Маша", "Петя"]
    while list_users[0] is not name:
        list_users.pop(0)
    print "{}, а вот и ты!".format(name)

name = input("Введите имя:")
find_person(name)
