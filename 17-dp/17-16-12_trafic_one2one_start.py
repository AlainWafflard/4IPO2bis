# Pas d'encapsulation : tous attributs publics

class Observer:
    """ observateur """

    # def __init__(self, observable):
    #     observable.subscribe(self)

    def notify( self, observable, *args, **kwargs ):
        print ('Got', args, kwargs, 'From', observable)


class Car(Observer) :

    def __init__(self, brand):
        self.brand = brand
        self.running = False

    def __str__(self):
        if self.running == True :
            return "{} says: Yeah, running on the road 66.".format(self.brand)
        else :
            return "{} says: Arghh, waiting for the green light.".format(self.brand)

    def notify( self, color ):
        # print ('Got', args, kwargs, 'From', observable)
        if color == 1 :
            print("red")
            self.stop()
        elif color == 2 :
            print("green")
            self.start()
        elif color == 3 :
            print("yellow")
            self.stop()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False




class Observable:
    """ sujet """

    def __init__(self):
        self.observer_l = []

    def subscribe(self, observer):
        self.observer_l.append(observer)

    def notify_observer_l(self, *args, **kwargs):
        for obs in self.observer_l:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self.observer_l.remove(observer)


class Light(Observable):
    """ modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ["", "RED", "GREEN", "YELLOW"]

    def __init__(self):
        super().__init__()
        self.color = 1

    def __str__(self):
        out = ""
        for obs in self.observer_l:
            out += obs.brand
        return "Light says : My color is {}; I follow the cars {}".format(
            self.color_name_a[self.color],
            out )

    def notify_observer_l(self):
        for obs in self.observer_l:
            obs.notify(self.color)

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        self.notify_observer_l()


if __name__ == '__main__':
    feu01 = Light()
    voiture_A = Car("Peugeot")
    feu01.subscribe(voiture_A)

    for i in range(8):
        print(feu01)
        print(voiture_A)
        feu01.change()
