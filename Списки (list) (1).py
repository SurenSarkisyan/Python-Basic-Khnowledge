# Списки - List - Структура которая используется для хранения упорядоченных последовательностей
# Списки так же имеют длинну для того чтобы ее узнать нужно использовать метод len

# Пример Списка с однородными данными то-есть только строки

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Пример списка с разными типами данных к примеру числа и строки, а так же пример вхождения списка в список
# Так же примером хорошего тона есть написания списка с однородным типом данных то-есть не мешать типы данных

my_list = ["apple", 1, 1.5, True, [1, 2, 3]]
print(my_list)

# Пример сравнения списков друг с другом результатом сравнения которого будет True если данные в списках равны или False если не равны
# == - сравнение
my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]
print(my_list1 == my_list3)

# Пример применения функции bool

print(bool([]))  # bool щт пустого списка будет False
print(bool([1]))  # bool от списка в котором есть хотя бы один элемент даже ноль то будет True

# Пример в котором мы можем просмотреть то или иное значение в списке результатом которого будет True если значение есть или False если его нет

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Ключевой оператор in как в SQL оператор вхождения искомого значения
print("watermelon" in fruits)  # False Пример так как данного значения нет в списке

# Пример в котором переменные можно поместить в список

elementn1 = "apple"
elementn2 = "banana"
elementn3 = "cherry"

fruits = [elementn1, elementn2, elementn3]
print(fruits)

# Пример составления списков из строк в котором каждая буква из слова Hello будет выведена отдельным списком

word = "Hello"
my_list = list(word)
print(my_list)

# Пример сложения списков друг с другом

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)

# У списков есть определенное количество методов где изменения присваиваются в первоначальную переменную

fruits = ["apple", "banana", "cherry"]
fruits.append("watermellon")  # append - метод добавления значения в список
print(fruits)

# В строках есть нюанс в том что первоначальная переменная не изменяется а метод replace отрабатывает во второй
# переменной в данном примере new_string

my_string = "Hello World"
new_string = my_string.replace("World", "Python")
print(my_string)
print(new_string)

# Пример метода pop в котором будет взят последний элемент списка удален  и присвоен переменной fruit
# В итоге наш список будет состоять из двух элементов а строка cherry будет присвоена переменной fruit

fruits = ["apple", "banana", "cherry"]
fruit = fruits.pop()
print(fruit)
print(fruits)

# Пример метода pop без присвоения для переменной

fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

# Пример добавления второго списка к первому метод extend

fruits = ["apple", "banana", "cherry"]
fruits2 = ["fig", "grape"]
fruits.extend(fruits2) # Список который мы хотим добавить
print(fruits)


# Пример разворота списка метод reverse

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

# Пример сортировки списка метод sort где значения будут отсортированы по возрастанию

my_list = [5, 4, 8, 10, 1, 2, 14, 4, 6, 9]
my_list.sort()
print(my_list)

# Пример сортировки списка метод sort где значения будут отсортированы по убыванию

my_list = [5, 4, 8, 10, 1, 2, 14, 4, 6, 9]
my_list.sort(reverse=True) # Пример присвоения функции reverse для метода sort с значением True что дает возможность применить сортировку по убыванию
print(my_list)

# Пример создания списка из слов разделенных пробелами в строке метод split

my_string = "My name is Alex"
my_list = my_string.split(" ")
print(my_list)

# Пример сборки из списка строки с словами разделенными пробелами

joined_string = " ".join(my_list)
print(joined_string)

# Пример списки можно передавать в различные функции которые работают с числами строками и тд...
# Так же списки с int и str типом данных не складываются

my_list = [5, 4, 8, 10, 1, 2, 14, 4]
print(max(my_list)) # Пример метода мах где мы узнаем максимальный элемент в списке
print(min(my_list)) # Пример метода мin где мы узнаем минимальный элемент в списке
print(sum(my_list)) # Пример метода sum где мы узнаем сумму элементов в списке

# Пример присваивания переменных и пропуска при помощи символа _

user_roles = ["admin", "editor", "watcher"]
role_1, role_2, _ = user_roles  # Пример присваивания переменных и пропуска при помощи символа _
print(role_1)
print(role_2)

