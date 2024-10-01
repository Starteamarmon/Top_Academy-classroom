# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


# class Auto:
#     def __init__(self,brand:str ,name:str ,year:int ,volume:float ,color:str ,price:int ):
#         self._name: str = name
#         self._year: int = year
#         self._brand: str = brand
#         self._volume: float = volume
#         self._color: str = color
#         self._price: int = price

#     def __str__(self):
#         return f'Название тачки {self._brand} {self._name}, она {self._year} года выпуска, объём её дрыгателя составлет\n{self._volume} литра, она окрашена в сексуальный {self._color} цвет, и все это превосходство стоит {self._price} рублей'
    
#     def editAuto(self):
#         print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
#         menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#         while menu != 7:
#             if menu == "1":
#                 self._brand = input('Введите название бренда с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '2':
#                 self._name = input('Введите название модели с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '3':
#                 self._volume:float = input('Введите объём двигателя с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '4':
#                 self._year = input('Введите год выпуска с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '5':
#                 self._color = input('Введите цвет авто с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu =='6':
#                 self._price = input('Введите стоимость авто с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '7':
#                 return (self)
#     def info(self):
#         print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
#         menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#         while menu != 7:
#             if menu == "1":
#                 print(self._brand)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '2':
#                 print(self._name)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '3':
#                 print(self._volume)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '4':
#                 print(self._year)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '5':
#                 print(self._color)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu =='6':
#                 print(self._price)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '7':
#                 return (self)
# integra = Auto('Honda','Integra',2001,2.0,'Белый',900000)
# integra.editAuto()
# print(integra)
# integra.info()





# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.



# class Book:
#     def __init__(self,name:str ,year:int ,publisher:str ,genre:str ,author:str ,price:int ):
#         self._name:str = name
#         self._year:int = year
#         self._publisher:str = publisher
#         self._genre:str = genre
#         self._author:str = author
#         self._price:int = price

    
#     def __str__(self):
#         return f'{self._name}\n{self._year} года выпуска\nАвтор: {self._author}\nЖанр: {self._genre}\nИздатель: {self._publisher}\nЦена: {self._price} р.'
    
    
#     def editBook(self):
#         print('1 Название\n2 Год выпуска\n3 Жанр\n4 Издатель\n5 Цена')
#         menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#         while menu != "6":
#             if menu == "1":
#                 self._name = input('Введите название книги с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '2':
#                 self._year = input('Введите год с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '3':
#                 self._genre:float = input('Введите жанр с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '4':
#                 self._publisher = input('Введите издателя с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '5':
#                 self._price = input('Введите стоимость с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '6':
#                 return (self)
            

#     def info(self):
#         print('1 Название\n2 Год выпуска\n3 Жанр\n4 Издатель\n5 Цена')
#         menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#         while menu != "6":
#             if menu == "1":
#                 print(self._name)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '2':
#                 print(self._year)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '3':
#                 print(self._genre)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '4':
#                 print(self._publisher)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '5':
#                 print(self._price)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '6':
#                 return (self)

# animal_farm = Book('Скотный двор',1945,'Harvill Secker',"Сатира","Джордж Оруэлл",102)
# print(animal_farm)
# animal_farm.editBook()
# animal_farm.info()
# print(animal_farm)





# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.



class Stadium:
    def __init__(self,name:str ,date:str ,country:str ,city:str ,capacity:int ):
        self._name:str = name
        self._date:str = date
        self._country:str = country
        self._city:str = city
        self._capacity:int = capacity


    def __str__(self):
        return f'Станион {self._name}\nДата открытия: {self._date}\nСтрана: {self._country}\nГород: {self._city}\nВместимость: {self._capacity}'


    def info(self):
        print('1 Имя\n2 дата\n3 Страна\n4 Город\n5 Вместимость\n6 Выход')
        menu = input('Какое поле вывести?: ')
        while menu != '6':
            if menu == '1':
                print(self._name)
                menu = input('Какое поле вывести?: ')
            elif menu == '2':
                print(self._date)
                menu = input('Какое поле вывести?: ')
            elif menu == '3':
                print(self._country)
                menu = input('Какое поле вывести?: ')
            elif menu == '4':
                print(self._city)
                menu = input('Какое поле вывести?: ')
            elif menu == '5':
                print(self._capacity)
                menu = input('Какое поле вывести?: ')
            elif menu == '6':
                return(self)
stadium = Stadium('Центральный','29.10.1967г','Россия','Красноярск',15000)#я тут подумал, вот метод ввода данных
print(stadium)#вот метод вывода данных

stadium.info()