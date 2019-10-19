_author__ = 'Igor A.Provorov'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random

# Количество бочонков в мешке
KEGS = 90

# получаем список чисел для игрока в лото
def get_numbers(n = 15, max = 90):
    i = 1
    cartlist = []
    while i <= n:
        number = random.randint(1, max)
        if number not in cartlist:
            cartlist.append(number)
        else:
            continue
        i+=1
    return cartlist

# получаем списки чисел построчно разбавленных пробелами
def get_cards(cartlist):
    i = 0
    list = []
    while i < 3:
        list.append(cartlist[i*5:i*5 + 5])
        list[i] = list[i] + ["  "] * 4
        random.shuffle(list[i])
        i+=1
    return list

# получаем итоговую карточку игрока в виде строки
def show_cards(list):
    card = ""
    for el1 in list.copy():
        l = ""
        for el2 in el1:
            # переводим числа в строки, если число состоит из 1-й цифры то добавляем ей пробел
            s = str(el2)
            if len(s) == 1:
                s = " " + s
            l = l + " " + s
        card = card + l + "\n"
    return card

def edit_cards(list_of_numbers, number):
    if number in list_of_numbers:
        pass

def find_cards(list_of_numbers, number):
    if number in list_of_numbers:
        return True
    else:
        return False

def kegs_gen(kegs):
    return {x: x for x in range(1,kegs+1)}

def get_keg(bag_of_kegs):
    n = random.randint(1, len(bag_of_kegs))
    return bag_of_kegs.pop(n)



print("В мешке {} бочонков".format(KEGS))
a = input("Начнем игру? y/n : ")
if a == "y":
    # Получаем списки случайных чисел для каждого игрока
    numbers_for_user = get_numbers()
    numbers_for_comp = get_numbers()

    while 1:

        # Выводим карточки игроков
        card_for_user = show_cards(get_cards(numbers_for_user))
        print('')
        print('------ Ваша карточка -----\n')
        print(card_for_user)
        print('--------------------------')

        card_for_comp = show_cards(get_cards(numbers_for_comp))
        print('')
        print('-- Карточка компьютера ---\n')
        print(card_for_comp)
        print('--------------------------')

        bag_of_kegs = kegs_gen(KEGS)
        KEGS -= 1
        if KEGS < 0:
            break
        keg = get_keg(bag_of_kegs)
        print("Выпал бачонок с номером: {} ".format(keg))
        y = input("Зачеркнуть совпашие числа в карточке? y/n :")

        # Проверяем действия игрокан
        if y == "y":
            if find_cards(numbers_for_user, keg):
                edit_cards(numbers_for_user, keg)
            else:
                print("Вы проиграли!")
                break
        else:
            if find_cards(numbers_for_user, keg):
                print("Вы проиграли!")
                break
            else:
                continue

        edit_cards(numbers_for_comp, keg)

else:
    print("До встречи!")