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

    def s(self):
        return f'Площать круга при радиусе в {self._side} равна {3.14 * self._side**2}'
    
class Tiangle(Figure):
    def __init__(self, side: int, side1: int):
        super().__init__(side)
        self._side1: int = side1
    
    def s(self):
        return f'Площадь треугольника при катетах {self._side} и {self._side1} равна {(self._side * self._side1)/2}'


class Rectangle(Figure):
    def __init__(self, side: int, side1: int):
        super().__init__(side)
        self._side1: int = side1

    def s(self):
        return f'Площадь прямоугольника при сторонах {self._side} и {self._side1} равна {self._side * self._side1}'


class Trapezoid(Figure):
    def __init__(self, side: int, side1: int, height: int):
        super().__init__(side)
        self._side1: int = side1
        self._height: int = height
    

    def s(self):
        return f'Площадь трапеции при параллельных сторонах {self._side}, {self._side1} и высоты {self._height} равна {((self._side + self._side1) / 2) * self._height}'

ronud = Round(3)
print(ronud.s())

tiangle = Tiangle(10,15)
print(tiangle.s())

rectangle = Rectangle(3,5)
print(rectangle.s())

trapezoid = Trapezoid(3,5,7)
print(trapezoid.s())