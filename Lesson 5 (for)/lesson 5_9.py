# ЗАДАЧА
# Выведите YES, если среди введенных чисел было хотя бы одно нечетное число.
# В противном случае выведите NO.
# РЕШЕНИЕ
flag = 'NO'
n = int(input('Введите количество чисел для ввода: '))

for i in range(n):
    number = int(input('введите число: '))
    if number % 2 != 0:
        flag = 'YES'

print(flag)
