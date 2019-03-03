# easy 1
def infoHuman(name, age, city):
    print(name + ', ' + age + ' год, ' + 'проживаает в городе ' + city)

name = str(input('Ваше имя: '))
age = input('Введите ваш возраст: ')
city = input('Место жительства: ')

infoHuman(name, age, city)