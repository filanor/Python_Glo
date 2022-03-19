import pathlib
import random

class FileIO:
    def get(self, path):
        path = pathlib.Path(path)
        if path.is_file():
            f = open(path, 'r')
            data = f.read()
            f.close()
            return data
        return False
    def save(self, path, data):
        f = open(path, 'a+')
        f.write(data+'\n')
        f.close()

    def rewritе(self, path, data):
        f = open(path, 'w')
        f.write(data)
        f.close()
        

class QuestionsStorage:
    def __init__(self):
        f = FileIO()
        data = f.get('questions.txt').strip('\n')
        data = data.split('\n')

        if data:
            self.questions = []
            for line in data:
                line = line.split(':::')
                self.questions.append(Question(line[0], int(line[1])))

    # Возвращает все вопросы
    def get_all(self):
        random.shuffle(self.questions)
        return self.questions
    
    # Добавление нового вопроса
    def add_question(self):
        fileIO = FileIO()
        print('Введите вопрос:')
        text = input()
        print('Введите числовой ответ:')
        while True:
            answer = input()
            if answer.isdigit():
                break
            print('Ошибка ввода. Ответ должен быть цифроваой')
        str = text + ':::' + answer
        f = fileIO.save('questions.txt', str)

    # Выводит все вопросы
    def print_all(self):
        i = 1
        if len(self.questions) < 1:
            return False
        for question in self.questions:
            print(f'{i} - {question.text}')
            i += 1

    def remove_question(self):
        self.print_all()
        questions_qtty = len(self.questions)
        print('\nВведите номер вопроса, который вы хотите удалить')
        while True:
            num = input()
            if num.isdigit() == False or int(num) < 1 or int(num) > questions_qtty:
                print('Ошибка ввода. Повторите ввод.')
                continue
            num = int(num)
            break

        self.questions.pop(num - 1)
        data = ""
        for question in self.questions:
            data += question.text + ':::' + str(question.answer) + '\n'
        
        f = FileIO()
        f.rewritе('questions.txt', data)
        print('Список вопросов был изменен')
        self.print_all()

    # Меню редактирования вопросов
    def edit_questions(self):
        while True:
            #questionsStorage = QuestionsStorage()
            print("Редактор Вопросов")
            print("1 - Для добавления вопроса введите '1''")
            print("2 - Для удаления вопроса введите '2'")
            print("3 - Для выхода")
            while True:
                answer = input()
                if answer.isdigit() == False or not int(answer) in [1, 2, 3]:
                    print('Ошибка ввода. Повторите Ввод')
                    continue
                if answer == '1':
                    self.add_question()
                    break
                if answer == '2':
                    self.remove_question()
                    break
                if answer == '3':
                    return    
        
        
        
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
        print('\n' * 3)
        if more == 'да' or more == 'yes':
            return True
        elif more == 'нет' or more == 'no':
            return False
        else:
            print('Я вас не понял, повторите, пожалуйста...')


# Вывод таблицы результатов
def print_results():
    usersResultStorage = UsersResultStorage()
    results = usersResultStorage.get_all()
    if results and len(results) > 0:
        print('\n' * 3)
        print('=========== НАШИ УЧЕНИКИ ============')
        print(f'{"Имя":20}{"Баллы":10}{"Диагноз":10}')
        for result in results:
            print(f'{result["name"]:20}{result["count"]:10}{result["diagnose"]:10}')
    else:
        print('Нет сохраненных результатов')
    print('\n' * 3)



# Сессия тестирования. Возвращает количество верных ответов
def examination():
    usersResultStorage = UsersResultStorage()
    questionsStorage = QuestionsStorage()
    while True:
        print('Как вас зовут?')
        name = input()
        user = User(name)
        print(f'{name} Ответьте на 5 вопросов и мы поставим вам диагноз')
        questions = questionsStorage.get_all()
        question_number = 1
        
        for question in questions:
            print(f'Вопрос № {question_number}: {question.text}')
            user_answer = get_answer()
            if user_answer == 'exit':
                return False
            
            right_answer = question.answer
            if user_answer == right_answer:
                user.increase_count()

            question_number += 1
    
        result = get_result(user.count, len(questions))
        user.set_result(result)
        
        print('Количество правильных ответов =', user.count)
        print(f'{user.name}, Ваш диагноз:', user.result)
        usersResultStorage.save(user)
        
        if more() == False:
            break        
    










# основное меню программы
print('Добро пожаловать в MyTest.')

while True:
    print('Выбирите действие:')
    print('1 - Пройти тестирование')
    print('2 - Отобразить таблицу результатов')
    print('3 - Редактирование вопросов')
    print('4 - Выход')
    action = input().strip()
    if action.isdigit() == False:
        print('Введите число (номер действия)')
        continue
    if action == '1':
        examination()
    elif action == '2':
        print_results()
    elif action == '3':
        questionsStorage = QuestionsStorage()
        questionsStorage.edit_questions()
    elif action == '4':
        break    
