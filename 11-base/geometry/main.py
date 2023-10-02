# Un point est représenté par son abscisse et son ordonnée
# Constructeur : coordonnées (0, 0) par défaut
# Méthode « distance » : calcule et renvoie la distance du point avec l’origine (0, 0)
import point
import segment
import cercle

# p0 = Point()
p1 = point.Point( (3,4) )
p2 = point.Point( (6,0) )
# print(p0,"distance=", p0.distance())
# print(p1, "distance=", p1.distance())

mon_segment1 = segment.Segment( (p1,p2) )
print(mon_segment1.longueur())  # 7
mon_segment1.longueur_type = "pythagore"
print(mon_segment1.longueur())  # 5.0
print(mon_segment1.longueur_type)

mon_cercle = cercle.Cercle(point.Point((4, 5)), 4)
print(mon_cercle.getPerimetre())
print(mon_cercle.getSurface())
print(mon_cercle.isInside(point.Point((100, 0))))
print(mon_cercle.isInside(point.Point((4, 4))))

print("------------------")
