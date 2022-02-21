num = int(input('Введите номер: '))

if num > 36 or num < 0:
    print('Введены неверные данные')
elif num == 0:
    print('зеленый')
elif num >= 1 and num <= 10 or num >= 19 and num <= 28:
    color = 'черный' if num % 2 == 0 else 'красный'
    print(color)
else:
    color = 'красный' if num % 2 == 0 else 'черный'
    print(color)
    