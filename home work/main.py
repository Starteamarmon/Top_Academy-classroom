# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.


fail_1:str = ''
fail_2:str = ''
with open('home work/input.txt', encoding='utf-8') as f:
    fail_1 = f.read()

with open('home work/output.txt', encoding='utf-8') as f:
    fail_2 = f.read()

arr_1 = fail_1.split('\n')
arr_2 = fail_2.split('\n')
for string in arr_1:
    if string not in arr_2:
        print(string)
for string in arr_2:
    if string not in arr_1:
        print(string)




