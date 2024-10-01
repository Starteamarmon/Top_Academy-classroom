# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод
# который при вызове возвращает количество созданных объектов класса «Дробь».



# class Fraction:
#     __count = 0

#     def __init__(self,dividend,divider):
#         self._dividend: int = dividend
#         self._divider: int = divider
#         Fraction.__count += 1


#     @staticmethod
#     def countFraction() -> int:
#         return Fraction.__count

# fr = Fraction(1,4)
# fr1 = Fraction(2,3)
# print(Fraction.countFraction())






# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт
# и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи
# возвращать это значение с помощью статического метода.



# class Сonverter:
#     count = 0
    
#     def __init__(self,num: int):
#         self._num: int = num

#     def __str__(self) -> str:
#         return f'{self._num}'
    
#     @staticmethod
#     def cel_in_far(num:int) -> int:
#         Сonverter.count += 1
#         return (num) * 1.8 + 32
    
#     @staticmethod
#     def far_in_cel(num:int) -> int:
#         Сonverter.count += 1
#         return (num - 32) / 1.8

#     @staticmethod
#     def countConv():
#         return f'{Сonverter.count}'


# print(Сonverter.cel_in_far(10))
# print(Сonverter.far_in_cel(50))
# print(Сonverter.countConv())






# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class Converter:
    @staticmethod
    def metr_in_foot(num:int):
        return num * 3.2808
    
    @staticmethod
    def foot_in_metr(num:int):
        return num / 3.2808
    
print(Converter.metr_in_foot(7))
print(Converter.foot_in_metr(1))