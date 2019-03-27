#5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.

firstChar = input('Введите первую букву: ').lower()
lastChar = input('Введите вторую букву: ').lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

place_first = alphabet.index(firstChar) + 1
place_second = alphabet.index(lastChar) + 1

print('Место первой буквы: ' + str(place_first))
print('Место второй буквы: ' + str(place_second))

count = place_second - place_first - 1
print('Букв между ними: ' + str(count))

