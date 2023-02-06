
# Comments Множества (set и frozenset)

# Множества - скожи с списками и все элементы идут в случайном порядке
# А так же в множестве не могут быть повторяющиеся элементы, так же можно преобразовывать
# готовые списки в множества и тем самым удалять все повторяющиеся элементы.
# Frozen set - обьединение кортежа и множества
# set и frozenset -мы можем создавать различные множества где у нас не будет повторяющихся элементов
# а так же все элементы будут выведены в хаотичном порядке

# Example 1

data = set("Hello")        # set - функция для преобразования списка или слова в множество.

print(data)

# Example 2

data = {5, 7, 4, 3, 5}     # Вывод в случайном порядке где повторяющиеся элементы будут удалены

print(data)

# Example 3

data = {5, 7, 4, 3, 5}

data.add(32)                      # add - функция добавления одного значения
data.update(["32", True, 4, 6])   # update функция добавления много значений с разными типами данных
data.remove(True)                 # remove функция удаления значения
data.pop()                        # pop - функция удаления первого элемента
data.clear()                      # clear - полное очищение

print(data)

# Example 4

data = {5, 7, 4, 3, 5}             # Вывод множества - пример удаления повторных значений

nums = [5, 7, 3, 5, 5]

new_nums = set(nums)

print(data)


# Example 4 Frozen set - замороженное множество

new_data = frozenset([5, 7, 4, 3, 5,"32", True, 4, 6])    # Пример создания кортежа плюс множества, свойства кортежей мы не можем
                                                          # ничего в кортежах добавлять удалять и видоизменять
print(new_data)
