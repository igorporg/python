# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

a = float('inf') # infinity
if a == a**2 and a == a*2 and a > 999999:
    print("Значение переменной найдено a = ", a)
else:
    print("Данное значение не соответствует условию задачи")