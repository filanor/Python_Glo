# Поговорите с пользователем:
# 1. Спросите его “Как вас зовут?”
# 2. Получите от него ответ в виде его имени
# 3. Спросите его “Как ваша фамилия?”
# 4. Получите от него ответ в виде его фамилии
# 5. Спросите его “Как ваше отчество?”
# 6. Получите от него ответ в виде его отчества
# 7. Выведите следующее: “{фамилия} - {имя} - {отчество}”

# Решение
# fio = input('Как вас зовут?\n')
# fio += ' ' + input('Как ваша фамилия?\n')
# fio += ' ' + input('Как ваше отчество?\n')
# print(fio)


first_name = input('Как вас зовут?\n')
last_name = input('Как ваша фамилия?\n')
patronymic = input('Как ваше отчество?\n')
print(last_name, first_name, patronymic, sep=' - ')
