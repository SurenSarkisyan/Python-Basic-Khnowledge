# Цикл For - Возможно одна из самых частотных конструкций которая будет использоваться в коде

# Пример вывода значений из списка в терминал с использованием for
# Каждое исполнение цикла называется его итерацией, количество итераций в цикле for равно количеству элементов
# которое мы перебираем в коллекции, списке

file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
for file_name in file_names:
    print(file_name)

# Пример использования цикла for со строками

greeting = "Hello World!"
for characters in greeting:
    print(characters)

# Пример использования цикла for со строками
# Пример синтаксического сахара

# count = count + 1
# count += 1

# count = count - 1
# count -= 1

# count = count * 2
# count *= 2

greeting = "Hello World!"
count_o = 0
for characters in greeting:
    if characters == "o":
        count_o += 1
        print(characters)
print(count_o)


# Пример циклов вложеных друг в друга
# Данный цикл выполняется последовательно с отображением значений, вложенный цикл есть
# признак плохого тона, есть договоренность внегласная что максимум может быть один вложенный цикл далее программу желательно дробить

students = ["Alice", "Bob", "Charlie", "David"]

for student in students:
    print(student)
    for characters in student:
        print(characters)

# Пример использования ключевого слова continue

# В данном примере у нас есть условие при котором если четное число будет делиться на 2 без остатка
# то слово continue отведет нас обратно к началу цикла for где программа будет выполена снова и наше число нечетное которое удовлетворяет
# условию будет выполнено в функции print

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    if num % 2 == 0: # Пример вывода нечетного числа в терминал. % 2 - остаток от деления на 2 == 0
        continue
    print(num)

# Пример использования ключевого слова break

# Пример если число равно 10 мы остановим цикл и не исполняем его дальше а все числа которые меньше 10 мы выведем в терминал

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    if num == 10:
        break
    print(num)


# Пример использования функции range, данная функция генерирует последовательности чисел

range_object = range(10)
print(list(range_object))

numbers = list(range_object)
print(numbers)

range_object = range(1, 10)
print(list(range_object))

range_object = range(1,10, 2) # Пример использования шага с диапазоном 2 и вывода каждого второго числа в списке
print(list(range_object))

range_object = range(10, 1, -1) # Пример убывающей последовательности отобразит список наоборот
print(list(range_object))

# Пример в котором к каждому числу добавляем единицу и меняем список
# int переменная не может меняться в Python, но тип переменной список может меняться по индексу
# i - пример обозначения переменной индекс

numbers = [10, 11, 12, 13, 14, 15]
for i in range(len(numbers)): # Пример передачи в функцию range аргумента len для вывода длинны массива
    numbers[i] += 1
    print(numbers)

# Пример определения количества букв, а так же их индексы

greeting = "Hello World!"

indexes = [0]
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)
print(count)
print(indexes)

















