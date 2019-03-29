# 2. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки
# компьютер сообщает меньше или больше загаданное число. В конце игры текст с результатом
# (или “Вы угадали”, или “Попытки закончились”).
#
import random

n = int(input('Введите N: '))
number = random.randint(1, n)

k = int(input('Введите k: '))

while k > 0:
    k -= 1
    attempt = int(input('Введите догадку какое число загадал компьютер: '))
    if attempt < number:
        print('Вы ввели слишком маленькое число. Осталось ' + str(k) + ' попыток')
    elif attempt > number:
        print('Вы ввели слишком большое число. Осталось ' + str(k) + ' попыток')
    else:
        print('Вы угадали!')
        exit(0)

print('Попытки закончились, Вам не повезло угадать число ' + str(number) + '. Попробуйте ещё!')

