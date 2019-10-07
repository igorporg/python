_author__ = 'Igor A.Provorov'

print("HOMEWORK 4 normal")

while 1:
    print("Задача-1")
    print("Задача-2")
    print("Задача-3")
    do = input("Введите номер задачи (0 - Выход): ")

    if do == "1":
        # Задание-1:
        # Вывести символы в нижнем регистре, которые находятся вокруг
        # 1 или более символов в верхнем регистре.
        # Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
        # Решить задачу двумя способами: с помощью re и без.

        line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
               'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
               'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
               'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
               'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
               'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
               'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
               'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
               'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
               'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
               'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
               'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
               'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
               'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
               'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

        lowcase = 'abcdefghijklmnopqrstuvwxyz'
        #uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        list = []
        str = ""
        for s in line:
            if s in lowcase:
                str = str + s
            else:
                if str:
                    list.append(str)
                    str = ""
        print(list)

        import re
        pattern = '[a-z]+'
        found = re.findall(pattern, line)
        print(found)
        print("********************")

    # Задача-2
    if do == "2":
        # Задание-2:
        # Вывести символы в верхнем регистре, слева от которых находятся
        # два символа в нижнем регистре, а справа - два символа в верхнем регистре.
        # Т.е. из строки
        # "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
        # нужно получить список строк: ['AY', 'NOGI', 'P']
        # Решить задачу двумя способами: с помощью re и без.

        line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
                 'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
                 'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
                 'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
                 'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
                 'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
                 'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
                 'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
                 'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
                 'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
                 'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
                 'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
                 'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
                 'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
                 'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

        lowcase = 'abcdefghijklmnopqrstuvwxyz'
        #uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        list = []
        str_small = ""
        str_big = ""
        for s in line_2:
            if s in lowcase:
                if len(str_small) >= 2 and len(str_big) >= 4:
                    list.append(str_big[:-2])
                    str_small = ""
                else:
                    str_big = ""
                str_small = str_small + s

            else:
                str_big = str_big + s

        print(list)

        import re
        pattern = '[a-z]{2}([A-Z]{2,})[A-Z]{2}[a-z]+'
        found = re.findall(pattern, line_2)
        print(found)
        print("********************")

    # Задача-3
    if do == "3":
        print("Задача-3")
        # Задание-3:
        # Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
        # произвольными целыми цифрами, в результате в файле должно быть
        # 2500-значное произвольное число.
        # Найдите и выведите самую длинную последовательность одинаковых цифр
        # в вышезаполненном файле.

        print("********************")


    if do == "0":
        break
