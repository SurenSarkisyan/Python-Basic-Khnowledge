# Индексы и Слайсы (Срезы)
# В программировании отчет начинается с нуля

# Диапазон значений для индексов

# my_string = "Hello"
#  0  1  2  3  4
#  H  e  l  l  o
# -5 -4 -3 -2 -1

# Возможный диапазон значений
# -len(my_string) ... len(my_string) -1 так же можно использовать отрицательные значения к примеру диапазон моет быть от -5 до 4

# Пример в котором мы выводим значение идущее в списке первым то-есть apple

fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits[0]) # Вызов apple по индексу 0
print(fruits[-4]) # Вызов apple по индексу -4
print(fruits[3])

# Пример использования индексов, пример присвоения в список и замены значения по индексу в списке

fruits = ["apple", "banana", "cherry", "watermelon"]
fruits[0] = "pineapple"
print(fruits)

# Пример перестановки элементов в списке с помощью индексов

fruits = ["apple", "banana", "cherry", "watermelon"]
fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits)

# Пример Срезов (Slices)

# Слайс - это всегда полуоткрытый интервал
# Элемент с закрывающим индексом не входит в конечную выборку

numbers = [0, 1, 2, 3, 4, 5, 6]
numbers[0:3]  # [0, 1, 2] - Пример вывода трех элементов



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])  # Пример выбора первых пяти элементов

# Пример Срезов (Slices) с присвоением в новую переменную

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:5]
print(new_numbers)

# Пртимер вывода полного списка с использованием метода len

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:5]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[:] # Так же пример вывода полного списка
print(new_numbers)


# Пример использования шага в слайсах

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:10:2] # Пример шага где будет отображено [0, 2, 4, 6, 8]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[::2] # Пример шага где будет отображено [0, 2, 4, 6, 8]
print(new_numbers)

# Пример использования отрицательных значений для слайсов
# Есть рекомендация для использования положительных значений для слайсов что снижает когнитивное восприятие кода

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[-5:-1] # Пример шага где будет отображено [5, 6, 7, 8]
print(new_numbers)

# Пример разворота слайсов в обратном порядке

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[::-1]
print(new_numbers)

# Пример работы со строками

string = "Hello, World"
print(string[5:]) # Вывод с пятого символа до самого конца

# Пример вывода каждого второго элемента

string = "Hello, World"
print(string[::2])

# Пример трех способов как можно развернуть list

# 1 Способ

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[::-1]
print(new_numbers)

# 2 Способ метод reverse

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)

# 3 Способ Функция Reversed обернутая в метод list

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = list(reversed(numbers))
print(type(new_numbers))
print(new_numbers)

