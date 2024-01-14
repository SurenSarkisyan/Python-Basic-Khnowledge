# Декораторы

# Декоратор - синтаксический сахар это консрукция языка которая делает более быстрым написание каких-то частотных паттернов,
# в Python декоратор это функция которая принимает как аргумент другую функцию и обогощяет поведение принимаемой функции

# Пример обьявления декоратора

def my_decorator(func):
    def wrapper(*args,**kwargs):  # Обьявление функции wrapper (обертка) внутри my_decorator
        print("Somthing is happen before function is called")
        func(*args,**kwargs)
        print("Somthing is happen after function is called")

    return wrapper

def say_hello():  # Пример без синтаксического сахара
    print("Hello!")

my_decorator(say_hello)()

@my_decorator
def say_hello(*, name: str) -> None:  # Пример с использованием синтаксического сахара
    print(f"Hello {name}!")

say_hello(name="John")



# Пример декоратора
def my_decorator(func):
    def wrapper(*args, **kwargs):  # Обьявление функции wrapper (обертка) внутри my_decorator
        print("Somthing is happen before function is called")
        result = func(*args, **kwargs)
        print("Somthing is happen after function is called")
        return result

    return wrapper

# Пример сложения
@my_decorator
def add_numbers(*, a: int, b: int) -> int:  # Пример с использованием синтаксического сахара
    print("Numbers Adding")
    return a + b

result = add_numbers(a=1, b=2)

print(result)































