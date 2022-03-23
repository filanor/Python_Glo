import pathlib
import random
import jsonpickle

class FileIO:
    def get(self, path):
        path = pathlib.Path(path)
        if path.is_file():
            f = open(path, 'r')
            data = f.read()
            if data:
                json_data = jsonpickle.decode(data)
            else:
                return False
            f.close()
            return json_data
        return False

    def save(self, path, data):
        f = open(path, 'w')
        f.writelines(jsonpickle.encode(data))
        f.close()
        

class QuestionsStorage:
    def __init__(self):
        self.file_name = 'questions.json'
        self.questions = self.get_all()

    # Возвращает все вопросы
    def get_all(self):
        data = fileIO.get(self.file_name)
        if data:
            self.questions = []
            for question in data:
                self.questions.append(question)
            random.shuffle(self.questions)
            return self.questions
        return []
    
    # Добавление нового вопроса
    def add_question(self):
        print('Введите вопрос:')
        text = input()
        print('Введите числовой ответ:')
        while True:
            answer = input()
            if answer.isdigit():
                break
            print('Ошибка ввода. Ответ должен быть цифроваой')

        new_question = Question(text, answer)
        self.questions.append(new_question)
        
        fileIO.save(self.file_name, self.questions)

    # Выводит все вопросы
    def print_all(self):
        i = 1
        if len(self.questions) < 1:
            print("Вопросов пока нет")
            return False
        for question in self.questions:
            print(f'{i} - {question.question}')
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
        print(self.questions)
        fileIO.save(self.file_name, self.questions)
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
        self.question = text
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
    def __init__(self):
        self.file_name = 'results.json'
        self.users = self.get_all()
        print(self.users)
        
    def save(self, user):
        self.users.append(user)
        #json_data = jsonpickle.encode(self.users)
        fileIO.save(self.file_name, self.users)
        

    def get_all(self):
        data = fileIO.get(self.file_name)
        if data:
            users = []
            for user in data:
                users.append(user)
            return users
        return []

    # Вывод таблицы результатов
    def print_results(self):
        if self.users and len(self.users) > 0:
            print('\n' * 3)
            print('=========== НАШИ УЧЕНИКИ ============')
            print(f'{"Имя":20}{"Баллы":10}{"Диагноз":10}')
            for user in self.users:
                print(f'{user.name:20}{str(user.count):10}{user.result:10}')
        else:
            print('Нет сохраненных результатов')
        print('\n' * 3)




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



# Сессия тестирования. Возвращает количество верных ответов
def examination():
    while True:
        print('Как вас зовут?')
        name = input()
        user = User(name)
        print(f'{name} Ответьте на 5 вопросов и мы поставим вам диагноз')
        questions = questionsStorage.get_all()
        question_number = 1
        
        for question in questions:
            print(f'Вопрос № {question_number}: {question.question}')
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
    







jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False,)


# основное меню программы
print('Добро пожаловать в MyTest.')
fileIO = FileIO()
questionsStorage = QuestionsStorage()
usersResultStorage = UsersResultStorage()
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
        usersResultStorage.print_results()
    elif action == '3':
        questionsStorage.edit_questions()
    elif action == '4':
        break    
