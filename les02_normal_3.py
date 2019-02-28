#задание 3 normal
import random
count = int(input('Количество элементов: '))
randomList = []
i = 0
while i < count:
    randomList.append(random.randint(-100, 100))
    i += 1
print(randomList)