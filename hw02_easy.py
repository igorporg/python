_author__ = 'Igor A.Provorov'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("HOMEWORK 2 Easy")
while 1:
    print("Задача-1")
    print("Задача-2")
    print("Задача-3")
    do = input("Введите номер задачи (0 - Выход): ")

    # Задача-1
    if do == "1":
        print("Задача-1")
        fruits = ["яблоко", "банан", "киви", "арбуз"]
        i = 0
        while i < len(fruits):
            print (i+1,'.{:>10}'.format(fruits[i]))
            i+=1
        print("********************")

    # Задача-2
    if do == "2":
        print("Задача-2")
        fruits = ["яблоко", "банан", "киви", "томат", "картофель", "абрикос", "персик"]
        vegetables = [ "томат", "картофель", "свекла", "капуста", "морковь", "лук"]
        for veg in vegetables:
            for fru in fruits:
                if fru == veg:
                    fruits.remove(veg)
        print (fruits)
        print("********************")

    # Задача-3
    if do == "3":
        print("Задача-3")
        spisok = [2,3,4,8,20,17]
        i = 0
        for num in spisok:
            if num % 2 == 0:
                spisok[i] /= 4
            else:
                spisok[i] *= 2
            i += 1
        print(spisok)
        print("********************")

    if do == "0":
        break
