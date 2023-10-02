import point
import segment
import math
class Cercle:

    def __init__(self, centre: point.Point, rayon:float):
        self.centre = centre
        self.rayon = rayon

    def getPerimetre(self):
        return 2 * math.pi * self.rayon

    def getSurface(self):
        return math.pi * self.rayon**2

    def isInside(self, point_ext: point.Point) -> bool:
        """
        isInside(Point p) : retourne True si p appartient
        au cercle, càd si la longueur du segment(p , r) est
        inférieure au rayon.
        :param point_ext:
        :return:
        """
        seg = segment.Segment( ( self.centre, point_ext ))
        seg.longueur_type = "pythagore"
        long = seg.longueur()
        return long <= self.rayon


# print(__name__)
if __name__ == "__main__":
    print("voici les tests de la classe Cercle")
    mon_cercle = Cercle( point.Point( (4, 5) ), 3 )
    print(mon_cercle.getPerimetre())
    print(mon_cercle.getSurface())
    print(mon_cercle.isInside( point.Point( (100,0))))
    print(mon_cercle.isInside( point.Point( (4, 4))))



