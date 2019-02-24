print('Введите данные о пациенте: имя, фамилия, возраст и вес')
name = str(input('Имя: '))
surname = str(input('Фамилия: '))
age = int(input('Возраст: '))
weight = int(input('Вес: '))

if name and surname and age and weight:
    isWeightGood = (50 < weight < 120)
    if age <= 30 and isWeightGood:
        print("Вы в хорошей форме, осмотр врача не требуется")
    elif (30 < age < 40) and not isWeightGood:
        print('Вам требуется начать вести правильный образ жизни')
    elif age >= 40 and not isWeightGood:
        print('Срочно обратиться к врачу')
    else:
        print('Необходимо пройти осмотр в случае плохого самочувствия')
else:
    print('Вы ввели не все данные о пациенте')