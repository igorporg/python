_author__ = 'Igor A.Provorov'
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print("HOMEWORK 5 normal")

import os
import sys

#print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("gotodir <dir_name> - переход в папку")
    print("listdir - просмотр содержимого текущей папки")
    print("deldir <dir_name> - удаление папки")
    print("mkdir <dir_name> - создание папки")

def goto_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.chdir(dir_path)
        print('Перешли в директорию {}'.format(dir_path))
    except FileExistsError:
        print('директория {} не существует'.format(dir_name))

def list_dir():
    dir_path = os.path.join(os.getcwd())
    files = [f.path for f in os.scandir(dir_path)]
    print("Содержимое текущего каталога {} :".format(dir_path))
    print(files)


def del_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.remove(dir_path)
        print('Выполнено удаление директории {}'.format(dir_path))
    except FileExistsError:
        print('директория {} не может быть удалена'.format(dir_name))


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


do = {
    "help": print_help,
    "gotodir": goto_dir,
    "listdir": list_dir,
    "deldir": del_dir,
    "mkdir": make_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
else:
    print("Задан неверный ключ")
    print("Укажите ключ help для получения справки")
