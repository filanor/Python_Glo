import random

def get_the_word():
    file = open('russian_nouns.txt')
    words_arr = file.read().split('\n')

    while True:
        random_index = random.randint(0, len(words_arr) - 1)
        word = words_arr[random_index]
        word = word.split(' - ')
        print(word[1])
        return word[0]

def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word




def play():
    count = 0
    enable_char = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
    used_char = []
    
    print('Перед вами загаданное слово. Вы можете угадывать его по буквам, либо назвать целиком.')
    secret_word = get_the_word()
    user_word = '*' * len(secret_word)
    print(user_word)

    while user_word != secret_word:
        print('Введите букву: ')
        char = input()
        if char.lower() == secret_word:
            count += 1
            break
        if len(char) > 1 or not char.lower() in enable_char:
            print('Ошибка ввода')
            continue

        char = char.lower()
        if char in used_char:
            print('Вы уже называли эту букву')
            continue

        user_word = update_user_word(secret_word, user_word, char)
        used_char.append(char)
        count += 1
        print(user_word)

    print('\n\n\nПоздравляю, вы выиграли!!!!!!!\n\n\n')
    print(f'Загаданное слово: {secret_word}. Вам понадобилост {count} ходов\n\n\n')
        




while True:
    play()

    print('Хотите сыграть еще раз (да/нет)?')
    answer = input()
    if answer.lower() != 'yes' or answer.lower() != 'да':
        print('Спасибо за игру!!!!')
        break