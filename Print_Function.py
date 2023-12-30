
# Print - Функция, которая помогает ориентироваться в коде для вывода переменных и строковых данных в терминал.


print("Hello World!")  # Print - Функция, которая помогает ориентироваться в коде для вывода переменных и строковых данных в терминал.


print("Hello", "World")  # В функцию принт можно передавать сразу несколько строковых значений через запятую, в терминале они будут разделены пробелом.


print("Hello", "World", sep=", ") # Если мы хотим разделить их каким то другим символом то мы используем аргумент sep (separator) и между словами Hello World! будет видиться запятая и пробел.


print("Hello", "World") # Исполнение функции Print в разных строках будет означать что значения будут так же выведены в разных строках


print("Hello", "World", end=" ")
print("Hello", "World", "Again")  # Данный аргумент end=" " - выведет две функции Print написаные на разных строках в одну строку, необходимо учесть что код в Python исполняется строка за строкой.
