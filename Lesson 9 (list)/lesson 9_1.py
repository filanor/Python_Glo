# ЗАДАЧА
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.


# РЕШЕНИЕ
n = int(input('Введите количество строк: '))
print('Введите строки')
arr = []

for i in range(n):
    arr.append(input())
    
search = input('Введите поисковый запрос: \n')

rez = []

for str in arr:
    if search.lower() in str.lower().split():
        rez.append(str)
        
print('Результаты поиска', *rez, sep='\n')