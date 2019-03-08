# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re
name = str(input('Введите имя: '))
surname = str(input('Введите фамилию: '))
mailAdress = input('Адрес электронной почты: ')

nameFormat = '[А-Я][а-я]*'
surnameFormat = '[А-Я][а-я]*'
mailFormat = '[a-z_0-9]+@[a-z]+\.[a-z]+'

if (re.match(nameFormat, name) is not None)\
    and (re.match(surnameFormat, surname) is not None)\
    and (re.match(mailFormat, mailAdress) is not None):
    print('Все введено верно, продолжайте работу')
else:
    print('Проверьте правильность ввода данных')




