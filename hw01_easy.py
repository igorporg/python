_author__ = 'Igor A.Provorov'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
<<<<<<< HEAD


=======


>>>>>>> Lesson_1
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print("HOMEWORK 1 Easy")
while 1==1:
    print("Задача-1")
    print("Задача-2")
    print("Задача-3")
    do = input("Введите номер задачи (0 - Выход): ")

    # Задача-1
    if do == "1":
        print("Задача-1")
        import random

        n = random.randint(10, 999999)
        print(n)
        s = str(n)
        print("Цикл FOR")
        for i in s:
            print(i)

        print("Цикл WHILE")
        i = 0
        while i < len(s):
            print(s[i])
            i += 1
        print("********************")

    # Задача-2
    if do == "2":
        print("Задача-2")
        a = input("Введите переменную а: ")
        b = input("Введите переменную b: ")
        c = a
        a = b
        b = c
        print("Значения переменных изменены:  a = ", a, ", b = ", b)
        print("********************")

    # Задача-3
    if do == "3":
        print("Задача-3")
        age = input("Введите ваш возраст: ")
        if int(age) < 18 :
            print(" ***** Извините, пользование данным ресурсом только с 18 лет *****")
        else:
            print(" ***** Доступ разрешен! ***** ")
        print("********************")
<<<<<<< HEAD

=======
        
>>>>>>> Lesson_1
    if do == "0":
        break
