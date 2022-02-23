# ЗАДАЧА
# выведите YES, если все введенные числа нечетные. В противном случае выведите NO.
# РЕШЕНИЕ
flag = 'YES'
n = int(input('Введите количество чисел для ввода: '))

for i in range(n):
    number = int(input('введите число: '))
    if number % 2 == 0:
        flag = 'NO'

print(flag)
