# ЗАДАЧА
# Напишите программу, которая подсчитывает, сколько пар элементов, равных друг другу.

# РЕШЕНИЕ
str = input()
str_arr = str.split()
count = 0

for i in range(len(str_arr)):
    for j in range(i + 1, len(str_arr)):
        if str_arr[i] == str_arr[j]:
            count += 1
print(count)