#задание 2 normal
#не совсем понятно, как без math извлекать корень
import math
numbers = [2, -5, 8, 9, -25, 25, 4]
newlist = []
for i in numbers:
    if (i > 0) and (math.sqrt(i)%1 == 0):
        newlist.append(int(math.sqrt(i)))
print(newlist)