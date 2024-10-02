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


# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.

# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.

# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника
# со сторонами, параллельными осям координат, и размерами этого прямоугольника.

# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур


from abc import abstractmethod

class Shape:
    def __init__(self, x:int, y:int):
        self._x:int = x
        self._y:int = y
    
    def show(self):
        return f'Координаты левого верхнего угла квадрата X: {self._x}  Y: {self._y} с длинной стороны {self._side_len}'

    def __str__(self):
        return f'Координаты левого верхнего угла квадрата X: {self._x}  Y: {self._y} с длинной стороны {self._side_len}'
    
    def save(self):
        string: str = ''
        result: str = str(self)
        with open('home work3/input.txt', encoding='utf-8') as f:
            string = f.read()
        if string == '':
            with open('home work3/input.txt','w',encoding='utf-8') as f:
                f.write(result)
        elif string != '':
            c: str = ''
            with open('home work3/input.txt', encoding='utf-8') as f:
                c = f.read()
            c = c.split('\n')
            c.append(result)
            with open('home work3/input.txt','w',encoding='utf-8') as f:
                f.write(('\n').join(c))

    def load(self):
        string: str = ''
        with open('home work3/input.txt', encoding='utf-8') as f:
            string = f.read()
        return string
    
class Square(Shape):
    def __init__(self, x:int, y:int, side_len:int):
        super().__init__(x, y)
        self._side_len: int = side_len

    
class Rectangle(Shape):
    def __init__(self, x: int, y: int, side_a: int, side_b: int):
        super().__init__(x, y)
        self._side_a: int = side_a
        self._side_b: int = side_b

    def show(self):
        return f'Координаты левого верхнего угла прямоугольника X: {self._x}  Y: {self._y} с длинной сторон {self._side_a} и {self._side_b}'
    
    def __str__(self):
        return f'Координаты левого верхнего угла прямоугольника X: {self._x}  Y: {self._y} с длинной сторон {self._side_a} и {self._side_b}'


class Circle(Shape):
    def __init__(self, x: int, y: int, r:int):
        super().__init__(x, y)
        self._r: int = r

    def show(self):
        return f'Координаты центра окружности X: {self._x}  Y: {self._y} с радиусом {self._r}'
    
    def __str__(self):
        return f'Координаты центра окружности X: {self._x}  Y: {self._y} с радиусом {self._r}'
    
class Ellipse(Shape):
    def __init__(self, x: int, y: int, side_a: int, side_b: int):
        super().__init__(x, y)
        self._side_a: int = side_a
        self._side_b: int = side_b

    def show(self):#хз я так вижу, если честно не понял элипс, на координатах левого верхнего угла прямоугольника его вертел
        return f'Координаты левого верхнего угла прямоугольника в который вписан элипс X: {self._x}  Y: {self._y} с длинной сторон {self._side_a} и {self._side_b} параллельных осям координат'
    
    def __str__(self):
        return f'Координаты левого верхнего угла прямоугольника в который вписан элипс X: {self._x}  Y: {self._y} с длинной сторон {self._side_a} и {self._side_b} параллельных осям координат'
    
a = Square(3,4,2)
print(a)
a.save()
print(a.load())
b = Rectangle(5,7,3,2)
b.save()
c = Circle(13,8,4)
c.save()