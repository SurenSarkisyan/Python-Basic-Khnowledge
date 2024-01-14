# Классы - как часть ООП, контр интуитивный метод абстракции
# ООП-  методология или стиль программирования на основе описания типов/моделей предметной области и их взаимодействия,
# представленных порождением из прототипов или как экземпляры классов, которые образуют иерархию наследования

# Экземпляр и его отличие от класса
# Класс - как чертеж дома аналогия из жизни
# Инстанс - конкретный дом, то-есть по одному чертежу может быть построено множество различных домов
# List - это класс
# my_list = list() - это экземпляр
# Синонимы слова экземпляр - Инстанс, Обьект


my_string = "Hello World!" #  my_string = Hello World - экземпляр класса
print(type(my_string))
print(type(str))  # str - это класс из стандартной библиотеки

# Пример создания класса

class MyClass:
    pass

my_class = MyClass()

print(type(MyClass))
print(type(my_class))

# Пример написания собственного класса
# __init__ - метод инициализации класса - так называемый дандер (Double Underscore) метод, дандер метод это метод в синтаксисе которого есть два подчеркивания
# Дандер методы так же называют магическими методами - они определяют как будет вести себя обьект класса с разными конструкциями языка
# Функция __init__ - работает при создании экземпляра конкретного класса


class Ork:
    def __init__(self, level: int) -> None:  # self - экземпляр класса который мы передаем в метод класса
        self.level = level
        self.health_point = 100 * level
        self.attack_power = 100 * level

    def attack(self,):
        print(f"Ork attacks with {self.attack_power} power")

ork = Ork(level=2)
print(ork.level)
print(ork.health_point)  # атрибут, свойство класса
print(ork.attack_power)
ork.attack()

# Пример манипуляции атрибутами экземпляра класса +=1 level

class Ork:
    def __init__(self, level: int) -> None:  # self - экземпляр класса который мы передаем в метод класса
        self.level = level
        self.health_point = 100 * level
        self.attack_power = 100 * level

    def attack(self,):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self):
        return f"Ork level: {self.level} , hp: {self.health_point}"

ork = Ork(level=2)


print(ork)
























