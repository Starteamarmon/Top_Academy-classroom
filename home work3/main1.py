# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы

# class Device:
#     def __init__(self, type: str, brand: str, name: str, consumption: int):
#         self._type: str = type
#         self._brand: str = brand
#         self._name: str = name
#         self._consumption: int = consumption

# class Blender(Device):
#     def __init__(self, type: str, brand: str, name: str, consumption: int, speed: int):
#         super().__init__(type, brand, name, consumption)
#         self._speed: int = speed

#     def __str__(self):
#         return f'Тип устройства: {self._type}\nМарка: {self._brand}\nМодель: {self._name}\nПотребляемая мощность: {self._consumption} Вт\nКоличество скоростей: {self._speed}'
    
#     def power_on_speed1(self):
#         print('Вж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж')
    
#     def power_on_speed2(self):
#         print('Вз-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И')

# class MeatGrinder(Device):
#     def __init__(self, type: str, brand: str, name: str, consumption: int, productivity: int):
#         super().__init__(type, brand, name, consumption)
#         self._productivity: int = productivity

#     def __str__(self):
#         return f'Тип устройства: {self._type}\nМарка: {self._brand}\nМодель: {self._name}\nПотребляемая мощность {self._consumption} Вт\nПроизводительность {self._productivity} кг/мин.'


# a = Blender("Бледнер","Toshiba",'HelperHomy',700,2)
# print(a)
# a.power_on_speed1()
# a.power_on_speed2()
# print(MeatGrinder('мясорубка',"RED",'HV8 ME687832',800,4.5))





# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы


# class Ship:
#     def __init__(self,displacement: int):
#         self._displacement: int = displacement

# class Cruiser(Ship):
#     def __init__(self, displacement: int, armor_thickness: int):
#         super().__init__(displacement)
#         self._armor_thickness: int = armor_thickness
#     def __str__(self):
#         return f'Водоизмещение ровняется {self._displacement} тысяч тонн, а толщина брони составляет {self._armor_thickness} мм'

# class Destroyer(Ship):
#     def __init__(self, displacement: int, damage_range: int):
#         super().__init__(displacement)
#         self._damage_range: int = damage_range
#     def __str__(self):
#         return f'Водоизмещение состовляетет {self._displacement} тысяч тонн, а дальность поражения {self._damage_range} морских миль'

# class Frigate(Ship):
#     def __init__(self, displacement: int, speed: int):
#         super().__init__(displacement)
#         self._speed: int = speed
    
#     def __str__(self):
#         return f'Водоизмещение {self._displacement} тысяч тонн, а скорость {self._speed} узлов'


# stormy = Cruiser(11,127)
# print(stormy)
# daring = Destroyer(9,600)
# print(daring)




# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей. 


class Money:
    def __init__(self, deutsche_mark: int, pfennig: int):
        self._deutsche_mark: int = deutsche_mark
        self._pfennig: int = pfennig
        

    def __str__(self):
        while self._pfennig > 100:
            self._pfennig -= 100
            self._deutsche_mark += 1
        return f'{self._deutsche_mark} дойчмарок и {self._pfennig} пфенингов'
    
print(Money(10,427))