#задание 2 easy
fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'огурец']
vegetables = ['банан', 'огурец', 'киви', 'помидор', 'тыква']
onlyfruits = list(set(fruits) - set(vegetables))
print(onlyfruits)