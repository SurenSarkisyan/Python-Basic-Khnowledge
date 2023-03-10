# Comments Циклы и операторы в Pyton (for, while)

# Циклы это конструкции которые позволяют выполнять код несколько раз подряд
# При чем колличество выполнений можно указать самостоятельно.
# for i in range(1, 6): - для переменной i будет задан диапазон отображения от 1 до 6
# print(i) - принт данных переменной i равный от 1 до 6
# range - параметр диапазона
# for - начало цикла
# for i in range(1, 6, 2): - так же можно добавить третий параметр двойку
# она означает  на сколько мы будем увеличивать переменную
# разница между for и while в формате записи
# for in - удобен для перебора строки или списка или создания диапазона
# while - удобен для прописи условия и дальнейшего выполнения цикла
# x = x + 1 - увеличить переменную на единицу


# Example 1

for i in range(1, 6 +1):
   print(i)

# Example 2

for x in 1,5,2,4,5:
    print(x ** 2)                             # пример возведения в степень содержимого переменной x


# Example 3

count = 0
word = "Hello world!"
for i in word:
    if i == "l":
        count  += 1

print("Count", count)                         # В данном примере мы каждый раз как находим символ
                                              # равный - l то count выводит значение искомого символа в числовом формате
                                              # так же если мы ищем L большую в данном примере то она не будет найдена так как зависит от регистра.

# Example 4

i = 5

while i <= 15:                                # весь цикл будет длиться до тех пор пока i будет меньше или равно 15
    print(i)                                  # итерация - однократное повторение тела цикла
    i += 2                                    # к этой же переменной увеличили вывод на 2 итого
                                              # 5, 7, 9 - так далее доконца цикла на числе 15
                                              # так же есть -=, *=, /=, //=, %=
# Example 5 infinity loop or cycle

i = 5

IsHasCar = True

while IsHasCar:
    print(i)
    i += 2

# Example 6

isHasCar = True

while isHasCar:
    if input("Enter Data ") == "Stop":
        isHasCar = False                       # В данном цикле ввод информации будет
                                               # до тех пор пока не будет введено ключевое слово Stop
                                               # тогда цикл завершится

# Example 7

for i in range(1,11):
    if i == 5:
        break                                  # Оператор завершения цикла в данном примере цикл завершится на 5
                                               # не смотря на то что диапазон от 1 до 11


    if i % 2 == 0:                             # % - деление, if i % 2 == 0: - при делении на 2 остаток равен 0
        continue                               # continnue - пропускает итерацию и возвращяется к началу цикла

    print(i)

# Example 8

found = None                                   # пустое значение переменной с дальнейшим присвоением значения

for i in "Hello":                              # данный цикл ищет символ l в слове Hello присвыивает значение истинно и обрывает цикл.
    if i == "m":
        found = True
        print("Yes correct")
        break                                  # break - обрывает цик
else:                                          # сработает в случае если значение False
    i = False
    print(i)

print(found)

# Example 9 # Вложенные циклы

x = int(input("Number: "))
while x > 0:
    y = x
    while y > 0:
        y -= 1
        print(y)
        x -= 1
        print("Stop")



