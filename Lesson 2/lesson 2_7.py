# ЗАДАЧА
# Дано натуральное число, не превосходящее 1 000 000 000. Найдите сумму
# последних трех цифр. Последние цифры – это те, которые справа в числе.
# РЕШЕНИЕ

num = int(input('Введите число: '))
last_3_num = num % 1000


sum = last_3_num // 100 + last_3_num % 10 + (last_3_num // 10) % 10
print(sum)