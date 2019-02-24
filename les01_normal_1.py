number = int(input('Введите любое целое число: '))
while number > 10 or number <= 0:
   number = int(input('Неверно! Введите любое целое число от 0 до 10: '))

print('Правильно! Ваше новое число: ')
newNumber = number ** 2
print(newNumber)
