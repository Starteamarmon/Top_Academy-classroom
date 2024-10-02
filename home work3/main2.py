# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади. 


class Figure:
    def __init__(self, side: int):
        self._side: int = side


class Round(Figure):
    def __init__(self, side: int):
        super().__init__(side)

    def __int__(self) -> int:
        return int(3.14 * self._side**2)

    def __str__(self):
        return f'Площать круга при радиусе в {self._side} равна {3.14 * self._side**2}'
    
class Tiangle(Figure):
    def __init__(self, side: int, side1: int):
        super().__init__(side)
        self._side1: int = side1
    
    def __int__(self) -> int:
        return int((self._side * self._side1)/2)

    def __str__(self):
        return f'Площадь треугольника при катетах {self._side} и {self._side1} равна {(self._side * self._side1)/2}'


class Rectangle(Figure):
    def __init__(self, side: int, side1: int):
        super().__init__(side)
        self._side1: int = side1

    def __int__(self) -> int:
        return int(self._side * self._side1)

    def __str__(self):
        return f'Площадь прямоугольника при сторонах {self._side} и {self._side1} равна {self._side * self._side1}'


class Trapezoid(Figure):
    def __init__(self, side: int, side1: int, height: int):
        super().__init__(side)
        self._side1: int = side1
        self._height: int = height
    
    def __int__(self) -> int:
        return int(((self._side + self._side1) / 2) * self._height)

    def __str__(self):
        return f'Площадь трапеции при параллельных сторонах {self._side}, {self._side1} и высоты {self._height} равна {((self._side + self._side1) / 2) * self._height}'

ronud = Round(3)
print(ronud)
ronud1 = int(ronud)
print(ronud1)

tiangle = Tiangle(10,15)
print(tiangle)
tiangle1 = int(tiangle)
print(tiangle1)

rectangle = Rectangle(3,5)
print(rectangle)
rectangle1 = int(rectangle)
print(rectangle1)

trapezoid = Trapezoid(3,5,7)
print(trapezoid)
trapezoid1 = int(trapezoid)
print(trapezoid1)


# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).


