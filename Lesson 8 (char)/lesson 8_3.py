# ЗАДАЧА

# Определите, является ли введенный символ заглавной буквой русского алфавита.
# РЕШЕНИЕ

c = input('Введите символ: ')
print(ord(c))
if ord(c) > 1039 and ord(c) < 1072:
    print('YES')
else:
    print('NO')