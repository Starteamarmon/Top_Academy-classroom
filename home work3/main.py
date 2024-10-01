# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод
# который при вызове возвращает количество созданных объектов класса «Дробь».



class Fraction:
    __count = 0

    def __init__(self,dividend,divider):
        self._dividend: int = dividend
        self._divider: int = divider
        Fraction.__count += 1


    @staticmethod
    def countFraction() -> int:
        return Fraction.__count

fr = Fraction(1,4)
fr1 = Fraction(2,3)
print(Fraction.countFraction())