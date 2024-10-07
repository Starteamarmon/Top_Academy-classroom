# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:

# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение 
# пользователю об этом, без добавления числа).okay

# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления). 
# !!!может я дурак? если у нас числа не повторяются то какие там всё вхождения? 
# просто удалить число из списка?okay


# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца).okay

# 4. Проверить есть ли значение в списке.okay

# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения).okay

# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

class NumberList:
    def __init__(self,arr: list):
        self._u_l: list = arr


    def __str__(self) -> str:
        return f'{self._u_l}'
    

    def appN(self,num):
        if num not in self._u_l:
            self._u_l.append(num)
        else:
            print(f'Число {num} уже есть в списке')
    

    def delete(self,num):
        if num not in self._u_l:
            print(f'числа {num} нет в списке')
        else:
            menu = input(f'1. Очистить спсок от {num} | 2. Удалить {num} один раз: ')
            if menu == '1':
                while num in self._u_l:
                    for i in self._u_l:   
                        if i == num:
                            self._u_l.remove(i)     
            elif menu == '2':
                for i in self._u_l:
                    if i == num:
                        self._u_l.remove(i)
            else:
                print(f'ты чё дурак?! смотри в пунты меню какая к чёрту {menu}?!')

    def show(self):
        menu = input('1 вывести список по порядку | 2 вывести список наоборот: ')
        rev_arr = []
        arr = []
        if menu == '1':
            print(self)
        elif menu == '2':
            for i in self._u_l:
                arr.append(i)
            count = len(arr)
            while len(rev_arr) != len(arr):
                rev_arr.append(arr[count-1])
                count -= 1
            print(rev_arr)
        else:
                print(f'ты чё дурак?! смотри в пунты меню какая к чёрту {menu}?!')


    def search(self,num):
        if num not in self._u_l:
            print(f'числа {num} нет в списке')
        elif num in self._u_l:
            print(f'число {num} есть в списке')


    def edit(self):
        num = input('какое число заменить?: ')
        num_edit = input(f'На какое значение заменить {num}: ')
        if num not in self._u_l:
            print(f'числа {num} нет в списке')
        elif num_edit in self._u_l:
            print(f'число {num_edit} есть в списке')
            num_edit = input('введите другое число для замены: ')
        else:
            menu = input(f'1. Заменить все числа {num} в списке | 2. Заменить первое число {num} : ')
            if menu == '1':
                count = 0
                for i in self._u_l:
                    if i == num:
                        self._u_l[count] = num_edit
                    count += 1
            elif menu == '2':
                count = 0
                for i in self._u_l:
                    if i == num:
                        self._u_l[count] = num_edit
                        break
                    count += 1
            else:
                print(f'ты чё дурак?! смотри в пунты меню какая к чёрту {menu}?!')


user_array = input('Введите числа через запятую(не больше 10ти чисел): ')
user_array = user_array.split(',')
if len(user_array) > 10:
        print('\nвы ввели слишком многочисел\n')
while len(user_array) > 10:
    user_array = input('Введите числа через запятую(не больше 10ти чисел): ')
    user_array = user_array.split(',')
    if len(user_array) > 10:
        print('\nВы ввели слишком многочисел\n')
a = NumberList(user_array)
print(a)
print('\n1. Добавить новое число в список')
print('2. Удалить указанное число из списка')
print('3. Показать содержимое списка')
print('4. Проверить есть ли число в списке')
print('5. Заменить значение в списке')
print('6. Завершить\n')
menu = input('Выберете пункт меню: ')

while menu != '6':
    if menu == '1':
        if len(user_array) >= 10:
            print('\nВ вашем списке не может быть больше 10 чисел')
            menu = input('\nВыберете пункт меню: ')
        else:
            num = input('Какое число добавить?: ')
            a.appN(num)
        menu = input('\nВыберете пункт меню: ')
    elif menu == '2':
        number = input('введите число:')
        a.delete(number)
        menu = input('\nВыберете пункт меню: ')
    elif menu == '3':
        a.show()
        menu = input('\nВыберете пункт меню: ')
    elif menu == '4':
        number = input('Какое число найти?: ')
        a.search(number)
        menu = input('\nВыберете пункт меню: ')
    elif menu == '5':
        a.edit()
        menu = input('\nВыберете пункт меню: ')
    else:
        print(f'ты чё дурак?! смотри в пунты меню какая к чёрту {menu}?!')
        menu = input('\nВыберете пункт меню: ')



# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.


class StoparikString:
    def __init__(self,arr: list):
        self._arr: list = arr
    
    def __str__(self):
        return f'{self._arr}'

    def app(self,strint):
        self._arr.append(strint)
    
    def push_out(self):
        print(f'Вытолкнута строка: {self._arr[-1]}')
        self._arr.remove(self._arr[-1])
    
    def counter(self):
        print(f'Строк в стеке: {len(self._arr)}')

    def empty(self):
        if len(self._arr) == 0:
            print('Стек пуст.')
        else:
            print('Стек не пуст.')

    def full(self):
        if len(self._arr) < 10:
            print('Стек не полон.')
        else:
            print('Стек полон.')
        
    def clean(self):
        while len(self._arr) != 0:
            self._arr.remove(self._arr[-1])

    def last(self):
        print(f'Крайняя строка: {self._arr[-1]}')

    def len(self):
        return len(self._arr)


print('1. Помещение строки в стек.')
print('2. Выталкивание строки из стека.')
print('3. Подсчет количества строк в стеке.')
print('4. Проверка пустой ли стек.')
print('5. Проверка полный ли стек.')
print('6. Очистка стека.')
print('7. Получение последнего значения.')
print('8. Выход.')

a = StoparikString([])
menu = input('Введите пункт меню: ')
while menu != '8':
    if menu == '1':
        string = input('Введите строку: ')
        if a.len() < 10:
            a.app(string)
        else:
            print('в стеке не может быть больше 10 строк')
        menu = input('Введите пункт меню: ')
    elif menu == '2':
        if a.len() > 0:
            a.push_out()
        else:
            print('нечего выталкивать...')
        menu = input('Введите пункт меню: ')
    elif menu == '3':
        print(a.counter())
        menu = input('Введите пункт меню: ')
    elif menu == '4':
        a.empty()
        menu = input('Введите пункт меню: ')
    elif menu == '5':
        a.full()
        menu = input('Введите пункт меню: ')
    elif menu == '6':
        a.clean()
        menu = input('Введите пункт меню: ')
    elif menu == '7':
        a.last()
        menu = input('Введите пункт меню: ')
    else:
        print('Такого пункта нет.')
        menu = input('Введите пункт меню: ')
