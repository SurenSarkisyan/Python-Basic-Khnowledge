# Наследование - класс -> наследник -> содержит атрибуты и методы наследуемого класса
# Полиморфизм - возможность переопределить конструкцию языка для каждого класса
# Инкапсуляция - ограничение доступа к составляющим объекта

# Пример добавления общего класса Character для множества персонажей

class Character:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self):
        print(f"{self.character_name} attacks with {self.attack_power} power")

    def __str__(self) -> str:  # Управление тем что пользователь увидит в print
        return f"{self.character_name} level: {self.level} hp: {self.health_points}"

class Ork(Character):  # Наследование класса Character для Ork
    base_health_points = 100  # Определение атрибутов класса
    base_attack_power = 10
    character_name = "Ork"

ork_1 = Ork(level=1)
ork_1.attack()
print(ork_1)

class Elf(Character):  # Наследование класса Character для Elf
    base_health_points = 50  # Определение атрибутов класса
    base_attack_power = 15
    character_name = "Elf"

    def attack(self):  # Пример переопредиления метода наследуемого класса
        print("This method from class-inheritor")

elf_1 = Elf(level=2)
elf_1.attack()


# Пример воспроизведения боя персонажей

class Character:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        print(
            f"{self.character_name} attacks {target.character_name} ({target.health_points} health_point)"
            f"with {self.attack_power} power."
        )
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} hp has {target.health_points}")


    def is_alive(self) -> bool:
        return self.health_points > 0


    def __str__(self) -> str:  # Управление тем что пользователь увидит в print
        return f"{self.character_name} level: {self.level} hp: {self.health_points}"

class Ork(Character):  # Наследование класса Character для Ork
    base_health_points = 100  # Определение атрибутов класса
    base_attack_power = 10
    character_name = "Ork"

class Elf(Character):  # Наследование класса Character для Elf
    base_health_points = 50  # Определение атрибутов класса
    base_attack_power = 15
    character_name = "Elf"


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

        print(f"Character 1: {character_1} is_alive {character_1.is_alive()}")
        print(f"Character 2: {character_2} is_alive {character_2.is_alive()}")

ork_1 = Ork(level=1)
elf_1 = Elf(level=2)

fight(character_1=ork_1, character_2=elf_1)

# Пример работы с классами

class Ork:
    def __init__(self, level: int) -> None:  # self - экземпляр класса который мы передаем в метод класса
        self.level = level
        self.health_point = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self) -> str:  # Управление тем что пользователь увидит в print
        return f"Ork level: {self.level} , hp: {self.health_point}"

class Elf:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_point = 50 * level
        self.attack_power = 15 * level

    def attack(self):
        print(f"Elf attacks with {self.attack_power} power")

    def __str__(self) -> str:  # Управление тем что пользователь увидит в print
        return f"Elf level: {self.level} , hp: {self.health_point}"




