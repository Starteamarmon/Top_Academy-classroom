# Задание 1
# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

import time

def rtrn0_100(zero: int, one_hundred: int):
    start = time.time()
    for i in range(zero+1,one_hundred+1):
        print(i)
    end = time.time() - start
    print(f'на вычисление простых чисел ушло {end} секунд')

rtrn0_100(0,100)


# Задание 2
# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.


# Задание 3
# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные.
# Используя механизм декораторов, решите вопрос
# отчетности для организаций.

class Organization:
    def __init__(self,report:str):
        self._report: str = report
    
    def txt(self):
        txt: str = '.txt'
        result = self._report+txt
        return result
    
    def doc(self):
        doc: str = '.doc'
        result = self._report+doc
        return result
    
    def pdf(self):
        pdf: str = '.pdf'
        result = self._report+pdf
        return result
    
a = Organization('Отчёт за май')
print(a.txt())
print(a.doc())
print(a.pdf())