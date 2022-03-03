# ЗАДАЧА
# Дан список. Выведите те элементы, которые встречаются в списке только один раз.

# РЕШЕНИЕ

str = input('Введите список: ')
arr = str.split()
rez = []

for el in arr:
    if arr.count(el) == 1:
        rez.append(el)
print(*rez)