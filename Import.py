# Imports Модулей

# Модуль в Python - это файл который содержит код и имеет расширение .py
# Модуль может содержать исполняемый код а так же опредиление функций или классов,каждый модуль содержит приватное пространство имен
# Импорт в модуле нужен для того чтобы завести в локальное пространство имен нашего файла какие-то другие библиотеки или файлы, помогает лучше
# компоновать код и лучше в нем ориентироваться


my_int = 1
import json
print(globals().keys())  # globals содержит все переменные функции классы которорые мы можем использовать в коде


# Пример выбора рандомного элемента с листа методом random.choice
# Зажав ctrl по модулю на него можно щелкнуть и посмотреть содержимое ctrl random


import random

my_list = [1, 2, 3]
print(random.choice(my_list))
print(globals().keys())

# Пример просмотра методов для модуля random

import random

print(dir(random))

# Пример импорта функций с файла math_operation_for_import

from Test.math_operation_for_import import add, subtract

print(add(1, 2))
print(subtract(1, 2))

# Пример импорта функций с файла math_operation_for_import
# В случае если импорт не работает нужно обратить внимание на файл __init__.py он говорит о том что вся папка является питоновским пакетом
from Test import math_operation_for_import

print(math_operation_for_import.add(1, 2))
print(math_operation_for_import.subtract(1, 2))

















