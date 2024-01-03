# Область видимости переменных

# Пример вызова функции в блоке кода, за границами блока кода функции код не рабоатет

def my_function():
    local_var = "I'm local variable"
    print(local_var)

my_function()

# Пример с использованием цикла

for i in range(10):
    print(i)

print(i) # Данный принт будет отображать последний индекс в range то-есть 9 будет выведено дважды

# Пример в котором переменная в теле функции будет первичной при присвоении а переменная вне тела функции будет отображена принтом
# Данные переменные вне тела функции не желательны для обьявления, используется только для констант

variable = "I'm a variable out of scope"

def my_function():
    variable = ("I'm a variable out of scope yes")
    print(variable)
my_function()
print(variable)

# Пример использования констант в функции для вычисления комфортной температуры и температуры в комнате например

COMFORTABLE_TEMPERATURE = 25

def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature

print(get_diff_from_comfortable_temperature(temperature=20))

# Пример изменения глобальной переменной в функции - абсолютное зло
# Вне скоупа функций нужно использовать только КОНСТАНТЫ
global_var = "I'm global variable"

def my_function():
    global global_var
    global_var = "I defined inside the scope of my function"

print(global_var)
my_function()
print(global_var)


# Пример функции в которой для персонажа в игре будет увеличен уровень или уровень оставить тем же
# Использование Констант в коде
DEFAULT_LEVEL_EXPERIENCE = 200

def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up

print(is_leveled_up(current_experience=150, gained_experience=60))  # TRUE
print(is_leveled_up(current_experience=10, gained_experience=60))   # False













