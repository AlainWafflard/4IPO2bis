class Car:

    def __init__(self, name):
        self.__name = name
        self.speed = 0
        self.duration = 0       # durée limitée
        self.__time = 0           # depuis le début (cumulé)
        self.__position = 0       # depuis le début (cumulé)

    def __str__(self):
        return f"{self.__name}: sp {self.speed}km/h, ti {self.__time}h, po {self.__position}km"

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val ):
        if val < 0 : val = 0
        if val > 50 : val = 50
        self.__speed = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val ):
        if val < 0 : val = 0
        self.__duration = val

    def forward(self):
        dist = self.speed * self.duration
        self.__time += self.duration
        self.__position += dist


voiture_A = Car("A")
print(voiture_A)
voiture_A.speed = 50
voiture_A.duration = 1
voiture_A.forward()
print(voiture_A)
voiture_A.duration = 0.5
voiture_A.forward()
print(voiture_A)
voiture_A.duration = 1
voiture_A.forward()
print(voiture_A)
voiture_A.duration = -0.5
voiture_A.forward()
print(voiture_A)
voiture_A.duration = 1
voiture_A.speed = -50
voiture_A.forward()
print(voiture_A)
