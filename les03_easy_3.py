# easy 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def longStr(*args):
    longestString = max(args, key=len)
    print(longestString)

arg1 = str(input("Первая строка: "))
arg2 = str(input("Вторая строка: "))
arg3 = str(input("Вторая строка: "))

longStr(arg1, arg2, arg3)
