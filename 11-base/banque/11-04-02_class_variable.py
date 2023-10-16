# Variable de classe
# public

class Compte:
	taux_interet = 0.02

	def __init__(self, owner):
		self.owner = owner


# MAIN
print("valeurs au niveau de la classe")
print("taux général", Compte.taux_interet)
print()

print("valeurs au niveau de l'objet")
kim_c = Compte("Kim")
print("taux de Kim", kim_c.taux_interet)
hilde_c = Compte("Hilde")
print("taux de Hilde", hilde_c.taux_interet)
print()

print("modification au niveau de la classe")
Compte.taux_interet = 0.04
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

print("modification au niveau de l'objet")
kim_c.taux_interet = 0.06
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

print("remodification au niveau de la classe")
Compte.taux_interet = 0.08
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

