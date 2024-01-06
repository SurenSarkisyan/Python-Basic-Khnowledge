# Set Множества
# Множества - Коллекция из уникальных элементов, в set храняться только уникальные значения
# Set - похож на dict где храниться ключ значение, а в set только значение
# В set порядок элементов не имеет никакого значения


# Пример создания Set

my_set = {1, 2, 3, 4, 5,}
print(type(my_set))
print(my_set)

# Второй пример создания Set

my_set = set()

for i in range(5):
    my_set.add(i)
print(my_set)

# Пример удаления элемента из set

my_set = {1, 2, 3, 4, 5,}

my_set.remove(2)
print(my_set)

# Пример обьединения двух множеств union

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))

# Пример вывода длинны множества

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

united_set = set1.union(set2)

print(len(united_set))
print(united_set)

# Пример нахождения пересечений для set, то-есть элементов которые присутствуют в двух сетах

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))

#  Пример применения метода сравнения difference между сетами

set1 = {1, 2, 3, 4, 7}
set2 = {3, 4, 5, 6}

print(set1.difference(set2))

# Пример создания set с помощью включений

squares = {x ** 2 for x in range(10)}

print(squares)

# В set порядок элементов не имеет никакого значения, важно чтобы оба сета включали одни и те же значения не важно в каком порядке

print({1, 2, 3} == {3, 2, 1})  # True

# Пример задачи с set с удалением дублей unique

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

unique_value = set(numbers)

print(type(unique_value))
print(unique_value)
unique_value = list(unique_value)  # Преобразование set в list
print(unique_value)

# Пример оптимизации вышестоящего кода в одну строку

unique_value = list(set(numbers))
print(unique_value)
print(type(unique_value))

