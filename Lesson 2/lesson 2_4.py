# ЗАДАЧА
# Мяч стоит r рублей и k копеек.
# Определите, сколько рублей и копеек нужно заплатить за n мячей.
# Программа получает на вход три целых числа: r, k, n.
# Программа должна вывести два числа: стоимость покупки в рублях и копейках.

# РЕШЕНИЕ
r = int(input('Введите стоимость мяча (рубли) '))
k = int(input('Введите стоимость мяча (копейки) '))
n = int(input('Введите количество мячей '))

print('За', n, 'мяч нужно заплатить', r * n + k * n // 100, 'рублей и ', k * n % 100, 'копеек')