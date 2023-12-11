from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    # def __init__(self, name, age):
    #     super().__init__(name, age)
    #     ... du code en plus ...

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


class Duck(Animal):
    def info(self):
        print(f"I am a duck. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Coin coin")


animal_l = [
    Cat("Kitty", 2.5),
    Dog("Fluffy", 4),
    Duck("Donald", 5 )
]

for animal in animal_l:
    animal.info()
    animal.make_sound()

