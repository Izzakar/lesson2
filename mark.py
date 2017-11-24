'''Задание: Создать список с оценками учеников разных классов 
   школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
   Посчитать и вывести средний балл по всей школе.
   Посчитать и вывести средний балл по каждому классу.'''


mark = [{'school_class': '2а', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '3б', 'scores': [2, 5, 3, 5, 1]},
        {'school_class': '1в', 'scores': [3, 4, 2]}]


def average_of_mark(mark):
    sum_school = 0
    quantity_mark = 0
    for i in mark:
        sum_class = 0
        for j in i['scores']:
            sum_class += j
        sum_school += sum_class
        quantity_mark += len(i['scores'])
        print("Cумма оценок по классу {} равна: {}".format(
            i['school_class'], int(round(float(sum_class) / len(i['scores'])))))
    print("Cумма оценок по школе: {}".format(
        int(round(float(sum_school) / quantity_mark))))

average_of_mark(mark)