# ЗАДАЧА
# Вводится одно целое четырехзначное число. Выведите максимальную цифру числа.

# РЕШЕНИЕ
#from math import max
num = int(input('Введите число: '))
num_copy = num

max = 0
while(num_copy > 0):
    if max < num_copy % 10:
        max = num_copy % 10
    num_copy = num_copy // 10
print(max)

