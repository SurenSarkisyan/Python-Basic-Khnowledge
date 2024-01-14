# Работа с файлами

# Пример записи в файл json данных

import json

data = {"name": "Mike", "age": 30, "city": "New York"}

file = open("files/Работа с файлами data.json", "w")  # "w" - режим записи от английского слова write

json.dump(data, file, indent=4)  # dump - запись информации в файл, indent - отступы для красоты

file.close()  # Закрытие файла важно так как может произойти утечка памяти

# Пример чтения информации из файла

file = open("files/Работа с файлами data.json", "r")  # "r" - режим чтения от английского слова read

loaded_data = json.load(file)

file.close()
print(loaded_data)

# Пример работы с csv файлом
# csv - посторочный набор данных разделенный сепаратором

import csv

rows = [['name', 'age', 'occupation'],
        ['John', 28, 'Engineer'],
        ['Marie', 22, 'Designer'],
        ['Mike', 32, 'Doctor']]

file = open("files/Работа с файлами person.csv", "w")

csv_writer = csv.writer(file)

csv_writer.writerows(rows)

file.close()

# Чтение csv файла с использованием класса dict reader

file = open("files/Работа с файлами person.csv", "r")

csv_dict_reader = csv.DictReader(file)

for row in csv_dict_reader:
        print(row["name"], row["age"], row["occupation"])
file.close()

# Пример добавления новых строк в файл Работа с файлами person.csv

Работа с файлами person.csv = [

        {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
        {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]

file = open("files/Работа с файлами person.csv", "a")  # add - добавление
fields = ['name', 'age', 'occupation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(Работа с файлами person)

file.close()