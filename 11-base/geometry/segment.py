import math

class Segment:

    def __init__(self, points):
        self.points = points
        self.longueur_type = "manhattan"

    def __del__(self):
        print("segment détruit")

    def longueur_Manhattan(self):
        abs0 = self.points[0].abscisse()
        ord0 = self.points[0].ordonnee()
        abs1 = self.points[1].abscisse()
        ord1 = self.points[1].ordonnee()
        d = abs( abs0 - abs1 ) + abs( ord0 - ord1 )
        return d

    def longueur_pythagore(self):
        abs0 = self.points[0].abscisse()
        ord0 = self.points[0].ordonnee()
        abs1 = self.points[1].abscisse()
        ord1 = self.points[1].ordonnee()
        d = math.sqrt( (abs0 - abs1)**2 + (ord0 - ord1)**2 )
        return d

    def longueur(self):
        if self.longueur_type == "pythagore" :
            return self.longueur_pythagore()
        elif self.longueur_type == "manhattan":
            return self.longueur_Manhattan()
        else:
            print("longueur_type non défini")
