# class Book:
#     def __init__(self,name: str,author: str,year: int):
#         self._name: str = name
#         self._author: str = author
#         self._yaer: int = year

#     def get_info(self):
#         print(f'Название книги: {self._name}\n Автор: {self._author}\n Год: {self._yaer}')

#     def yEdit(self):
#         self._yaer = input('Введите год с изменениями: ')

#     def __str__(self):
#         return f'{self._name,self._author,self._yaer}'


# class BankAccount:
#     def __init__(self,balance: int):
#         self._balance: int = balance

#     def deposit(self, money:int):
#         self._balance += money
    
#     def __str__(self):
#         return f'{self._balance}'
    
#     def withdraw(self, money:int):
#         if self._balance > 0:
#             self._balance -= money
#             if self._balance <= 0:
#                 self._balance = 0

#     def get_balance(self):
#         print(self)
        

# class Person:
#     def __init__(self,name:str ,age: int):
#         self._name: str = name
#         self._age: int = age


# class Student(Person):
#     def __init__(self, name: str, age: int,school: str,ball: float):
#         super().__init__(name, age)
#         self._school: str = school
#         self._ball: float = ball
    
#     def __str__(self):
#         return f'{self._name, self._age,self._school,self._ball}'
    
# import math

# class Rectangle:
#     def __init__(self, width: float, length: float):
#         self.__width: float = width
#         self.__length: float = length

#     def __str__(self):
#         return f'Длинна: {self.__length}\nШирина: {self.__width}'
    
#     def get_area(self):
#         return self.__length * self.__width
    
# class Cirle:
#     def __init__(self,r:float):
#         self._r: float = r
    
#     def __str__(self):
#         return f'Радиус: {self._r}'
    
#     def get_area(self):
#         return math.pi * ({self._r} * {self._r})


# class LibraryItem:
#     def __init__(self,ID: int,name: str, stat: bool = True):
#         self._id : int = ID
#         self._name : str = name
#         self._stat: bool = stat
    
#     def __str__(self):
#         return f'{self._id, self._name, self._stat}'

#     def vzyatb(self):
#         self._stat = False

#     def vernutb(self):
#         self._stat = True

# class Book(LibraryItem):
#     def __init__(self, ID: int, name: str, author: str, stat: bool = True):
#         super().__init__(ID, name, stat)
#         self._author: str = author

#     def __str__(self):
#         return f'{self._id, self._name,self._author, self._stat}'

# class Mabazine(LibraryItem):
#     def __init__(self, ID: int, name: str,public: str, stat: bool = True):
#         super().__init__(ID, name, stat)
#         self._public: str = public

# a = Book(194302,'1984','Толкиен')
# print(a)
# a.vzyatb()
# print(a)



# Описание: Разработайте систему управления видеотекой, где можно брать в аренду фильмы.
# В системе есть различные виды контента, такие как фильмы, сериалы и документальные фильмы.
# У каждого контента есть уникальный ID, название, режиссер, длительность и информация о доступности для аренды.
# Пользователи могут брать в аренду контент, а затем возвращать его.
# Также пользователи могут просматривать историю арендованных фильмов и оставлять оценки для контента


class Item:
    def __init__(self,id: int,name: str,drectir: str,duration: str,taken: bool = False):
            self._id: int = id
            self._name: str = name
            self._drectir: str = drectir
            self._duration: str = duration
            self._taken: bool = taken


    def __str__(self):
        return f'id: {self._id}, Название: {self._name}, Режисёр: {self._drectir}, длительность: {self._duration} мин, взят: {self._taken}'
    

class Movie(Item):
    def __init__(self, id: int, name: str, drectir: str, duration: str, taken: bool = False):
         super().__init__(id, name, drectir, duration, taken)


class Series(Item):
    def __init__(self, id: int, name: str, drectir: str, duration: str, taken: bool = False):
        super().__init__(id, name, drectir, duration, taken)


class Documentary(Item):
    def __init__(self, id: int, name: str, drectir: str, duration: str, taken: bool = False):
        super().__init__(id, name, drectir, duration, taken)


class VideoLibreri:
    def __init__(self):
	    self.__items: list[Item] = []
         
    def addi(self, item: Item):
        self.__items.append(item)

a = Series(1,'Хасбик VS Абдурозик',"Тамаев","1:20")
print(a)
VideoLibreri.addi(Movie(2,'Хасбик VS Абдурозик',"Тамаев","1:20"))