import time
class Predator:
    def __init__(self, position):
        self.position = position
        self.prey_o = None

    def __str__(self):
        return f"predator : {self.position}"

    def set_prey(self, prey_o):
        self.prey_o = prey_o

    def move_to_prey(self):
        self.position += 10

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

    def __str__(self):
        return f"prey : {self.status} {self.position}"

    def set_predator(self, predator_o):
        self.predator_o = predator_o

    def escape(self):
        diff = self.position - self.predator_o.position
        if diff <= 20:
            self.position += 5
            self.status = "escaping"
        else:
            self.status = "quiet"


lion = Predator(0)
buffle = Prey(100)
lion.set_prey(buffle)
buffle.set_predator(lion)

while True:
    lion.move_to_prey()
    print(lion)
    buffle.escape()
    print(buffle)
    if lion.prey_caught():
        print("Caught ! Bon appétit !")
        break
    time.sleep(1)

# • OUTPUT
# predator : 10 / prey : quiet 100
# predator : 20 / prey : quiet 100
# …
# predator : 80 / prey : escaping 105
# predator : 90 / prey : escaping 110
# predator : 100 / prey : escaping 115
# predator : 110 / prey : escaping 120
# predator : 120 / predator caught pre