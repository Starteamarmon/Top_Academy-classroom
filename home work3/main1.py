# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы

class Device:
    def __init__(self, type: str, brand: str, name: str, consumption: int):
        self._type: str = type
        self._brand: str = brand
        self._name: str = name
        self._consumption: int = consumption

class Blender(Device):
    def __init__(self, type: str, brand: str, name: str, consumption: int, speed: int):
        super().__init__(type, brand, name, consumption)
        self._speed: int = speed

    def __str__(self):
        return f'Тип устройства: {self._type}\nМарка: {self._brand}\nМодель: {self._name}\nПотребляемая мощность: {self._consumption} Вт\nКоличество скоростей: {self._speed}'
    
    def power_on_speed1(self):
        print('Вж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж-ж')
    
    def power_on_speed2(self):
        print('Вз-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И-И')

class MeatGrinder(Device):
    def __init__(self, type: str, brand: str, name: str, consumption: int, productivity: int):
        super().__init__(type, brand, name, consumption)
        self._productivity: int = productivity

    def __str__(self):
        return f'Тип устройства: {self._type}\nМарка: {self._brand}\nМодель: {self._name}\nПотребляемая мощность {self._consumption} Вт\nПроизводительность {self._productivity} кг/мин.'


a = Blender("Бледнер","Toshiba",'HelperHomy',700,2)
print(a)
a.power_on_speed1()
a.power_on_speed2()
print(MeatGrinder('мясорубка',"RED",'HV8 ME687832',800,4.5))