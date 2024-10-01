class Passport:
    def __init__(self, name: str, age: int, city: str, country: str):
        self._name: str = name
        self._age: int = age
        self._city: str = city
        self._country: str = country
    

    def __str__(self):
        return f"Имя: {self._name}, Возраст: {self._age}, Город: {self._city}, Страна: {self._country}"
    
p1 = Passport("Александр", 28,"Красноярск","Россия")
print(p1)

class ForeignPassport(Passport):
    def __init__(self,name: str, age: int, city: str, country: str, pass_number: int, visa: list):
        super().__init__(name, age, city, country)
        self._pass_number: int = pass_number
        self._visa: list[str] = visa
    
    def set_visa(self, value: list[str]):
        self._visa = value

    def app_visa(self, value: str):
        self._visa.append(value)

    def __str__(self):
        return f"Имя: {self._name}, Возраст: {self._age}, Город: {self._city}, Страна: {self._country}, Номер заграна: {self._pass_number}, список виз: {self._visa}"
    
fp = ForeignPassport("XAEn-12",12,"Вашингтон","США",2987494,["Россия","Мадагаскар","уругвай"])
print(fp)
fp.set_visa(["Япония"])
print(fp)
fp.app_visa("Аргентина")
print(fp)