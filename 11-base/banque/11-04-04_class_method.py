# Variable de classe
# privée + getter/setter

class Compte:
	__taux_interet = 0.02

	def __init__(self, owner):
		self.owner = owner

	@classmethod
	@property
	def taux_interet(cls):
		# cls.__taux_interet = 0.25
		return cls.__taux_interet

	@classmethod
	def set_taux_interet(cls, nouveau_taux):
		cls.__taux_interet = nouveau_taux



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
Compte.set_taux_interet(0.04)
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

print("modification au niveau de l'objet - don't do that")
kim_c.set_taux_interet(0.06)
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

print("remodification au niveau de la classe")
Compte.set_taux_interet(0.08)
print("taux général", Compte.taux_interet)
print("taux de Kim", kim_c.taux_interet)
print("taux de Hilde", hilde_c.taux_interet)
print()

