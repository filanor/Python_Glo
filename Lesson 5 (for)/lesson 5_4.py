# ЗАДАЧА
# Даны два целых числа a и b. Напишите программу, которая выводит все ЧЕТНЫЕ
# числа на данном промежутке в возрастающем порядке, включая a и b.

# РЕШЕНИЕ

a = int(input('Введите а '))
b = int(input('Введите b '))
for i in range(min(a, b), max(a, b) + 1):
    if i % 2 == 0:
        print(i)