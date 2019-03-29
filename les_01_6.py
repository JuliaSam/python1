#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

user_index = int(input('Введите индекс буквы (от 1 до ' + str(len(alphabet)) + '): '))
print(alphabet[user_index - 1])


