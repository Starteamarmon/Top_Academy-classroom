# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Auto:
    def __init__(self,brand:str ,name:str ,year:int ,volume:float ,color:str ,price:int ):
        self._name: str = name
        self._year: int = year
        self._brand: str = brand
        self._volume: float = volume
        self._color: str = color
        self._price: int = price

    def __str__(self):
        return f'Название тачки {self._brand} {self._name}, она {self._year} года выпуска, объём её дрыгателя составлет\n{self._volume} литра, она окрашена в сексуальный {self._color} цвет, и все это превосходство стоит {self._price} рублей'
    
    def editAuto(self):
        print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
        menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
        while menu != 7:
            if menu == "1":
                self._brand = input('Введите название бренда с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu == '2':
                self._name = input('Введите название модели с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu == '3':
                self._volume:float = input('Введите объём двигателя с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu == '4':
                self._year = input('Введите год выпуска с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu == '5':
                self._color = input('Введите цвет авто с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu =='6':
                self._price = input('Введите стоимость авто с изменениями: ')
                menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
            elif menu == '7':
                return (self)
    def info(self):
        print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
        menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
        while menu != 7:
            if menu == "1":
                print(self._brand)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu == '2':
                print(self._name)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu == '3':
                print(self._volume)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu == '4':
                print(self._year)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu == '5':
                print(self._color)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu =='6':
                print(self._price)
                menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
            elif menu == '7':
                return (self)
integra = Auto('Honda','Integra',2001,2.0,'Белый',900000)
integra.editAuto()
print(integra)
integra.info()