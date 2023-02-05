
# Comments Словари (dict) и работа с ними в языке Python
# {} - символ создания словарей
# [] - искомый кюч помещяем в скобки


# Example 1


country = {4: 3}                # {4: 3} - в данном примере 4 является ключем к значению 3, клбчи могут быть разных типов данных
print(country[4])               # пример вывода значения по ключу будет выведено значение 3 пример вывода всегда в квадратных скобках

# Example 2


country = {(5, 6): 3}           # возможность задать ключ как кортеж
print(country[5, 6])            # пример вывода по ключу всегда в квадратных скобках

# Example 3


country = {"code": "UA", "name": "Ukraine", "population": 45}    # множественное присвоение ключей - "code": "name": "population": - выведут соответсвующие данные
print(country["population"])                                     # поиск по ключу в данном примере будет выведено 45

# Example 4


country = dict(code="UA", name="Ukraine")      # Пример присвоения ключа при помощи dict
print(country["name"])                         # поиск по искомому ключу

# Example 5


country = {"code": "UA", "name": "Ukraine", "population": 45}
print(country)                                                   # Вывод в фигурных скобках что говорит о том что мы работаем со словаренм

# Example 5

country = {"code": "UA", "name": "Ukraine", "population": 45}

for key in country:                                              # в данном примере через цикл for мы будем получать исключительно ключи
    print(key)


# Example 6

country = {"code": "UA", "name": "Ukraine", "population": 45}

print(country.items())                                           # items - В данном примере мы получаем список где каждый элемент это опредиленный кортеж состоящий из двух
                                                                 # элементов это ключ и его значение


# Example 7

country = {"code": "UA", "name": "Ukraine", "population": 45}

for key, value in country.items():
    print(key, " - ", value)                          # Вывод данной конструкции - # code - UA
                                                                                   # name  -  Ukraine
                                                                                   # population  -  45

# Example 8 Функции при работе с словарями

country = {"code": "UA", "name": "Ukraine", "population": 45}

print (country.get("name"))          # get - Метод получения значения по опредиленному ключу
country.clear()                      # clear - метод полного очищения словаря от всех элементов
country.pop("name")                  # pop - метод удаления опредиленного ключа будет выведены все значения кроме name
country.popitem()                    # popitem - метод при котором каждый раз удаляется последний элемент
country["code"] = "None"             # update - Пример обновления значения которое было присвоено ключу "code"
print(country.keys())                # keys - в данном выводе метод получения списка - ключей
print(country.values())              # values - метод получения только списка значений
print(country.items())               # Вывод списка кортежей где каждый элемнт это ключей и значение

# Example 9

person = {
    "user_1": {
        "first_name": "John",
        "last_name": "Marley",
        "age": "45",
        "address": ("city - New York", "street Long - Way 45", "Appartment 45"),   # () - вложеный список
        "Grades": {"Math": 5, "Physics": 5 }                                       # {} - вложеный словарь
    },
    "user_2": {

    }
}
print(person["user_1"]["address"][1])      # В данном примере есть возможность вывести любую вложенность нашего словаря
                                           # person, последовательное обращение к элементам user_1, address, [1] - где [1] - это индекс в кортеже address.
                                           # в случае если [1] не указывать при выводе то будет отображен целый кортеж address


















