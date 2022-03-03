# ЗАДАЧА
# На вход программе подается строка текста, содержащая 4 целых числа
# разделенных точкой. Напишите программу, которая определяет является ли
# введенная строка текста ip-адресом.

# РЕШЕНИЕ
ip = input('Введите IP адрес:')
if ip.find('.') > -1:
    ip_arr = ip.split('.')
    flag = 'Yes'

    for i in ip_arr:
        if i.isdigit():
            if int(i) > 256 and int(i) < 0:
                flag = 'No'
            else:
                flag = 'No'
else:
    flag = 'No'
    
print(flag)
        
