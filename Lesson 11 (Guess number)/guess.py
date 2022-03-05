# =============   Guess the number  ================

import random


# Проверка введенной строки и преобразование к числу
def is_valid(num):
    if not num.isdigit():
        if num == 'exit':
            return -100
        return -1
    elif int(num) < 1 or int(num) > 100:
        return -1
    else:
        return int(num)

# clear screen
def cls():
    print('\n' * 100)

    
def optimal_count(secret_number, min_number=0, max_number=100):
    count = 0
    i = 0
    while i != secret_number:
        count += 1
        i = min_number + (max_number - min_number) // 2
        if i < secret_number:
            min_number = i
        else:
            max_number = i
    return count



    
# Game mode: User guess the number
def start_guess(min_number=0, max_number=100):
    secret_number = random.randint(1, 100)
    optimal = optimal_count(secret_number)
    count = 0

    while True:
        user_number = input(f'enter a number from {min_number} to {max_number}: ')
        user_number = is_valid(user_number)

        if user_number == -1:
            print('ошибка ввода')
            continue
        elif user_number == -100:
            break
        count += 1
        
        if user_number > secret_number:
            print(f'The hidden number is less than {user_number}')
            max_number = user_number
        elif user_number < secret_number:
            print(f'Secret number more than {user_number}')
            min_number = user_number
        else:
            print('*******************************')
            print('=========== YOU WIN ===========')
            print(f'The number of your moves {count}')
            print(f'Optimal number of steps: {optimal}')
            print('*******************************')
            break    



# Game mode: Computer guess the number
def start_computer_guess(min_number=0, max_number=100):
    cls()
    print('')
    print('if your number is less than answer - print "less" or "1"')
    print('if your number is more than answer - print "more" or "2"')
    print('if your number is less than answer - print "right" or "3"')
    print('So, choose your number and click enter')
    input()

    while True:
        computer_number = min_number + (max_number - min_number) // 2
        print(f'If your number {computer_number}?')
        answer = input()
        if answer == '1' or answer == 'less':
            max_number = computer_number
        elif answer == '2' or answer == 'more':
            min_number = computer_number
        elif answer == '3' or answer == 'yes':
            print("Yippee!!!!!!!!  I'm so happy to play with you.")
            break
        else:
            print("I don't understand you((")
            continue



while True:
    cls()
    print('============= Guess the number =============')
    print('Select the game mode:')
    print('1. you guess a number')
    print('2. computer guess a number')
    game_mode = input()  

    if game_mode == '1':
        start_guess()
    elif game_mode == '2':
        start_computer_guess()
    else:
        'Ошибка ввода. Введите 1 или 2'
        continue

    print('Do you want to play again (yes/no): ')
    again = input()
    if again != 'yes':
        print('See you later..')
        break


