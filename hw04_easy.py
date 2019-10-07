_author__ = 'Igor A.Provorov'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(number, ndigits):
#     pass
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     pass
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
#

print("HOMEWORK 3 Easy")
while 1:
    print("Задача-1")
    print("Задача-2")
    do = input("Введите номер задачи (0 - Выход): ")

    if do == "1":
        print("Задача-1")
        def my_round(number, ndigits):
            if number is float and ndigits is int:
                list = str(number).split(".")
                celoe = int(list[0])
                drobnoe = int(list[1][:ndigits+1])
                ostatok = float("0." + list[1][ndigits + 1:])
                if ostatok > 0.5:
                    drobnoe += 1
                    if len(str(drobnoe))> 6:
                        celoe += 1
                        drobnoe = 0
            else:
                return False
            return float(str(celoe) + "." + str(drobnoe))

        print(my_round(2.1234567, 5))
        print(my_round(2.1999967, 5))
        print(my_round(2.9999967, 5))
        print(my_round(5.9999997, 5))
        print("********************")

    # Задача-2
    if do == "2":
        print("Задача-2")
        def lucky_ticket(ticket_number):
            if len(str(ticket_number)) == 6:
                n1 = str(ticket_number)[:3]
                n2 = str(ticket_number)[3:]
                sum_n1 = int(n1[0]) + int(n1[1]) + int(n1[2])
                sum_n2 = int(n2[0]) + int(n2[1]) + int(n2[2])
                if sum_n1 == sum_n2:
                    return True
                else:
                    return False
            else:
                return False

        print(lucky_ticket(123006))
        print(lucky_ticket(12321))
        print(lucky_ticket(436751))
        print("********************")

    if do == "0":
        break
