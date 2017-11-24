''' Задание: Попросить пользователя ввести возраст.
    По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
    Вывести занятие на экран.'''


''' This is first variant:
def definition_of_age():
    age_str = input("Введите возраст:")
    age = int(age_str)
    if 0< age < 140:  
        if 0 < age < 7:
            print("Вы ходите в детский сад")
        elif 7 <= age < 18:
            print("Вы учитесь в школе")
        elif 18 <= age < 23:
            print("Вы учитесь в ВУЗе")
        elif 22 < age :
            print("Вы уже всему научились")
    else:
        print ("Вы точно человек? Может попробуем ещё раз? ")
        definition_of_age()
definition_of_age()'''


def definition_of_age():
    age = input("Введите возраст:")
    age_array = [x for x in range(0, 141)]
    if int(age) in age_array:
        if int(age) in age_array[0:8]:
            print("Вы ходите в детский сад")
        elif int(age) in age_array[8:18]:
            print("Вы учитесь в школе")
        elif int(age) in age_array[18:24]:
            print("Вы учитесь в ВУЗе")
        elif int(age) in age_array[24:]:
            print("Вы уже всему научились")
    else:
        print("Вы точно человек? Может попробуем ещё раз? ")
        definition_of_age()
definition_of_age()
