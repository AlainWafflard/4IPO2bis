# Structure polymorphique
# Chaque classe possède les mêmes méthodes
# class mère : Compte (abstraite)
# classes enfants : CompteCourant et CompteEpargne
from abc import ABC, abstractmethod


class Compte(ABC):
	_type = ""   # compte Renaissance

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def __str__(self):
		return "{0} ({2}) : solde de {1}".format(self.owner, self.balance, self._type)

	@abstractmethod
	def deposer(self, somme):
		self.balance += somme

	@abstractmethod
	def retirer(self, somme):
		self.balance -= somme

	@abstractmethod
	def transferer(self, compteDest, somme):
		pass


class CompteCourant(Compte):
	__frais_retrait = 1
	_type = "CC"

	def deposer(self, somme):
		super().deposer(somme)

	def retirer(self, somme):
		super().retirer(somme + self.__frais_retrait)
		if self.balance < 0:
			# compte en négatif => on prévient le client
			print("{0} ({2}) : solde négatif ({1}), attention aux intérêts débiteurs".format(
				self.owner, self.balance, self._type))

	def transferer(self, compteDest, somme):
		self.retirer(somme)
		compteDest.deposer(somme)


class CompteEpargne(Compte):
	__frais_retrait = 0
	_type = "CE"

	def deposer(self, somme):
		super().deposer(somme)

	def retirer(self, somme):
		if somme > self.balance:
			# solde insuffisant => retrait interdit
			print(
				"{0} ({3}) : solde insuffisant ({1}) pour procéder à un retrait de {2}".format(
					self.owner, self.balance, somme, self._type))
			return
		super().retirer(somme + self.__frais_retrait)

	def transferer(self, compteDest, somme):
		print("Un virement n'est pas autorisé depuis ce compte.")


# MAIN
kong_cc = CompteCourant("Kong")
kong_cc.deposer(50)

kim_cc = CompteCourant("Kim")
kim_cc.deposer(200)
kim_cc.transferer(kong_cc, 100)
kim_cc.retirer(500)
print(kim_cc)  # -402

kim_ce = CompteEpargne("Kim")
kim_ce.deposer(200)
kim_ce.transferer(kong_cc, 100)  # error
kim_ce.retirer(500)  # error
print(kim_ce)  # 200

print(kong_cc)  # 150

# philippe_compte = Compte("Philippe")

