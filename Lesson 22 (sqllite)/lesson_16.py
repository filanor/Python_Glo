import random
import sqlite3
import jsonpickle

  

class QuestionsStorage:
    def __init__(self, connection):
        self.connection = connection
        cursor = connection.cursor()
        
        cursor.execute('''SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'questions' ''')
        a = cursor.fetchone()[0]
        if a == 0:
            self.create_new_table()

        self.questions = self.get_all()

    # Возвращает все вопросы
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM questions;")
        all_questions = cursor.fetchall()
        self.questions = []
        for question in all_questions:
            self.questions.append(Question(question[0], question[1]))
        random.shuffle(self.questions)
        return self.questions

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
        self.add(new_question)
        self.questions.append(new_question)

    def add(self, question):
        cursor = self.connection.cursor()
        cursor.execute(f"""INSERT INTO questions (Text, Answer) VALUES('{question.text}', '{question.answer}');""")
        self.connection.commit()

    def create_new_table(self):
        self.questions = []
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE questions(
        Text TEXT PRIMARY KEY,
        Answer INTEGER);""")
        self.connection.commit()
        
        questions = [Question("Бревно нужно рапилить на 10 частей, сколько надо сделать распилов?", 9),
                     Question("Сколько будет два плюс два умноженное на два", 6),
                     Question("На двух руках 10 пальцев. Сколько пальцев на 5 руках?", 25),
                     Question("Укол делают каждые полчаса, сколько минут нужно для трех уколов?", 60),
                     Question("Пять свечей горело, две потухли. Сколько свечей осталось?", 3),
                     ]
        for question in questions:
            self.add(question)
        
    # Выводит все вопросы
    def print_all(self):
        i = 1
        if len(self.questions) < 1:
            print("Вопросов пока нет")
            return False
        print('\n\n')
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

        question_for_delete = self.questions.pop(num - 1)

        cursor = self.connection.cursor()
        cursor.execute(f"""DELETE FROM questions WHERE Text = '{question_for_delete.text}';""")
        self.connection.commit()
        print('\n\nСписок вопросов был изменен\n\n')
        self.print_all()

    # Меню редактирования вопросов
    def edit_questions(self):
        while True:
            #questionsStorage = QuestionsStorage()
            print("\nРедактор Вопросов")
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
    def __init__(self, connection):
        self.connection = connection

        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'users' ''')
        a = cursor.fetchone()[0]
        if a == 0:
            self.create_new_table()        

        self.users = self.get_all()


    def create_new_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE users(
        Name TEXT PRIMARY KEY,
        Count INTEGER,
        Result TEXT);""")
        self.connection.commit()
        
        
    def save(self, user):
        cursor = connection.cursor()
        self.users.append(user)
        cursor.execute(f"""INSERT INTO users (Name, Count, Result) VALUES('{user.name}', '{user.count}', '{user.result}');""")
        self.connection.commit()        


    def get_all(self):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM users""")
        all_users = cursor.fetchall()
        if all_users:
            users = []
            for user in all_users:
                users.append(User(user[0], user[1], user[2]))
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
connection = sqlite3.connect('MyTester.db')
questionsStorage = QuestionsStorage(connection)
usersResultStorage = UsersResultStorage(connection)
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
