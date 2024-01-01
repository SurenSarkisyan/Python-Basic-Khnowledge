# Обьявление строки в одинарных и двойных кавычках данная опция на усмотрение кому как удобно

my_string = "Hello World"
my_string = 'Hello World'
print(my_string)

# Присвоение большого текста для переменной

my_string = """
Логика проверки данного кейса заключается в том что при отправке сообщения с тегом 76 в мип коммон сообщении отображается парти блок с неназначеными значениями, 
так же когда 76 тег присудствует сообщение отображаетсякореектно с правильным оторбажением парти блока в мип комон сообщении, как теструем, отсылаем сообщение без парти груп тегов, 
и соответственно в екзекюшн репорте к мип комон сообщении не должен мапиться андефайн блок парти груп.
"""
print(my_string)

# Сложение строк друг с другом

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name  # " " - пробел
print(full_name)

# Узнать длину строки - количество символов в строке

lenght = len(full_name)
print(lenght)

print(len(""))  # Длинна пустой строки

# Пример перевода из численного типа в строковый str

my_integer = 100
my_string = str(my_integer)
print(type(my_string))

# Пример перевода из строкового типа в численный int

my_integer = int("10")
print(type(my_integer))

# Пример получения для функции input вводимой пользователем

my_integer = int(input("Enter your number: "))
print(type(my_integer))

# Оператор in помогает найти вхождение подстроки в строку в данном примере мы ищем Hello как
# вхождение в строку если значение есть результатом будет True or False, так же данный метод регистрозависимый

my_string = "Hello World"
print("Hello" in my_string)

# Вывод строки написанная Кепсом метод Upper()

my_string = "Alice"
print(my_string.upper())

# Вывод строки написанная Кепсом метод lower()

y_string = "ALICE"
print(my_string.lower())

# Метод strip() для удаления ненужных пробелов в строке

my_string = "   Hello World   "
print(len(my_string))
print(len(my_string.strip()))

# Замена слов или символов внутри строки replace()

my_string = "Hello World"
print(my_string.replace("World", "Python"))

# Подсчет количества вхождения символов в строке count()

my_string = "Hello World"
print(my_string.count("l"))

# Определение того есть ли в строке цифры isdigit()

my_string = "10"
print(my_string.isdigit())

# Пример при вводе числа пользователем

my_integer = input("Please enter number: ")
if my_integer.isdigit():
    my_integer = int(my_integer)
print(type(my_integer))

# Пример того как в строку можно вставить какие-либо данные Форматирование - f
# В данном примере используем параметр f и указываем в фигурных скобках переменные с нужными значениями

name = "Alice"
age = 25
print(f" Hello, my name is {name} and i {age} years old ")

x = 10
y = 10
print(f" Summary {x + y} is, multiplication {x * y} is ")


my_string = input("Enter Number: ")
if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")