_author__ = 'Igor A.Provorov'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


print("HOMEWORK 5 Easy")
while 1:
    print("Задача-1")
    print("Задача-2")
    print("Задача-3")
    do = input("Введите номер задачи (0 - Выход): ")

    # Задание-1:
    if do == "1":
        print("Задача-1")
        import os
        dirs = []
        for n in range(1, 10):
            dir_name = "dir_" + str(n)
            dir_path = os.path.join(os.getcwd(), dir_name)
            dirs.append(dir_path)
            try:
                os.mkdir(dir_path)
                print("Директория создана", dir_name)
            except FileExistsError:
                print("Директория уже существует в текущей папке")

        print("Желаете удалить папки?")
        delete = input("Yes / No : ")
        if delete == "Yes":
            for dir_name in dirs:
                try:
                    os.rmdir(dir_name)
                    print("Директория ", dir_name," удалена в текущей папке")
                except FileExistsError:
                    print("Директория ", dir_name," не существует, и не может быть удалена!")

        print("********************")

    # Задание-2:
    if do == "2":
        print("Задача-2")
        import os
        d = os.path.join(os.getcwd())
        subfolders = [f.path for f in os.scandir(d) if f.is_dir()]
        print(subfolders)
        print("********************")

    # Задание-3:
    if do == "3":
        print("Задача-2")
        import sys
        import os
        import shutil

        file_name = os.path.basename(sys.argv[0])

        print("Дублирование текущего файла")
        print("Текущий файл: ", file_name)
        answ = input("Хотите продублировать? Y / N : ")
        if answ == "Y":
            copyfile = file_name + '.copy'
            shutil.copy(file_name, copyfile)
            if os.path.exists(copyfile):
                print("Файл ", copyfile, " был успешно создан")
            else:
                print("Возникли проблемы копирования")
        else:
            continue
        print("********************")

    if do == "0":
        break
