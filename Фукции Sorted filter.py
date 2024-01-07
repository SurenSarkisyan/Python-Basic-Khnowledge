# Функции Sorted filer сортировка и фильтрация

# Сортировка - количество элементов не изменяется, элементы изначальной выборки включены в конечную, но меняется
# порядок элементов по определенному признаку: [1, 3, 2] -> [1, 2, 3]

# Фильтрация - конечная выборка может не включать элементы из первоначальной. Элементы попадают в конечную выборку
# по определенному признаку: [1, 2, 3, 4, 5] -> [2, 4] четные числа

# Пример сортировки по алфавиту

fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)

# Пример сортировки по алфавиту в обратном порядке

fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)

# Пример сортировки слов по длине

fruits = ["banana", "apple", "cherry", "date"]

def sort_by_len(element: str) -> int:
    return len(element)

print(sort_by_len)
print(type(sort_by_len))

# Пример передачи оной функции в другую как аргумент

fruits = ["banana", "apple", "cherry", "date"]

def sort_by_len(element: str) -> int:
    return len(element)

sorted_fruits = sorted(fruits, key=sort_by_len)

print(sorted_fruits)

# Пример использования сортировки key=

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]
def sort_by_age(person: dict) -> int:
    return person["age"]

sorted_peole = sorted(people, key=sort_by_age)
print(sorted_peole)

# Пример использования сортировки по двум признакам key=, в случае если у обьектов одинаковый возраст
# мы их сортируем по алфавиту

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 30}
]

def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_peole = sorted(people, key=sort_by_age_name)
print(sorted_peole)

# Пример Функции Filter с результатом вывода
def is_even(n: int) -> bool:
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_numbers = list(filter(is_even, numbers))

print(type(filtered_numbers))
print(filtered_numbers)

# Пример Функции Filter с результатом вывода

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "Diana", "age": 40}
]

def is_adult(person: dict) -> bool:
    return person["age"] >= 18

filtered_people = list(filter(is_adult, people))
print(filtered_people)
























































