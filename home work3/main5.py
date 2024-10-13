# Задача 5: Магические методы

# Описание: Создайте класс ComplexNumber, который будет представлять
#  комплексное число и реализуйте сложение и вычитание комплексных чисел,
#  используя магические методы add() и sub().

# Условия:

#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.

class ComplexNumber:
    def __init__(self,a:int,b:int) -> None:
        self._a: int = a
        self._b: int = b
   
    def __add__(self, Another):
        return ComplexNumber(Another._a + self._a, Another._b + self._b)
    
    def __sub__(self, Another):
        return ComplexNumber( self._a - Another._a, self._b - Another._b)
    
    def __str__(self) -> str:
        return f'{self._a}, {self._b}'
    

a = ComplexNumber(70,88)
b = ComplexNumber (30,12)
print(a + b)
print(a - b)


# Задача 6: Инкапсуляция

# Описание: Создайте класс Car, который содержит информацию о марке автомобиля,
#  максимальной скорости и текущей скорости. Инкапсулируйте переменные с текущей скоростью,
#  чтобы нельзя было напрямую её изменять.

# Условия:

#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя, чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.

class Car:
    def __init__(self,brand: str ,max_speed: int, current_speed: int = 0):
        self.__brand: str = brand
        self.__max_speed: int = max_speed
        self.__current_speed: int = current_speed
    
    def gas(self,gas):
        if gas + self.__current_speed < self.__max_speed:
            self.__current_speed = gas + self.__current_speed
            return self.__current_speed
        else:
            self.__current_speed = self.__max_speed
            return self.__current_speed
        
    def brake(self,brake):
        if self.__current_speed - brake > 0:
            self.__current_speed = self.__current_speed - brake
        else:
            self.__current_speed = 0
            return self.__current_speed
        
    def __str__(self):
        return f'Машина {self.__brand} двигается со скоростью {self.__current_speed} км/ч и имеет максимальную скорость {self.__max_speed}'
    

car = Car('Интегра', 220)
print(car)
car.gas(270)
print(car)
car.brake(30)
print(car)
car.brake(200)
print(car)


from abc import abstractmethod

# Задача 7: Абстрактные классы

# Описание: Создайте абстрактный класс Shape, который имеет абстрактный метод get_area().
#  Затем создайте классы Square и Triangle, которые наследуются от этого абстрактного класса
#  и реализуют свои версии метода get_area().

# Условия:

#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.

# Каждая из этих задач поможет вам лучше понять принципы ООП, такие как инкапсуляция, наследование,
#  полиморфизм и абстракция.

class Shape:

    @abstractmethod
    def get_area():
        raise f'нид мейк фанкшн'
    
class Square(Shape):
    def __init__(self,len_side):
        self._len_side: int = len_side

    def get_area(self):
        return self._len_side ** 2
    
    def __str__(self):
        return f'{self._len_side}'
    
class Triangle(Shape):
    def __init__(self,height,base):
        self._height: int = height
        self._base: int = base

    def get_area(self):
        return (self._height * self._base)/2
    
s = Square(4)
t = Triangle(3,2)
print(t.get_area(),s.get_area())