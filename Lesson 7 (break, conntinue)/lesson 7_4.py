# ЗАДАЧА
# Дано натуральное число n. Напишите программу, которая выводит числа от 1 до n
# включительно за исключением:
# чисел от 2 до 8 включительно
# чисел от 128 до 256 включительно;
# чисел от 1024 до 2048 включительно.

# РЕШЕНИЕ
a = int(input('Введите а: '))
for i in range(1, a + 1):
    if (i >= 2 and i <= 8) or (i >= 2 and i <= 8) or (i >= 2 and i <= 8):
        continue
    print(i)