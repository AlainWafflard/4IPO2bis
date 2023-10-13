class Car:

    def __init__(self, name):
        self.name = name
        self.speed = 0

    def __str__(self):
        return f"{self.name}: speed {self.speed} km/h"

    def increment(self, inc=1 ):
        self.speed += inc

    def decrement(self, dec=1 ):
        self.speed -= dec


voiture_A = Car("Peugeot")
print(voiture_A)
voiture_A.increment()
print(voiture_A)
voiture_A.increment(10)
print(voiture_A)
voiture_A.decrement()
print(voiture_A)

