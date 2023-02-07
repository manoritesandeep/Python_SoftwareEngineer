from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass

    def eat(self):
        print('Eating...')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


d = Dog('bow')
print(d.num_legs())

animals = [Dog('Bow'), Monkey('Dang')]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_legs())