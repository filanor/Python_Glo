# ЗАДАЧА
# Напишите функцию, которая принимает в качестве аргумента строковое
# представление корректной даты и возвращает значение True, если дата
# является звездной и False в противном случае.

# РЕШЕНИЕ
def is_star_date(date=[]):
    if len(date) != 3:
        return False

    for i in date:
        if i.isdigit() == False:
            return False

    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    return day * month == year % 100

    
date = input('Введите дату в формате дд.мм.гггг: ')
date_arr = date.split('.')

print(is_star_date(date_arr))