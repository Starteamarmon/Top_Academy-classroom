class Human:
    def __init__(self, name: str, age: int):
        self._name: str = Human._valid_name(name)
        self._age: int = Human._valid_date(age)

    @staticmethod
    def _valid_name(name:str) -> str:
        if name.isalpha():
            return name
        raise Exception  ('только буквы')


    @staticmethod
    def _valid_date(age: int) -> int:
        if 0 < age <= 100:
            return age
        raise Exception('возраст вне предела 0-100')
    

    def __str__(self):
        return f"{self._name}({self._age})"
    
# h1 = Human("Дюша",19)    
# print(h1)

class Builder(Human):
    def __init__(self, name, age, complain: str) -> str:
        super().__init__(name,age)
        self._complain: str = complain
    
    def __str__(self):
        return f"{self._name},{self._age} года. рабочий ноет: {self._complain}"

class Pilot(Human):
    def __init__(self, name, age, coolness: str) -> str:
        super().__init__(name,age)
        self._coolness: str = coolness

    def __str__(self):
        return f'{self._name},{self._age}, степень крутости: {self._coolness}'
    
class Sailor(Human):
    def __init__(self, name: str, age: int, disease: str):
        super().__init__(name, age)
        self._disease: str = disease

    def __str__(self):
        return f"Имя матросни: {self._name}, лет ему: {self._age}, заразность: {self._disease}"

# h2 = Builder('Лёха', 23, "Гвозди ржавые")
# h3 = Pilot('Андре', 36,"Очень крутой")
# h4 = Sailor('Глеб', 19, "Цинга")
# print(h2,h3)
# print(h4)



