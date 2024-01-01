# Условные Операторы
# if, else, elif, - Условные операторы, Есть правила при написании кода, с выводом блока кода под условие.

# if True:
#    print("Hello World")

# Пример использования if

x = 10
if x > 0:
    print("x is positive")

x = -10
if x > 0:
    print("x is positive")

# Несколько условий в котором для else будет выведено исключение всего того что не припадает под if, elif

x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Пример использования if

x = 10
y = 20
if x > 0 and  y > 0:
    print("x and y are positive")

# Пример использования условных операторов так как в переменной есть значение блок кода будет исполнен

message = "Hello World"
if message:
    print("message is not empty")

x = 1
if x:
    print("x is not zero")



