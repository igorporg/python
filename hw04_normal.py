_author__ = 'Igor A.Provorov'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
#     pass

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     pass
#
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("HOMEWORK 3 normal")

while 1:
    print("Задача-1")
    print("Задача-2")
    print("Задача-3")
    print("Задача-4")
    do = input("Введите номер задачи (0 - Выход): ")

    # Задача-1
    if do == "1":
        print("Задача-1")
        def fibonacci(n, m):
            if m > n > 0:
                i = 2
                f = [1,1]
                while i < m:
                    f.append(f[i-1] + f[i-2])
                    i+=1
                return f[n:]
            else:
                return False

        print(fibonacci(9,15))
        print(fibonacci(20, 15))
        print("********************")

    # Задача-2
    if do == "2":
        print("Задача-2")
        def sort_to_max(origin_list):
            n = len(origin_list)
            list = origin_list.copy()
            i = 0
            while i <= n - 1:
                j = 0
                while j < n - i - 1:
                    if list[j] > list[j + 1]:
                        k = list[j]
                        list[j] = list[j + 1]
                        list[j + 1] = k
                    j += 1
                i += 1
            return list

        print('Отсортированный список: ');
        print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
        print("********************")

    # Задача-3
    if do == "3":
        print("Задача-3")
        def my_filter(func, list):
            pass
        print("********************")

    # Задача-4
    if do == "4":
        print("Задача-4")

        def parallelogram(*args):
            if len(args) > 4:
                return False

            # функция вычисления отрезка между двумя координатами p1, p2
            def get_length(p1, p2):
                import math
                sum = (p1[0] ** 2 - p2[0] ** 2) + (p1[1] ** 2 - p2[1] ** 2)
                if  sum > 0:
                    d = math.sqrt(sum)
                else: d = 0
                return d

            point = []
            for i in args:
                point.append(i)
            lengths = []
            i = 0
            while i < 4:
                for p in point:
                    l = get_length(point[i] , p)
                    if l > 0:
                        lengths.append(l)
                i += 1

            # Проверяем повторения по длине отрезков в списке lengths, если паралелограм то должно быть три повторения
            l = list(set(lengths))
            if len(l) == 4:
                return True
            else:
                return False

        А1 = (3, 7)
        А2 = (5, 3)
        А3 = (9, 9)
        А4 = (11, 5)
        print(parallelogram(А1, А2, А3, А4))
        print("********************")

    if do == "0":
        break
