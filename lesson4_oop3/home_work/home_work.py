ofcTxt: str = ''
with open("lesson4_oop3/home_work/input.txt", encoding='utf-8') as f:
    ofcTxt = f.read()


class Office:
    def __init__(self,employees: list):
        employees: list = ofcTxt.split('\n')
        self._employees: list = employees

    def __str__(self):
        return f"{self._employees}"


    def app_employees(self, Empl):
        self._employees.append(f'{Empl}')


    def search(self,i):
        i = str(i)
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
            elif i in empl:
                print(empl)


    def editEmpl(self,i):
        i = str(i)
        count = 0
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
                self._employees[count] = input('введите данные сотрудника с изменениями: ')
            elif i in empl:
                print(empl)
                self._employees[count] = input('введите данные сотрудника с изменениями: ')
            count += 1


    def deleteEmpl(self,i):
        i = str(i)
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
                a = input('Удалить сотрудника? (да|нет): ')
                if a == "да":
                    self._employees.remove(empl)
            elif i in empl:
                print(empl)
                a = input('Удалить сотрудника? (да|нет): ')
                if a == "да":
                    self._employees.remove(empl)

    

    def load(self,ofcArr:list) -> list:
        for empl in self._employees:
            ofcArr.append(empl)
        return list(ofcArr)
    

class Empl:
    def __init__(self, name: str, age: int):
        self._name: str = name
        self._age: int = age

    
    def __str__(self):
        return f"{self._name}, {self._age}"

ofcArr = []
ofcTxt = Office([])
ofcTxt.app_employees(Empl("Березовскйи Александр Васильевич", 28))
ofcArr: list = ofcTxt.load(ofcArr)
ofcArr = ('\n').join(ofcArr)
with open("lesson4_oop3/home_work/input.txt", 'w', encoding='utf-8') as f:
    f.write(ofcArr)