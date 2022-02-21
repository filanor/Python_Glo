number = int(input('Введите номер билета: '))

if number > 999999 or number < 100000:
    answer = 'Ошибка ввода данных'
else:
    answer = 'Билет ' + str(number) + ' '
    first_hulf = number // 1000
    last_hulf = number % 1000

    first_hulf = first_hulf % 10 + first_hulf // 100 + (first_hulf // 10) % 10
    last_hulf = last_hulf % 10 + last_hulf // 100 + (last_hulf // 10) % 10
    answer += 'счастливый' if first_hulf == last_hulf else 'НЕсчастлилвый'

print(answer)