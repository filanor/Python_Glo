import pathlib
import random


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
     },
    {
        'question': 'Тестовый вопрос введите 1',
        'answer': 1
    }
]




# Получение ответа и его проверка
# False для прекращения сессии вопросов
def get_answer():
    while True:
        answer = input()
        if answer.lower() == 'exit' or answer.lower() == 'выход':
            return 'exit'
        if answer.isdigit() == True:
            print(f' get_answer {answer}')
            return int(answer)
        print('Ответ должен быть числом. Введите число или выход/exit что бы прервать сессию')


# Сессия тестирования. Возвращает количество верных ответов
def examination():
    count_right_answer = 0
    i = 0
    for question in questions:
        print(f'Вопрос № {i+1}: {question["question"]}')
        user_answer = get_answer()
        if user_answer == 'exit':
            return 'exit'
        
        right_answer = question['answer']
        if user_answer == right_answer:
            count_right_answer += 1
        i += 1

    return count_right_answer



# Определение диагноза
def get_result(count):
    diagnose = {
        0: 'Идиот',
        1: 'Кретин',
        2: 'Дурак',
        3: 'Нормальный',
        4: 'Талант',
        5: 'Гений'
    }
    question_qtty = len(questions)
    return diagnose[(count * 100 // question_qtty) // 20]
    


# Запрос, стоит ли протестировать посторно
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


# Сохранение в файл
def save_result(str):
    f = open('results.txt', 'a+')
    f.write(str + '\n')
    f.close()


# Вывод таблицы результатов 
def print_result():
    path = pathlib.Path('results.txt')
    if path.is_file():
        print('========= НАШИ УЧЕНИКИ ==========')
        print('Имя              ', 'Баллы ', 'Диагноз   ')
        f = open('results.txt', 'r')
        for line in f:
            line = line.strip('\n')
            data = line.split('###')
            print(f'{data[0]:20}{data[1]:5}{data[2]:10}')
        f.close()    


# основная программа
print('Добро пожаловать в MyTest.')
get_result(5)
print_result()
print('Как вас зовут')
name = input()
print(f'{name} Ответьте на 5 вопросов и мы поставим вам диагноз')

random.shuffle(questions)

while True:
    count_right_answer = examination()
    if count_right_answer == 'exit':
        break
    result = get_result(count_right_answer)
    print('Количество правильных ответов =', count_right_answer)
    print(f'{name}, Ваш диагноз:', result)

    if more() == False:
        str = f'{name}###{count_right_answer}###{result}'
        save_result(str)
        break