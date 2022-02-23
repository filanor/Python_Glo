# ЗАДАЧА
# Напишите программу, которая выводит наибольшее и наименьшее число
# из введенной последовательности.

# РЕШЕНИЕ
n = int(input('Введите количество чисел в последовательности: '))


for i in range(n):
    current_number = int(input())
    if i == 0:
        max_number = current_number
        min_number = current_number
    else:
        if current_number >= max_number:
            max_number = current_number
        else:
            min_number = current_number

print('Минимум равен', min_number)
print('Максимум равен', max_number)

    