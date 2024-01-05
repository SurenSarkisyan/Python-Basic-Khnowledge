# args ** kwargs

# Пример суммирования x и y и возврат их суммы

def add(x: int, y: int):
    return x + y

print(add(x=10, y=5))

# Пример сложения множества элементов с использованием args*

def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

print(add_all(1,2,3,4,5,6,7))

# Пример сложения двух списков между собой с использованием функции

def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all(*values, *other_values))

# Пример передачи в функцию именованные аргументы с использованием **kwargs и метода items
# **kwargs - именнованые аргументы
# kwargs - это на самом деле словарь, функция type говорит об этом

def introduse(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
introduse(name="John", age=30, city="New York")  # Разные типы данных

# Пример задачи с помещением словаря в функцию с использованием двух звездочек **

def introduse(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person ={
        "city": "New York",
        "age": 30,
        "name": "John"
    }
introduse(**person)

# Пример функции которая примет все возможные варианты аргументов

def function_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

person ={
    "city": "New York",
    "age": 30,
    "name": "John"
}

function_with_all_arguments(1, 2, 3, 4, 5, **person)

# Пример возврата нескольких значений
# Пример функции которая будет модифицировать словари и возвращать первым аргументом модифицированный словарь
# а вторым аргументом был ли словарь модифицирован

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict,bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

product = {"id": 1, "name": "Laptop", "price": 999.99}


product, was_modified = modify_dict(old_dict=product, name="Laptop")
print(product)
print(was_modified)












