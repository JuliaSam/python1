# normal 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python

separator = " - "


def write_salary_to_file(filename, salary_info):
    with open(filename, 'w', encoding='UTF-8') as file:
        new_line_format = "{}" + separator + "{}\n"
        for name, money in salary_info.items():
            if money < 500000:
                file.write(new_line_format.format(name, money))


def print_from_file(filename, taxes):
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            splitted = line.split(separator)
            uppercased = splitted[0].upper()
            final_salary = float(splitted[1]) * (1 - taxes)
            print(uppercased, final_salary)


names = ['Ivan', 'Vladimir', 'Gleb', 'Misha']
salary = [10000, 560000, 80000, 155000]
dict_salary = dict(zip(names, salary))
salary_filename = "salary.txt"

write_salary_to_file(salary_filename, dict_salary)
print_from_file(salary_filename, 0.13)
