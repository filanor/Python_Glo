# ЗАДАЧА
# По данным ФИО сформируйте строку, содержащую фамилию с инициалами.

# РЕШЕНИЕ
f = input('Введите фамилию: ')
i = input('Введите имя: ')
o = input('Введите отчество: ')

print(f'{f} {i[0].lower()}.{o[0].upper()}.')