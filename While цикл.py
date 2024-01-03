# Цикл While Используется не так часто как цикл for так же отличия while от цикла for в том что цикл for повторяется
# определенное количество раз Чаще всего количество его итераций цикла for равно количеству элементов в коллекции
# которую мы перебираем Цикл while может повторяться неопределенное количество раз, это цикл который исполняется по
# условию, чаще всего можно применить для подсчета каких либо числовых условий.

# Пример каунтера - щетчика

counter = 1

while counter <=5:
    print(f"Counter is: {counter}")
    counter +=1

# Пример использования цикла while когда из листа нужно удалить элементы

my_list = [0, 1, 2, 3]
while my_list:
    element = my_list.pop()
    print(f"element: {element}")

print(my_list)

# Пример бесконечного цикла while infinity loop

while True:
    print("Infinity loop")
    break
# Пример бесконечного цикла while infinity loop

while True:
    answer = input("Enter a number: ")
    if answer == "quit":
        break
    print(f"You entered {answer}")


# Пример стратегии Мартингейла на примере броска монетки

import random  # Импорт библиотеки где можно взять нужную функцию

HEADS = "heads"  # Константа Орел
TAILS = "tails"  # Константа Решка
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES) # Возврат рандомного значения


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        print("======")
        steps_to_loose += 1
        current_funds -= current_bet
        print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()
    if flipped_coin_value == HEADS:
        win = current_bet * 2
        print(f"{win=}")
        current_funds += win
        current_bet = min_bet
    else:
        print("Loose")
        current_bet *= 2
        if current_bet > max_bet:
            current_bet = min_bet
        if current_bet > current_funds:
            current_bet = current_funds

    return steps_to_loose

print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))





































