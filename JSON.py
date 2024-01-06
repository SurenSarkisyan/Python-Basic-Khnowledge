# JSON - Java Script Objective Notation, текстовый формат обмена данными.
# Применяется в веб приложениях как для обмена данными между клиентами
# (фронтенд или мобильное приложение) и сервером, так и между серверами, формат считается независимым от языка и может
# использоваться с любым языком программирования

# JSON - делает следующее он берет какую то структуру данных и упаковывает ее в одну строку
# по определенным внутренним правилам, делает это в одном языке и потом по таким же правилам распаковывает в структуру данных
# в другом языке

# Пример упаковки json с методом dumps

import json

book= {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "978-0451524935",
    "uuid": "a0eebc09-9c0b-4ef8-bb6d-6bb9bd380a11"
}

json_string = json.dumps(book)
print(type(json_string))
print(json_string)


# Пример распаковки json с методом loads

json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc09-9c0b-4ef8-bb6d-6bb9bd380a11"}'

book = json.loads(json_string)
print(type(book))
print(book)
