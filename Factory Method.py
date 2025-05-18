from abc import ABC, abstractmethod
from symtable import Class


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Рычание"

class Monkey(Animal):
    def make_sound(self):
        return "Визг"

class Elefan(Animal):
    def make_sound(self):
        return "ДУдение"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElefanFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elefan()

lion_factory = LionFactory()
monkey_factory = MonkeyFactory()
elefan_factory = ElefanFactory()

lion = lion_factory.create_animal()
monkey = monkey_factory.create_animal()
elefan = elefan_factory.create_animal()

print(lion.make_sound())
print(monkey.make_sound())
print(elefan.make_sound())