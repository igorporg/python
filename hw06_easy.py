

_author__ = 'Igor A.Provorov'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


print("HOMEWORK 6 Easy")
while 1:
    print("Задача-1")
    print("Задача-2")
    do = input("Введите номер задачи (0 - Выход): ")

    # Задание-1:
    if do == "1":
#*****************************************************************************************
        print("Задача-1")
        import math
        class triangle:
            def __init__(self, a, b, c):
                self.coords = [a, b, c]
                self.x1 = int(a[0])
                self.x2 = int(b[0])
                self.x3 = int(c[0])
                self.y1 = int(a[1])
                self.y2 = int(b[1])
                self.y3 = int(c[1])
                self.ab = self.line(self.x1, self.y1, self.x2, self.y2)
                self.ac = self.line(self.x1, self.y1, self.x3, self.y3)
                self.bc = self.line(self.x2, self.y2, self.x3, self.y3)

            # определяем равны ди две точки
            def equal(self, a, b):
                if int(a[0]) == int(b[0]) and int(a[1]) == int(b[1]):
                    return True
                else:
                    return False

            # определяем действительно ли это треугольник
            def is_triangle(self):
                # проверяем совпадат ли точки или нет.
                # по хоршему еще нужно добавить проверку не стоят ли точки на одной линии
                if self.equal(self.a, self.b) or self.equal(self.a, self.c) or self.equal(self.b, self.c):
                    return False
                else:
                    return True

            # Длина отрезка
            def line(self, x1, y1, x2, y2):
                d = (x1 - x2)**2 + (y1 - y2)**2
                if d > 0:
                    return math.sqrt(d)
                else:
                    return 0

            # площадь фигуры
            def square(self):
                s = 0.5 * math.fabs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1))
                return s

            # периметр фигуры
            def perimeter(self):
                return self.ab + self.ac + self.bc

            # Высота треугольника с вершиной в точке h [x,y]
            def height(self, h):
                piece = []
                for point in self.coords:
                    # ищем две другие вершины треугольника и добавляем в список piece
                    if not self.equal(point, h):
                        piece.append([point[0], point[1]])

                x1 = int(piece[0][0])
                y1 = int(piece[0][1])
                x2 = int(piece[1][0])
                y2 = int(piece[1][1])
                # Вычисляем высоту по формуле h = 2*S/a где S - площадь, a - длина основания
                a = self.line(x1, y1, x2, y2)
                return 2 * self.square() / a

        while 1:
            a = input("Введите координаты точки А (x,y): ").split(",")
            b = input("Введите координаты точки B (x,y): ").split(",")
            c = input("Введите координаты точки C (x,y): ").split(",")

            t = triangle(a, b, c)
            if not t.is_triangle:
                print("Это не треугольник! Введите другие координаты.")
                continue

            print("Координаты треугольника: ", t.coords)
            print("Площадь треугольника: ", t.square())
            print("Высота треугольника (с вершиной a): ", t.height(a))
            print("Высота треугольника (с вершиной b): ", t.height(b))
            print("Высота треугольника (с вершиной c): ", t.height(c))
            print("Периметр треугольника: ", t.perimeter())

            go = input("Желаете повторить вычисления? (Yes/No)")
            if go == "No":
                break
            else:
                continue
        print("Задача выполнена!")
        print("********************")
#********************************************************************************************
    # Задание-2:
    if do == "2":
        print("Задача-2")
        import math
        class trapeze:
            # теоретически можно сделать наследование класса triangle, поскольку трапецию можно разбить на два треугольника
            def __init__(self, a, b, c, d):
                # Вычилим их значения координат
                points = sorted([a, b, c, d])
                self.a, self.b, self.c, self.d = points[0], points[1], points[2], points[3]
                self.coords = [self.a, self.b, self.c, self.d]
                # Будем считать что точки a, d максимально удалены друго от друга а точки b,c минимально
                # Вычислим отрезки между точками
                self.ab = self.line(self.a[0], self.a[1], self.b[0], self.b[1])
                self.ad = self.line(self.a[0], self.a[1], self.d[0], self.d[1])
                self.bc = self.line(self.b[0], self.b[1], self.c[0], self.c[1])
                self.cd = self.line(self.c[0], self.c[1], self.d[0], self.d[1])
                # Диагонали
                self.ac = self.line(self.a[0], self.a[1], self.c[0], self.c[1])
                self.bd = self.line(self.b[0], self.b[1], self.d[0], self.d[1])

            # определяем равны ди две точки
            def equal(self, a, b):
                if int(a[0]) == int(b[0]) and int(a[1]) == int(b[1]):
                    return True
                else:
                    return False

            # определяем действительно ли это трапеция
            def is_trapeze_equilateral(self):
                if self.ac == self.bd:
                    return True
                else:
                    return False

            # Длина отрезка
            def line(self, x1, y1, x2, y2):
                d = (int(x1) - int(x2))**2 + (int(y1) - int(y2))**2
                if d > 0:
                    return math.sqrt(d)
                else:
                    return 0

            # площадь фигуры
            def square(self):
                # площадь равнобедренной трапеции вычисляется по формуле: S=½h(ad + bc)
                s = 0.5 * self.height() * (self.ad + self.bc)
                return s

            # периметр фигуры
            def perimeter(self):
                return self.ab + self.bc + self.cd + self.ad

            # Высота равнобедренной трапеции
            def height(self):
                ## определяеся формулой: h = 2*S / (ad + bc) - где S площадь трапеции
                ## h  = 2 * self.square() / (self.ad + self.bc)  - не подходит, т.к. ведет к зацкливанию функций height и square

                # Высоту трапеции можно найти если известны значения длин сторон
                h = math.sqrt(self.ab ** 2 - (((self.ad - self.bc) ** 2 + self.ab ** 2 - self.cd ** 2) / (2 * (self.ad - self.bc))) **2 )
                return h

        while 1:
            a = input("Введите координаты точки А (x,y): ").split(",")
            b = input("Введите координаты точки B (x,y): ").split(",")
            c = input("Введите координаты точки C (x,y): ").split(",")
            d = input("Введите координаты точки D (x,y): ").split(",")

            t = trapeze(a, b, c, d)
            if not t.is_trapeze_equilateral:
                print("Это НЕ равнобедренная трапеция!")
                #continue
            else:
                print("Это равнобедренная трапеция.")

            print("Координаты трапеции: ", t.coords)
            print("Площадь трапеции: ", t.square())
            print("Длина стороны AB: ", t.ab)
            print("Длина стороны BC: ", t.bc)
            print("Длина стороны CD: ", t.cd)
            print("Длина стороны AD: ", t.ad)
            print("Периметр трапеции: ", t.perimeter())

            go = input("Желаете повторить вычисления? (Yes/No)")
            if go == "No":
                break
            else:
                continue

        print("Задача выполнена!")
        print("********************")
#**************************************************************************************************

    if do == "0":
        break
