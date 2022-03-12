# Быки и Коровы
import random


# генерация секретного слова
def generate_secret_num(secret_num_len):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_num = ''
    for i in range(secret_num_len):
        random_index = random.randint(0, len(digits) - 1)
        secret_num += str(digits[random_index])
        digits.pop(random_index)
    return secret_num


# Проверка введенного пользовательлского числа
def check_user_num(user_num, secret_num_len):
    if user_num.isdigit() == False or len(user_num) < secret_num_len or len(user_num) > secret_num_len:
        print(f'Введите последовательность из {secret_num_len} цифр')
        return False
    else:
        for i in range(len(user_num) - 1):
            for j in range(i + 1, len(user_num)):
                if user_num[i] == user_num[j]:
                    print('Не может быть повторяющихся символов. Повторите ввод')
                    return False
    return True
                
# Ввод пользовательского числа
def get_user_num(secret_num_len):
    while True:
        user_num = input()
        if check_user_num(user_num, secret_num_len) == True:
            return user_num

def calculate_bulls(user_num, secret_num):
    count = 0
    for i in range(len(secret_num)):
        if user_num[i] == secret_num[i]:
            count += 1
    return count

def calculate_cows(user_num, secret_num):
    count = 0
    for i in range(len(secret_num)):
        if user_num[i] != secret_num[i] and user_num[i] in secret_num:
            count += 1
    return count



def play():
    secret_num_len = 4
    secret_num = generate_secret_num(secret_num_len)

    print(secret_num)
    while True:
        print('Найди число, задуманное компьютером')
        user_num = get_user_num(secret_num_len)

        bulls_count = calculate_bulls(user_num, secret_num)
        cows_count = calculate_cows(user_num, secret_num)
        
        print(f'Количество быков: {bulls_count}. Количество коров: {cows_count}')

        if bulls_count == 4:
            print('Ура!! Вы Победили!!!')
            break


def more():
    print('\n\n Хотите попробовать еще раз?')
    more = ''
    while True:
        more = input()
        more = more.lower()
        print(more)
        if more == 'да' or more == 'yes':
            return True
        elif more == 'нет' or more == 'no':
            print('Спасибо за участие')
            return False
        else:
            print('Я вас не понял, повторите, пожалуйста...')
            
            
            
            
# ============= main ==================
print('Быки и коровы')
while True:
    play()

    if more() == False:
        break