
# Comments - Наследование, Инкапсуляция, Полиморфизм. - Основные концепции ООП

# Наследование - это одна из важнейших концепций ООП и она гласит нам о том что у любого класса может быть класс
# наследник что будет наследовать абсолютно все от класса родителя или другими словами супер класса, То есть класс
# наследник это класс который строиться на основе какого либо родительского класса и соответственно этот класс
# наследник он наследует такие вещи как методы, поля, а так же различные конструкторы.

# Таким образом Наследование - это особенность ООП за счет которой мы можем создать некий
# дополнительный класс и в этом же классе мы укажем что мы наследуем все от Родителя или же Супер класса


# Example 1 Создание Супер класса и класса наследника


class Building:                                       # Супер Класс - общие характеристики year и city,так же можно добавить много различных характеристик в класс
    year = None
    city = None

    def __init__(self, year, city):                   # Конструктор для принятия двух параметров self.year self.city
        self.year = year
        self.city = city

    def get_info(self):                               # def get_info(self): - в данном примере метод который будет выностить информацию по опредиленной постройке
        print("Year:", self.year, ". City:", self.city)

class School(Building):                               # Класс School - наследовает все характеристики класса Building
    students = 0                                      # pass - говорит что ничего в этом классе нет

    def __init__(self,students, year, city):
        super(School, self).__init__(year,city)       # super - функция вызова Супер Класса (Родительского класса, в данном примере School)
        self.students = students
        #self.year = year
        #self.city = city


class House(School):                                   # Пример что класс House наследовает все от класса School  и School в свою очередь все от Buiding
    pass                                               # В Python нельзя прописывать два класса родителя это неверно
                                                       # тоесть множественное наследование клаасов запрещено
                                                       # но классы наследники могут иметь свои классы наследников

class Shop(Building):
    pass

school = School(100, 2000, "Kiev")
school.get_info()                                      # Метод вывода информации (все обработает корректно на основе наследования данных с метода Building)

#house = House(2000, "Kiev")


shop = Shop(2000, "Kiev")


# Example 2 Полиморфизм - Возможность переписывать методы, что обь явлены в классе родителе
# мы их можем переписать в классах наследниках


class Building:                             # Супер Класс - общие характеристики year и city,так же можно добавить
                                            # много различных характеристик в класс
    year = None
    city = None

    def __init__(self, year, city):         # Конструктор для принятия двух параметров self.year self.city
        self.year = year
        self.city = city

    def get_info(self):                     # def get_info(self): - в данном примере метод который будет выностить информацию по опредиленной постройке
        print("Year:", self.year, ". City:", self.city)

class School(Building):                               # Класс School - наследовает все характеристики класса Building
    students = 0                                      # pass - говорит что ничего в этом классе нет

    def __init__(self, students, year, city):
        super(School, self).__init__(year, city)       # super - функция вызова Супер Класса (Родительского класса, в данном примере School)
        self.students = students
        #self.year = year
        #self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)    # Тоже самое что и - super().get_info()
        #super().get_info()                                # Обращение к родительскому классу
        print("students", self.students)

class House(School):                                   # Пример что класс House наследовает все от класса School  и School в свою очередь все от Buiding
    pass                                               # В Python нельзя прописывать два класса родителя это неверно
                                                       # тоесть множественное наследование клаасов запрещено
                                                       # но классы наследники могут иметь свои классы наследников
class Shop(Building):
    pass


school = School(100, 2000, "Kiev")
school.get_info()                                      # Метод вывода информации (все обработает корректно на основе наследования данных с метода Building)

#house = House(2000, "Kiev")

shop = Shop(2000, "Kiev")
shop.get_info()


# Example 2 Инкапсуляция -  Концепция гласит о том что любые поля что существуют в каком либо классе они должны быть
# защищенными, тоесть инкапсуляция это по сути защита данных, доступ к полям может быть только к функциям и методам внутри самого класса
# В языке Python инкапсуляция не реализована корректно!


#class Building:                      # Супер Класс - общие характеристики year и city,так же можно добавить
                                     # много различных характеристик в класс
#    year = None
#    city = None


#def __init__(self, year, city):      # Конструктор для принятия двух параметров self.year self.city
#    self.year = year
#    self.city = city


#def get_info(
#        self):                       # def get_info(self): - в данном примере метод который будет выностить информацию по опредиленной постройке
#    print("Year:", self.year, ". City:", self.city)


#class School(Building):              # Класс School - наследовает все характеристики класса Building
#    students = 0                     # pass - говорит что ничего в этом классе нет

#    def __init__(self, students, year, city):
#        super(School, self).__init__(year, city)                  # super - функция вызова Супер Класса (Родительского класса, в данном примере School)
#        self.students = students
        # self.year = year
        # self.city = city

#    def get_info(self):
#        print("Year:", self.year, ". City:", self.city)     # Тоже самое что и - super().get_info()
        # super().get_info()                                # Обращение к родительскому классу
#        print("students", self.students)


#class House(School):                     # Пример что класс House наследовает все от класса School  и School в свою очередь все от Buiding
#    pass                                 # В Python нельзя прописывать два класса родителя это неверно
                                         # тоесть множественное наследование клаасов запрещено
                                         # но классы наследники могут иметь свои классы наследников

#class Shop(Building):
#    pass


#school = School(100, 2000, "Kiev")
#school.get_info()                        # Метод вывода информации (все обработает корректно на основе наследования данных с метода Building)

# house = House(2000, "Kiev")

#shop = Shop(2000, "Kiev")
#shop.get_info()























































