# ЗАДАЧА
# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
# РЕШЕНИЕ

n = int(input('Введите n: '))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)