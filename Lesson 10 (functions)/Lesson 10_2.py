# ЗАДАЧА
# Напишите функцию для нахождения максимального элемента списка.

# РЕШЕНИЕ
def max_el(arr):
    maximum = 0
    for el in arr:
        el = int(el)
        if el > maximum:
            maximum = el
    return maximum

arr_1 = input().split()
arr_2 = input().split()

max_arr_1 = max_el(arr_1)
max_arr_2 = max_el(arr_2)

print(max_arr_1 * max_arr_2)
