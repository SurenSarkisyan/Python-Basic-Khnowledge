# Словари Dictionary

# Словари - структура с именноваными полями, набор ключ - значение, ключи словаря должны быть уникальными

# Пример объявления словаря

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)

# Пример присвоения других ключей в созданный словарь

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

person ["job"] = "Engineer"

print(person)

# Еще пример как можно объявлять словарь

person = {}

person["name"] = "John"
person["age"] = 30
person["city"] = "New York"

print(person)

# Пример вызова значения в словаре по ключу

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Пример вывода объекта которого мы создали то-есть John
print(person["age"])

# Пример вызова значения с использованием метода get

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person.get("name"))  # Для несуществующего обьекта не будет падать ошибка в консоле но будет выведено значение None

# Пример в котором в метод get будет помещено дефолтное значение которого нет в словаре

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person.get("country", "USA"))

# Пример итерации по словарю и запроса по ключу

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for p in person:
    print(person[p])

# Второй Пример итерации по словарю и запроса по ключу с применением метода items

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key, value in person.items():  # Распаковка ключ + значение в виде кортежа
    print(key)
    print(value)

# Пример итерации только по ключам с применением метода keys

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in person.keys():
    print(key)

# Пример итерации по значениям с использованием метода values

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for value in person.values():
    print(value)

# Пример сравнения словарей diff для словарей результатом которого будет true или false
# Для словаря порядок не важен потому что ключи у нас всегда уникальные
# true в случае если все совпадает
# false в случае если хоть одно значение не есть равным или в одном и во втором сравниваемых словарей будет разное колличество ключей

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

other_person = {
    "city": "New York",
    "age": 30,
    "name": "John",
    "country": "Ukraine"
}

# Пример объединения двух словарей методом update где "city" будет браться из последнего объекта из того который обновляет
# первоначальный объект то-есть additional_person_info обновляет person

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

# Второй Пример объединения двух словарей с использованием | - пайп лайна

person.update(additional_person_info)
print(person)

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

person = person | additional_person_info
print(person)