# Обработка исключений try except

# Пример написания функции которое находит среднее значение и обрабатывает ошибку при делении на ноль

def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

try:
    find_average(numbers=[]) # В случае если бы массив был не пустой он бы сработал на вычисление, а так мы обработали ошибку далее по коду
except ZeroDivisionError:  # После ключевого слова except мы перечисляем ошибки которые могут потенциально возникнуть
    print("The list is empty")

print("We are here")

# Пример того что будет если выключить интернет и исполнить код

import requests

try:
    responce = requests.get(
        url = "https://api.binance.com/api/v3/ticker/price",
        params={"symbol": "BTCUSDT"}
    )
    bitcoin_prices = responce.json()["price"]
    bitcoin_prices = float(bitcoin_prices)
    print(bitcoin_prices)
except requests.exceptions.ConnectionError as error:  # Пример вывода информации ошибок которые передаются в Python
    print(f"Somthing goes wrong:  {error}")

