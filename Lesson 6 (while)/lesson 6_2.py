# ЗАДАЧА
# Вводится натуральное число a. Найдите количество цифр 5 среди всех цифр числа a.

# РЕШЕНИЕ

a = int(input('Введите a: '))
count = 0

while a != 0:
    if a % 10 == 5:
        count += 1
    a = a // 10
print(count)
    