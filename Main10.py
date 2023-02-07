
# Comments Функции (def,lambda)

# Функции это что то типа подпрограмм - внутрь которой можно поместить
# код и  вдальнейшем запустить его выполнение, таким образом функции позволяют сократить нам код всей программы.

# Example 1

def test_func():               # def - пример создания функции
    pass                       # pass - при вызове функции ничего не произойдет

test_func()                    # Пример вызова функции

# Example 2

def test_func():                     # Внутри функции можно обрабатывать много разных строчек кода
    print("Hello", end="")
    print("!")                       # В данном примере будет вызов функции и вывод Hello! В случае
                                     # если я захочу вывести 3 раза к примеру test_func - то три раза будет обработан код который находится внутри test_func функции

# Example 3 Передача параметра в Функцию

def test_func(word):              # параметр word виден исключительно в пределах самой функции
    print(word, end="")
    print("!")

test_func("Hi")                   # В функцию можно передавать разные типы данных
test_func(5)
test_func(5.6)


# Example 4

def summa(a, b):                  # В функцию можно передавать много параметров
    result = a + b
    print("Result:", result)

summa(5.5, 7.5)
summa("H", "i")


# Example 5

def summa(a, b):
    result = a + b
   #return  a + b                   # Более лаконичный вариант - передаем парметры 5.5, 7.5 далее выполняется сложение результат возвращяется и записывается в переменную result и мы его выводим.
    return result                   # return - что будет возвращяться из функции, в итоге выполнили сложение, далее
                                    # сложение вернули из функции, далее то что вернулось поместили в переменную result и вывели на экран.
result = summa(5.5, 7.5)
print(result)
print(summa("H", "i"))


# Example 6

nums1 = [5, 7, 2, 9, 4]                        # Пример вывода нименьшего числа из списка

min_number = nums1[0]                          # нулевой элемент в списке будет минимальный
for element in nums1:
    if element < min_number:
        min_number = element

print(min_number)


# Example 7

nums1 = [5, 7, 2, 9, 4]                        # Пример вывода наименьших чисел из двух списко

min_number = nums1[0]
for element in nums1:
    if element < min_number:
        min_number = element

print(min_number)

nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]

min_number2 = nums2[0]
for element in nums2:
    if element < min_number2:
        min_number2 = element

print(min_number2)


# Example 8

def minimal(l):                                      # Аналог Example 7 только более локаничней, меньше строчек кода и удобнее.
    min_number = l[0]
    for element in l:
        if element < min_number:
            min_number = element

    print(min_number)

nums1 = [5, 7, 2, 9, 4]
minimal(nums1)

nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
minimal(nums2)


# Example 9

def minimal(l):
    min_number = l[0]
    for element in l:
        if element < min_number:
            min_number = element

    return min_number

nums1 = [5, 7, 2, 9, 4]
min_number1 = minimal(nums1)

nums2 = [5.4, 7.2, 1.9, 2.3, 2.1, 9.4, 4.2]
min_number2 = minimal(nums2)

if min_number1 < min_number2:
    print(min_number1)
else:
    print(min_number2)

# Example 10 Анонимные Функции lambda

func = lambda x, y: x * y                         # Любую лямбда функцию надо помещять в епременную которая в свою очередь будет анонимной функцией,
                                                  # удобно для небольших строчек кода, возможно проводить разные операции сложение умножение и так далее
result = func(5, 2)
print(result)


