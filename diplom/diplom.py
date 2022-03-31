import sqlite3

# Для воода циифр
def input_number():
    while True:
        num = input()
        if num.isdigit() == True:
            return int(num)
        print("Ошибка ввода данных. Нужно ввести числовое значение:")
        
def input_age():
    while True:
        age = input_number()
        if age < 6 or age > 18:
            print("Неверно указан возраст. Посторите ввод (от 6 до 18).")
            continue
        return age

def input_name():
    while True:
        name = input()
        if len(name.split()) < 3:
            print("Введите Фамилию Имя и Отчество")
            continue
        return name

def print_school_info(school, students):
    print(f'''
    Школа № {school.number} находится по адресу {school.adress}. Количество учеников: {students.count}
    ''')    


# Класс отвечающий за обработки и хранение инвормации о школе
class School:
    def __init__(self, conn):
        self.count = 0
        self.conn = conn
        curr = self.conn.cursor()
        curr.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='school';""")
        data = curr.fetchone()[0]
        if data == 0:
            self.create_school()
        data = self.get_school_info()
        (self.id, self.number, self.adress) = data

    # Ввод начальных данных о школе и создание таблицы
    def create_school(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS school(
        id INT PRIMARY KEY,
        number INT,
        adress TEXT);
        """)
        self.conn.commit()
        print("Приветствую вас в системе учета школы.")
        print("Для начала работы нужно заполнить данные о школе")
        print("Введите номер школы:")
        number = input_number()
        print("Введите адрес школы: ")
        adress = input()
        cur.execute(f"""INSERT INTO school(id, number, adress) 
           VALUES('1', '{number}', '{adress}');""")
        self.conn.commit()

    # Получение инвойрмации о школе из БД
    def get_school_info(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT * FROM school""")
        info = cur.fetchone()
        return info
    

    # Ребактирование данных о школе
    def change_data(self):
        cur = self.conn.cursor()
        while True:
            print(""" 
            
            Какие данные нужно поменять:
            1 - номер школы
            2 - адрес школы
            3 - выйти из режима изменения данных о школе
            
            """)
            action = input_number()
            if action == 1:
                new_number = input_number()
                cur.execute(f"""Update school set number = {new_number} where id = {self.id}""")
                self.conn.commit()
                self.number = new_number
            elif action == 2:
                new_adress = input()
                cur.execute(f"""Update school set adress = {new_adress} where id = {self.id}""")
                self.conn.commit()
                self.adress = new_adress
            elif action == 3:
                break
            else:
                print("Ошибка ввода.")
    

# Класс отвечающий за хранение и обработку учащихся
class StudentStorage:
    def __init__(self, conn):
        self.conn = conn
        curr = self.conn.cursor()
        curr.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students';""")
        data = curr.fetchone()[0]
        if data == 0:
            self.create_students_db()
        self.students = self.get_all()
        self.count = len(self.students)

    # Создание таблицы школьников в БД
    def create_students_db(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        class TEXT);
        """)
        self.conn.commit()

    # Загрузка всех школьников из БД
    def get_all(self):
        curr = self.conn.cursor()
        curr.execute("""SELECT * FROM students;""")
        data = curr.fetchall()
        students = []
        for student in data:
            print(student)
            (stud_id, name, age, cl) = student
            students.append({
                "id": stud_id, "name": name, "age": age, "class": cl
            })
        return students

    # Печать таблицы школьников
    def print_all(self):
        print(f'\n{"№":4} {"ФИО":30} {"Возраст":10} {"Класс":7}')
        i = 1
        for student in self.students:
            print(f'{i:4} {student["name"]:33} {student["age"]:9} {student["class"]:5}')
            i += 1
        
    # Добавление нового школьника
    def add(self):
        print("Введите Имя ФИО учащегося")
        name = input_name()
        print("Введите возраст учащегося")
        age = input_age()
        print("Введите класс учащегося")
        cl = input()
        cur = self.conn.cursor()
        cur.execute(f"""INSERT INTO students(id, name, age, class) 
           VALUES(null, '{name}', '{age}', '{cl}');""")
        self.conn.commit()
        self.students = self.get_all()


    # Удаление ученика из БД
    def remove(self):
        self.print_all()
        print("Ввдеите номер учащегося, которого нужно удалить:")
        while True:
            num = input_number()
            if num < 1 or num > len(self.students):
                print("Ошибка ввода. Повторите ввод")
                continue
            break
        student_id = self.students[num - 1]["id"]
        cur = self.conn.cursor()
        cur.execute(f"""DELETE FROM students WHERE id = '{student_id}';""")
        self.conn.commit()
        self.students.pop(num - 1)
  
  
     
# Основное меню программы
def main():
    conn = sqlite3.connect('school.db')
    school = School(conn)
    students = StudentStorage(conn)
    while True:
        print("""
        Выбирите действие:
        1 - Посмотреть информацию о школе.
        2 - Изменить данные школы.
        3 - Посмотреть список учеников.
        4 - Добавить нового Ученика.
        5 - Удалить ученика.
        6 - Выход из программы.
        """)
        action = input_number()
        if action == 1:
           print_school_info(school, students)
        elif action == 2:
            school.change_data()
        elif action == 3:
            students.print_all()
        elif action == 4:
            students.add()
        elif action == 5:
            students.remove()
        elif action == 6:
            conn.close()
            break


main()