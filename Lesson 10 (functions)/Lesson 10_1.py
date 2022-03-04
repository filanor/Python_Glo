# ЗАДАЧА
# Дано два натуральных числа. Найдите количество разрядов каждого из них и выведите их произведение.

# РЕШЕНИЕ
def digit_caunnting(a):
    count = 0
    while a != 0:
        count += 1
        a = a // 10
    return count


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

rez = digit_caunnting(a) * digit_caunnting(b)

print(rez)