# Функция - Блок кода для многократного повторения


# Пример получения среднего элемента в списке
# DRY - Dont Repeat Yourself хороший код не должен повторяться для этого есть функции

numbers1 = [1, 2, 3, 4, 5]
average_1 = sum(numbers1) / len(numbers1)
print(average_1)

# Пример написания функции с ключевым словом def
# None - функция когда нет ключевого слова return возвращает ничего
# Функции в Питон отделяются от основного блока кода двумя строками

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers1)
average_2 = find_average(numbers2)
print(average_1, average_2)


# Пример функции которая считает количество гласных в строке

def count_vowels(string):
    VOWELS = "aeiouAEIOU"   # Константа в питоне пишеться капсом и является неизменяемым значением
    count = 0
    for characters in string:
        if characters in VOWELS:
            count +=1

    return count

print(count_vowels("Hello World!"))
print(count_vowels("Python is very powerful language!."))

# Пример заглушки чтобы функция ничего не исполняла
# Для создания кодовой базы и модификации в дальнейшем

# def nothing():
#    pass    # Аргумент говорящий о том что функция не будет исполнена

# nothing()

# Пример функций с более чем одним аргументом
# Примером хорошего тоная является обьявление типов данных для переменных и применение звездочки

def format_date(*, day: int, month: str) -> str:  # -> Обьявление типа возвращяемого значения, * - явное лучше не явного, не даст возможность попутать типы данных при выводе
    return f"The date is {day} of {month}"

print(format_date(day=15, month="October"))


# Пример объявления Дефолтных аргументов в функциях

def custom_greeting(*, name:str, greeting:str = "Hello") -> str:
    return f"{greeting}, {name}"

print(custom_greeting(name="John", greeting="Good Morning"))
print(custom_greeting(name="John"))