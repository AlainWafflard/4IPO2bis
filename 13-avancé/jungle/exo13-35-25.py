import time


class JungleComponent:

    def __init__(self, position):
        self.position = position
        self.status = "quiet"

    def prey_caught(self):
        return False

    def move(self):
        pass


class Resource(JungleComponent):
    # quantity = 0

    def __init__(self, position):
        super().__init__(position)
        self.quantity = 0

    def __str__(self):
        return f"{self.name} : qnt {self.quantity}"

    def enough(self):
        return self.quantity > 0

    def decrease(self):
        self.quantity -= 5


class Archaeplastida(Resource):
    name = "plant"

    def __init__(self, position):
        super().__init__(position)
        self.quantity = 50


class Water(Resource):
    name = "water"

    def __init__(self, position):
        super().__init__(position)
        self.quantity = 100


class Animal(JungleComponent):
    name = "animal"

    def __init__(self, position):
        super().__init__(position)
        self.water_o = None
        self.status = ""

    def __str__(self):
        return f"{self.name} : status {self.status} pos {self.position}"

    def set_water(self, water_o):
        self.water_o = water_o



class Predator(Animal):
    name = "predator"

    def __init__(self, position):
        super().__init__(position)
        self.prey_o = None
        self.status = "walking"

    def set_prey(self, prey_o):
        self.prey_o = prey_o

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
        if abs(self.position-self.water_o.position) <= 5 and self.water_o.enough() :
            self.status = "drinking"
            self.water_o.decrease()
        if abs(self.position-self.prey_o.position) <= 50:
            self.status = "hunting"
        if abs(self.position-self.prey_o.position) <= 2:
            self.status = "eating"

        # mouvement
        if self.status == "walking":
            self.position -= 10
        elif self.status == "hunting":
            self.position -= 20
        else:
            self.position += 0

    def prey_caught(self):
        out = False
        if abs(self.position - self.prey_o.position) <= 5:
            out = True
        return out


class Prey(Animal):
    name = "prey"

    def __init__(self, position):
        super().__init__(position)
        self.predator_o = None
        self.archaeplastida_o = None
        self.status = "quiet"

    # def __str__(self):
    #     return f"prey : {self.status} {self.position}"

    def set_predator(self, predator_o):
        self.predator_o = predator_o

    def set_archaeplastida(self, archaeplastida_o):
        self.archaeplastida_o = archaeplastida_o

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
        if abs(self.position-self.archaeplastida_o.position) <= 5 and self.archaeplastida_o.enough():
            self.status = "eating"
            self.archaeplastida_o.decrease()
        if abs(self.position-self.water_o.position) <= 5 and self.water_o.enough() :
            self.status = "drinking"
            self.water_o.decrease()
        if abs(self.position-self.predator_o.position) <= 25:
            self.status = "escaping"
        if abs(self.position-self.predator_o.position) <= 2:
            self.status = "caught"

        # mouvement
        if self.status == "walking":
            self.position += 5
        elif self.status == "escaping":
            self.position -= 10
        else:
            self.position += 0



if __name__ == '__main__':
    jungle_d = {}
    jungle_d['lion'] = Predator(150)
    jungle_d['buffle'] = Prey(1)
    jungle_d['lac'] = Water(100)
    jungle_d['plante'] = Archaeplastida(50)
    jungle_d['lion'].set_prey(jungle_d['buffle'])
    jungle_d['lion'].set_water(jungle_d['lac'])
    jungle_d['buffle'].set_predator(jungle_d['lion'])
    jungle_d['buffle'].set_water(jungle_d['lac'])
    jungle_d['buffle'].set_archaeplastida(jungle_d['plante'])

    caught = False
    while not caught:
        for jungle_component in jungle_d.values():
            jungle_component.move()
            print(jungle_component)
            if jungle_component.prey_caught():
                print("Caught ! Bon appétit !")
                caught = True
        time.sleep(1)


# Créez la classe Archaeplastida sous
# la classe Resource. OK
# • Spécifications supplémentaires :
# • La proie mange la plante OK
# • L'eau est disponible en quantité limitée.
# • La plante est disponible en quantité limitée.
# • Les animaux gagnent en énergie en mangeant
# ou en buvant.
# • Les animaux perdent leur énergie en
# marchant ou, encore plus, en courant.
# • Sans énergie, les animaux ne peuvent plus se
# déplacer.
# • Prévoir une méthode draw() qui affiche
# l'état de l'obje



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