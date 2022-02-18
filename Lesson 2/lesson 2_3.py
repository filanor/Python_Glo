# ЗАДАЧА
# На вход программе вводится одно целое трехзначное положительное число.
# Выведите сумму и произведение цифр данного числа.


# РЕШЕНИЕ
number = int(input('Введите трехзначное число '))
a = number
if number < 100 or number > 999:
    print('Неверное число')
else:
    number_summ = 0
    number_compos = 1    
    while(a > 0):
        remain = a % 10
        number_summ += remain
        number_compos *= remain
        a = a // 10
    print('Сумма цифр числа', number, 'равна', number_summ)
    print('Произведение цифр числа', number, 'равна', number_compos)

