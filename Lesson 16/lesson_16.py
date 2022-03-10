import random

answers = [6, 9, 25, 60, 2]
questions = [
    {
        'question': 'Сколько будет два плюс два умноженное на два',
        'answer': 6
    },
    {
        'question': 'Бревно нужно рапелить на 10 частей, сколько надо сделать распилов?',
        'answer': 9
    },
    {
        'question': 'На двух руках 10 пальцев. Сколько пальцев на 5 руках?',
        'answer': 25
    },
    {
        'question': 'Укол делают каждые полчаса, сколько минут нужно для трех уколов?',
        'answer': 60
    },
    {
        'question': 'Пять свечей горело, две потухли. Сколько свечей осталось?',
        'answer': 2
     }
]

diagnose = {
    0: 'Идиот',
    1: 'Кретин',
    2: 'Дурак',
    3: 'Нормальный',
    4: 'Талант',
    5: 'Гений'
}


def examination():
    count_right_answer = 0
    i = 0
    for question in questions:
        print(f'Вопрос № {i+1}: {question["question"]}')
        user_answer = int(input())

        right_answer = question['answer']
        if user_answer == right_answer:
            count_right_answer += 1
        i += 1

    return count_right_answer

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



print('Добро пожаловать в MyTest.')
print('Как вас зовут')
name = input()
print(f'{name} Ответьте на 5 вопросов и мы поставим вам диагноз')

random.shuffle(questions)

while True:
    count_right_answer = examination()
    print('Количество правильных ответов =', count_right_answer)
    print(f'{name}, Ваш диагноз:', diagnose[count_right_answer])

    if more() == False:
        break