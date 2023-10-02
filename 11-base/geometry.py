# Un point est représenté par son abscisse et son ordonnée
# Constructeur : coordonnées (0, 0) par défaut
# Méthode « distance » : calcule et renvoie la distance du point avec l’origine (0, 0)
import math

class Point:

    def __init__(self, coord=(0, 0) ):
        self.coord = coord
        self._distance = None

    def __del__(self):
        print("point détruit")

    def __str__(self):
        return f" abscisse {self.coord[0]}, ordonnée {self.coord[1]} "

    def distance(self):
        if self._distance is None:
            print("distance calculée")
            self._distance = self.coord[0] + self.coord[1]
        return self._distance

    def abscisse(self):
        return self.coord[0]

    def ordonnee(self):
        return self.coord[1]

class Segment:

    def __init__(self, points):
        self.points = points
        self.__longueur_type = "manhattan"

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
        if self.__longueur_type == "pythagore" :
            return self.longueur_pythagore()
        elif self.__longueur_type == "manhattan":
            return self.longueur_Manhattan()
        else:
            print("longueur_type non défini")


# p0 = Point()
p1 = Point( (3,4) )
p2 = Point( (6,0) )
# print(p0,"distance=", p0.distance())
# print(p1, "distance=", p1.distance())

mon_segment1 = Segment( (p1,p2) )
print(mon_segment1.longueur())  # 7
mon_segment1.__longueur_type = "pythagore"
print(mon_segment1.longueur())  # 5.0
print(mon_segment1.__longueur_type)

# mon_segment2 = Segment( ( Point( (1,1)), Point( (2,2)) ) )
# print(mon_segment.longueur_pythagore())
# print(mon_segment2.longueur_Manhattan())  # 2

# del(mon_segment1)
# del(mon_segment2)

print("------------------")