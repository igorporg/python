_author__ = 'Igor A.Provorov'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


print("HOMEWORK 6 normal")

# class school:
#     def __init__(self, number):
#         self.number_scool = number
#
#     def classes(self):
#         print("Вывод списка классов в школе № {}".format(self.number_scool))
#
#
# class klass(school):
#     def __init__(self, number):
#         self.number_klass = number
#
#     def list_pupils(self):
#         print("Список учеников класса {} в школе № {}".format(self.number_klass, self.number_scool))


class People:
    def __init__(self, firstname, secondname, surname, school, klass):
        self.fname = firstname
        self.sname = secondname
        self.surname = surname
        self.school = school
        self.klass = klass

    def get_full_name(self):
        return self.surname.title() + " " + self.fname.title() + ' ' + self.sname.title()

    def get_short_name(self):
        return self.surname.title() + " " + self.fname[:1].upper() + '. ' + self.sname[:1].upper() + "."

    # def set_full_name(self, firstname, secondname, surname):
    #     self.fname = firstname
    #     self.sname = secondname
    #     self.surname = surname

# Ученики
class Pupil(People):
    def __init__(self, firstname, secondname, surname, school, klass, mother, father):
        super().__init__(self, firstname, secondname, surname, school, klass)
        self.mother = mother
        self.farther = father

    def show_fio(self):
        print(self.get_full_name())

    def show_parents(self):
        print("Родители ученика {}: мать - {}, отец - {}".format(self.get_full_name(), self.mother, self.farther))

# Учителя
class Teacher(People):
    def __init__(self, firstname, secondname, surname, school, klass, subject):
        super().__init__(self, firstname, secondname, surname, school)
        self.klass = klass.split(",")
        self.subject = subject

    def get_teacher_in_klass(self, klass_number):
        if klass_number in self.klass:
             print(self.get_full_name());



pupils = [Pupil("Иван", "Иванович", "Иванов", '11', "4А", "Иванова А.А.", "Иванов Б.Б"),
            Pupil("Петр", "Петрович" "Сидоров", '11', "5Б", "Сидорова А.А.", "Сидоров Б.Б."),
            Pupil("Федор", "Федорович", "Петров", "11", "4В", "Петрова В.В.", "Петров С.С."),
            ]

teachers = [Teacher("Александр", "Иванович", "Иванов", '11', "4А,5Б,8В", "Математика"),
            Teacher("Афанасий", "Петрович" "Сидоров", '11', "5Б,4В,7А", "Физика"),
            Teacher("Антон", "Федорович", "Петров", "11", "8В,7А,9Б", "Химия"),
            ]