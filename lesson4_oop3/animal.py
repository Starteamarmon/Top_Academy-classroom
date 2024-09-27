from abc import abstractmethod

class Animal:
    def __init__(self,name: str):
        self._name: str = name
    def __str__(self):
        return f"{self._name}"
    
    @abstractmethod
    def sound(self):
        raise Exception("напиши звук")
    
    @abstractmethod
    def type(self):
        raise Exception("Напиши тип")
    
    def __str__(self) -> str:
        return f"{self._name}"

class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def sound(self):
        print('Гаф')

    def type(self):
        print('Собака')


dog = Dog("шарик")
dog.type()