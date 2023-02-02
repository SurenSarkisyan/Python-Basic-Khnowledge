
# Comments - Переменные и типы данных

# number = 5 - переменной number присвоено значение 5, можно задать число с точкой положительное и отрицательное с точкой
# print("Результат:", number) - вывод переменной
# del number - удаление переменной
# digit = 4.53435464 - возможность задать число с точкой положительное и отрицательное с точкой - название переменной может быть любое
# word = "Результат:" - Возможность задать строкое значение - название переменной может быть любое
# boolean = False - тип данных bool
# boolean = True - тип данных bool
# str - string - преобразовывает любые типы данных в строку str(digit) digit может быть любое число
# int - integer - преобразовывает любые типы данных в число int(str_num) - str_num = '5' - что есть строка
# boolean - преобразовывает в bool тип данных
# float - преобразовывает к типу данных float

# Example 1

number = 5            # integer - тип данных
digit = 4.53435464    # float - тип данных
word = "Результат: "  # string - тип данных
boolean = False       # boolean - тип данных
str_num = 5           # string

print(word + str(digit))

print(word + str(number + int(str_num)))

del number

number = 7
print("Результат:", number)

# Example 2

num1 = int(input("Введите первое число: "))

num2 = int(input("Введите второе число: "))

num1 = num1 + 5      # или num1 += 5 и так можно использовать остальные операции математические

print("Result:", num1 + num2)
print("Result:", num1 - num2)
print("Result:", num1 / num2)
print("Result:", num1 * num2)
print("Result:", num1 ** num2)
print("Result:", num1 // num2)

# Example 3

word = "Hi"          # string - добавляется тип данных автоматом
print(word * 2)      # это значит что строка будет умножена выведена дважды на экран и так далее

del word

word = "Hello"
print(word)

# Example 4

0.5 ** 3            # корень из трех






