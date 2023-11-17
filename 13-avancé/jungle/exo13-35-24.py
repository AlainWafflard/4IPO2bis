import time
class Predator:
    def __init__(self, position):
        self.position = position
        self.prey_o = None
        self.water_o = None
        self.status = "walking"

    def __str__(self):
        return f"predator : {self.status} {self.position}"

    def set_prey(self, prey_o):
        self.prey_o = prey_o

    def set_water(self, water_o):
        self.water_o = water_o

    def move(self):
        """
        soit marcher tranquillos
        soit boire de l'eau
        soit courir après le buffle
        deux parties
        - conditions
        - mouvement
        """
        # conditions
        self.status = "walking"
        if abs(self.position-self.water_o.position) <= 5:
            self.status = "drinking"
        if abs(self.position-self.prey_o.position) <= 50:
            self.status = "hunting"
        if abs(self.position-self.prey_o.position) <= 2:
            self.status = "eating"

        # mouvement
        if self.status == "walking":
            self.position += 10
        elif self.status == "hunting":
            self.position += 20
        else:
            self.position += 0


    def prey_caught(self):
        out = False
        if abs(self.position - self.prey_o.position) <= 5:
            out = True
        return out


class Prey:

    def __init__(self, position):
        self.position = position
        self.predator_o = None
        self.status = "quiet"
        self.water_o = None

    def __str__(self):
        return f"prey : {self.status} {self.position}"

    def set_predator(self, predator_o):
        self.predator_o = predator_o

    def set_water(self, water_o):
        self.water_o = water_o

    def move(self):
        """
        soit marcher tranquillos
        soit boire de l'eau
        soit s'enfuit du prédateur
        deux parties
        - conditions
        - mouvement
        """
        # conditions
        self.status = "walking"
        if abs(self.position-self.water_o.position) <= 5:
            self.status = "drinking"
        if abs(self.position-self.predator_o.position) <= 25:
            self.status = "escaping"
        if abs(self.position-self.predator_o.position) <= 2:
            self.status = "caught"

        # mouvement
        if self.status == "walking":
            self.position += 5
        elif self.status == "escaping":
            self.position += 10
        else:
            self.position += 0


class Water:

    def __init__(self, position):
        self.position = position


lion = Predator(3)
buffle = Prey(100)
lac = Water(150)
lion.set_prey(buffle)
lion.set_water(lac)
buffle.set_predator(lion)
buffle.set_water(lac)

while True:
    lion.move()
    print(lion)
    buffle.move()
    print(buffle)
    if lion.prey_caught():
        print("Caught ! Bon appétit !")
        break
    time.sleep(1)

# Ecrivez les classes Water, Prey et Predator correspondant aux
# spécifications suivantes :
# • Un lac se trouve à 150m, une proie à 100m et un prédateur à 0m.
# • Le lac contient une réserve d'eau infinie.
# • Les animaux se déplacent à leur rythme vers la droite (cf figure).
# • Quand un animal rencontre le lac, il s'y arrête pour y boire.
# • Le prédateur voit la proie quand celle-ci est à moins de 50m,
#    et se met alors à courir vers # elle pour l'attraper.
# • La proie voit le prédateur quand celle-ci est à moins de 25m,
#   et se met alors à fuir.
# • Boire ou fuir, il faut choisir … la fuite. ;-)
#

# • OUTPUT
# predator : 10 / prey : quiet 100
# predator : 20 / prey : quiet 100
# …
# predator : 80 / prey : escaping 105
# predator : 90 / prey : escaping 110
# predator : 100 / prey : escaping 115
# predator : 110 / prey : escaping 120
# predator : 120 / predator caught pre