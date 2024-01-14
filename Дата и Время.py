# Дата и Время, Date - Time

# Модуль datetime


# Пример работы с модулем

import datetime

utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)

current_time = datetime.datetime.now()
print(current_time.isoformat())  # получение данных методом isoformat

current_time = datetime.datetime.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.minute)
print(current_time.hour)

# Пример инициализации datetime обьекта

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=30)
print(some_datetime)

# Пример работы с датой

current_date = datetime.date.today()
print(current_date)

# Получение объекта времени из метода datetime

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
print(current_date)

# Пример получения времени которое было ровно 24 часа назад

current_datetime = datetime.datetime.now()
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)

# Пример вывода datetime в хьюманридбл формате strftime

current_datetime = datetime.datetime.now()

print(current_datetime.strftime("%A, %d, %B, %Y"))

# Пример преобразования даты в isoformat в datetime обьект

isoformat = "2023-08-07T20:15:30.123456"

my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime))
print(my_datetime)
