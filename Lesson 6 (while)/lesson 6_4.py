# ЗАДАЧА
# Дано натуральное число n, (n ≥ 10). Напишите программу, которая определяет
# его максимальную и минимальную цифры.

# РЕШЕНИЕ
n = int(input('Введите n >= 10: '))
if n < 10:
    print('Ошибка ввода')
else:
    min = n % 10
    max = min

    while n != 0:
        i = n % 10
        if i > max:
            max = i
        elif i < min:
            min = i
        n = n // 10
    print('Максимальная цифра равна', max)
    print('Минимальная цифра равна', min)
