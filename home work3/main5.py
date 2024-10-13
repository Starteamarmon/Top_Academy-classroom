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