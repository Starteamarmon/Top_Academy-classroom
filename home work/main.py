# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.


# fail_1:str = ''
# fail_2:str = ''
# with open('home work/input.txt', encoding='utf-8') as f:
#     fail_1 = f.read()

# with open('home work/output.txt', encoding='utf-8') as f:
#     fail_2 = f.read()

# arr_1 = fail_1.split('\n')
# arr_2 = fail_2.split('\n')
# for string in arr_1:
#     if string not in arr_2:
#         print(string)
# for string in arr_2:
#     if string not in arr_1:
#         print(string)




#Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# Количество символов;
# Количество строк;
# Количество гласных букв;
# Количество согласных букв;
# Количество цифр.



# fail:str = ''
# with open('home work/input.txt', encoding='utf-8') as f:
#     fail = f.read()

# fail_str: list = fail.split('\n')
# count_symbol = 0
# count_string = len(fail_str)
# count_v_letter = 0
# count_c_letter = 0
# count_num = 0

# for i in fail:
#     count_symbol += 1

# for i in fail:
#     i = str(i.upper())
#     vowels = 'УЕЫАОЭИЮ'
#     consonant = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
#     num = '1234567890'
#     if i in vowels:
#         count_v_letter += 1
#     elif i in consonant:
#         count_c_letter += 1
#     elif i in num:
#         count_num += 1

# result: str = f'Количество символов {count_symbol}\nКоличество строк {count_string}\nКоличество глассных букв {count_v_letter}\nКоличество согласных букв {count_c_letter}\nКоличество цифр {count_num}'
# print(result)

# with open('home work/output.txt','w',encoding='utf-8') as f:
#     f.write(result)



# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.


# fail:str = ''

# with open('home work/input.txt',encoding='utf-8') as f:
#     fail = f.read()

# fail_arr: list = fail.split('\n')
# fail_arr.remove(fail_arr[-1])
# print(fail_arr)
# fail_arr = ('\n').join(fail_arr)
# with open('home work/output.txt','w',encoding='utf-8') as f:
#     f.write(fail_arr)



# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.


# fail: str = ''

# with open('home work/input.txt', encoding='utf-8') as f:
#     fail = f.read()

# fail_arr = fail.split('\n')
# max_len = 0
# for i in fail_arr:
#     if len(i) > max_len:
#         max_len = len(i)
# print(max_len)


# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

# file: str = ''
# with open('home work/input.txt', encoding='utf-8') as f:
#     file = f.read()
# file = file.split()
# search = input("какой слово искать?: ")
# count = 0
# for i in file:
#     if i.upper() == search.upper():
#         count += 1
# print(f'слово {search}, встречается в тексте {count} раз')


# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

file: str = ''
with open('home work/input.txt', encoding='utf-8') as f:
    file = f.read()

search = input("какое слово заменить?: ")
edit_letter: str = input("На какое?: ")
file = file.replace(search,edit_letter)
print(file)

with open('home work/input.txt', 'w', encoding='utf-8') as f:
    f.write(file)