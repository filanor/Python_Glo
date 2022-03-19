import pathlib
import random

class FileIO:
    def get(self, path):
        path = pathlib.Path(path)
        if path.is_file():
            f = open('results.txt', 'r')
            data = f.read()
            f.close()
            return data
        return False
    def save(self, path, data):
        f = open('results.txt', 'a+')
        f.write(data+'\n')
        f.close()        

class QuestionsStorage:
    def __init__(self):
        self.questions = [
            Question('Сколько будет два плюс два умноженное на два', 6),
            Question('Бревно нужно рапелить на 10 частей, сколько надо сделать распилов?', 9),
            Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
            Question('Укол делают каждые полчаса, сколько минут нужно для трех уколов?', 60),
            Question('Пять свечей горело, две потухли. Сколько свечей осталось?', 2),
            Question('Тестовый вопрос введите 1', 1)
        ]
    def get_all(self):
        random.shuffle(self.questions)
        return self.questions


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class User:
    def __init__(self, name, count=0, result='не задан'):
        self.name = name
        self.count = count
        self.result = result
    
    def increase_count(self):
        self.count += 1

    def set_result(self, result):
        self.result = result



class UsersResultStorage:
    def save(self, user):
        str = f'{user.name}###{user.count}###{user.result}'
        f = FileIO()
        f.save('results.txt', str)
        

    def get_all(self):
        f = FileIO()
        data = f.get('results.txt').strip('\n')
        data = data.split('\n')
        if data:
            results = []
            for line in data:
                data_arr = line.split('###')
                result = {'name': data_arr[0], 'count': data_arr[1], 'diagnose': data_arr[2]}
                results.append(result)
            return results
        return False


# Получение ответа и его проверка
# False для прекращения сессии вопросов
def get_answer():
    while True:
        answer = input()
        if answer.lower() == 'exit' or answer.lower() == 'выход':
            return 'exit'
        if answer.isdigit() == True:
            return int(answer)
        print('Ответ должен быть числом. Введите число или выход/exit что бы прервать сессию')


# Сессия тестирования. Возвращает количество верных ответов
def examination(questions):
    print('Как вас зовут?')
    name = input()
    user = User(name)
    print(f'{name} Ответьте на 5 вопросов и мы поставим вам диагноз')    
    question_number = 1
    
    for question in questions:
        print(f'Вопрос № {question_number}: {question.text}')
        user_answer = get_answer()
        if user_answer == 'exit':
            return 'exit'
        
        right_answer = question.answer
        if user_answer == right_answer:
            user.increase_count()
        question_number += 1

    result = get_result(user.count, len(questions))
    user.set_result(result)
    
    print('Количество правильных ответов =', user.count)
    print(f'{user.name}, Ваш диагноз:', user.result)
    
    return user



# Определение диагноза
def get_result(count, question_qtty):
    diagnose = {
        0: 'Идиот',
        1: 'Кретин',
        2: 'Дурак',
        3: 'Нормальный',
        4: 'Талант',
        5: 'Гений'
    }
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


# Вывод таблицы результатов
def print_results(results):
    print('=========== НАШИ УЧЕНИКИ ============')
    print(f'{"Имя":20}{"Баллы":10}{"Диагноз":10}')
    for result in results:
        print(f'{result["name"]:20}{result["count"]:10}{result["diagnose"]:10}')




# основная программа
print('Добро пожаловать в MyTest.')
questionsStorage = QuestionsStorage()
usersResultStorage = UsersResultStorage()

results = usersResultStorage.get_all()
if results:
    print_results(results)

while True:
    questions = questionsStorage.get_all()
    user = examination(questions)
    if user == 'exit':
        break

    usersResultStorage.save(user)

    if more() == False:
        break