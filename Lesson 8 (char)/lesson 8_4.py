# ЗАДАЧА
# Вводится один символ. Измените регистр символа, если он был латинской буквой:
# сделайте его заглавным, если он был строчной буквой и наоборот. Символы, не
# являющиеся латинской буквой нужно оставить без изменения.
# 
# РЕШЕНИЕ

c = input('Введите символ: ')
if ord(c) > 40 and ord(c) < 67:
    print(c.lower())
elif ord(c) > 96 and ord(c) < 123:
    print(c.upper())
else:
    print(c)