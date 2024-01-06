# Списочные включения Complihations

# List Complihations

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

# Пример оптимизации вышестоящего кода с использованием Complihantions

squares = [x ** 2 for x in range(10)]
print(squares)

# Пример списка четных квадратов чисел

even_square = []
for x in range(10):
    if x % 2 == 0:
        even_square.append(x ** 2)
print(even_square)

# Пример оптимизации вышестоящего кода с использованием Complihantions

even_square = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_square)

# Пример замены каждого четного числа словом even а нечетного odd

labelled_numbers = []
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")

print(labelled_numbers)

# Пример оптимизации вышестоящего кода с использованием Complihantions

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labelled_numbers)

# Пример создания словаря через List Complihantions

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)

# Пример транспонирования матрицы с помощью List Complihantions, матрица это двумерный массив чисел у которого есть
# строки и столбцы
# транспонирование - это операция над матрицей когда ее строки становятся столбцами с тем же номером а столбцы ствновятся строками

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transponse_matrix = []

for i in range(len(matrix)):
    transponse_row = []
    for row in matrix:
        transponse_row.append(row[i])
    transponse_matrix.append(transponse_row)

print(transponse_matrix)

# Пример оптимизации вышестоящего кода с использованием Complihantions

transponse_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transponse_matrix)


