# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

is_possible = True
# Question: How to write `is_possible and= some_logical_value`?
is_possible = is_possible and (a < b + c)
is_possible = is_possible and (b < c + a)
is_possible = is_possible and (c < a + b)

if is_possible:
    if a == b and b == c:
        print('Это равносторонний треугольник')
    elif a == b or b == c:
        print('Это равнобедренный треугольник')
    else:
        print('Это разносторонний треугольник')
else:
    print('Треугольник с такими сторонами не может существовать')
