#задание 3 easy
numbers = [1, 10, 25, 8, 72, 3, 18, 165, 55, 1000]
newlist = []
for i in numbers:
    if i%2 == 0:
        newlist.append(i/4)
        newlist.append(i*2)
print(newlist)