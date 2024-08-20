from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Intentar instanciar una ABC directamente resultará en un error
# animal = Animal("Generic Animal")

perro = Dog("Firulais")
print(perro.make_sound())  # Output: Woof!

gato = Cat("Mittens")
print(gato.make_sound())   # Output: Meow!