# Библиотеки Requests и запросы к API
# API - интерфейс для взаимодействия программ между собой
import time

# Пример запроса к другому ресурсу у которого есть свой персональный API
# Вызов из своей программы другую программу через HTTP запрос

# Пример в котором узнаем стоимость биткоина на Бинансе,так как у Бинанса есть открытое API с документацией

import requests

url = "https://api.binance.com/api/v3/ticker/price"

responce = requests.get(url, params={"symbol": "BTCUSDT"})

price_object = responce.json()

price = float(price_object["price"])

print(price)

# Пример в котором код каждую секунду ходит к API Бинанса узнает цену на биткоин и добавляет ее в список
# Модуль библиотеки time

import requests

url = "https://api.binance.com/api/v3/ticker/price"

bitcoin_prices = []
for i in range(30):
    responce = requests.get(url, params={"symbol": "BTCUSDT"})
    price = float(responce.json()["price"])
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))










