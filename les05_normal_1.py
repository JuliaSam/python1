# normal 1 lesson 5

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

#не создавала отдельный файл с функциями

import os
while True:
    chooseNumber = int(input('[1] - Перейти в папку\n[2] - Просмотреть содержимое текущей папки\n[3] - Удалить папку\n[4] - Создать папку\nВаш выбор: '))
    if chooseNumber == 1:
        try:
            nameOfFile = input('Введите название папки: ')
            print(os.chdir(nameOfFile))
            print('Вы перешли в папку' + nameOfFile)
        except FileNotFoundError:
            print('Проверьте корректность написания, ошибка')
    elif chooseNumber == 2:
        print(os.listdir())
    elif chooseNumber == 3:
        try:
            deleteFileName = input('Введите название файла, которое хотите удалить: ')
            os.rmdir(deleteFileName)
            print('Файл удален')
        except FileExistsError:
            print('Такого файла не найти, проверьте корректность')
    elif chooseNumber == 4:
        try:
            newFileName = input('Введите название файла: ')
            os.mkdir(newFileName)
            print('Файл создан')
        except FileExistsError:
            print('Такой файл уже создан')
    else:
        print('Вы ввели недопустимое значение')