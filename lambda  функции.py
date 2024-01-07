# lambda Функции - механизм объявления функции очень коротко

# Пример lambda функции для оптимизации sort_by_len функции

def sort_by_len(element: str) -> int:
    return len(element)

sort_by_len_lambda = lambda element: len(element)
print(sort_by_len("banana"))
print(sort_by_len_lambda("banana"))

# Пример lambda функции

fruits = ["banana", "apple", "cherry", "date"]

sorted_fruits = sorted(fruits, key=lambda element: len(element))

print(sorted_fruits)

# Пример использования lambda функций с другими встроеными функциями Python, функция мах вернет один элемент из выборки и условия это
# самое длинное слово

fruits = ["banana", "apple", "cherry", "date"]

longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)






