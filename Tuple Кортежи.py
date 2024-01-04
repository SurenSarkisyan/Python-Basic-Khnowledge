# Кортежи Tuple
# Tuple - похожи на list но они не изменяются
# Tuple применяется тогда когда мы точно знаем что структуру данных не придеться менять
# Tuple применяется с функциями


# Пример синтаксиса Tuple

my_tuple = ("admin",)  # tuple с одним элементом
print(type(my_tuple))

user_roles = ("admin", "editor", "watcher")
print(user_roles)

# Пример с отображением длинны len для tuple

user_roles = ("admin", "editor", "watcher")
print(len(user_roles))

# Пример проведения итерации по Tuple вывод массива в каждой строке

user_roles = ("admin", "editor", "watcher")
for role in user_roles:
    print(role)

# Пример вхождения значения в tuple результатом которого будет True или False

user_roles = ("admin", "editor", "watcher")
print("admin" in user_roles)
print("writter" in user_roles)

# Пример с отображением индексов у tuple

user_roles = ("admin", "editor", "watcher")
print(user_roles[1])  # Будет выведен editor

# Пример распаковки кортежа в котором количество переменных должно быть равно количеству элементов в tuple

user_roles = ("admin", "editor", "watcher")
role_1, role_2, role_3 = user_roles  # Пример присваивания переменных в каждой переменной лежит елемент из кортежа
print(role_1)
print(role_2)
print(role_3)

# Пример пропуска переменной

user_roles = ("admin", "editor", "watcher")
role_1, role_2, _ = user_roles  # Пример присваивания переменных и пропуска при помощи символа _
print(role_1)
print(role_2)
