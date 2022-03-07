# =============================================
# ===============   PASSWORD   ================
# =============================================
import random

def ask_parameter(quest):
    while True:
        print(quest, 'Введите Да или Нет')
        answer = input()
        if answer.lower() == 'да' or answer.lower() == 'yes':
            return True
        elif answer.lower() == 'нет' or answer.lower() == 'no':
            return False
        else:
            print('Ошибка ввода. Повторите ввод.')
 

def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]
    return password


        
def we_need_digit():
    while True:
        str = input()
        if str.isdigit():
            return int(str)
        print('Ошибка ввода. Повторите ввод')


        
def set_settings():
    enabled_chars = ''
    digits = '0123456789'
    latin_lowercase = 'abcdefghijklmnoprstuvwxyz'
    latin_uppercase = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    russian_lowercase = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
    russian_uppercase = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!@#$%^&*+-=?_'

    digits_enabled = ask_parameter('Включать ли цифры?')
    if digits_enabled:
        enabled_chars += digits

    latin_lowercase_enabled = ask_parameter('Включать ли строчные латинские буквы?')
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase

    latin_uppercase_enabled = ask_parameter('Включать ли заглавные латинские буквы?')
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase

    russian_lowercase_enabled = ask_parameter('Включать ли строчные русские буквы?')
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase

    russian_uppercase_enabled = ask_parameter('Включать ли заглавные русские буквы?')
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase
        
    punctuations_enabled = ask_parameter('Включать ли знаки пунктуации?')
    if punctuations_enabled:
        enabled_chars += punctuation    


    return enabled_chars





def main():
    print('Сколько паролей нужно сгенерировать?')
    qtty = we_need_digit()

    print('укажите длину пароля ')
    length = we_need_digit()

    enabled_chars = set_settings()

    for i in range(qtty):
        password = generate_password(length, enabled_chars)
        print(password)





while True:
    main()

    print('Нужны еще пароли (no/yes)?')
    more = input()
    if more.lower() == 'yes' or more.lower() == 'да':
        continue
    elif more.lower() == 'no' or more.lower() == 'нет':
        break
    else:
        print('ошибка ввода')