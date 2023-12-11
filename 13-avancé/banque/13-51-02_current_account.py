class Compte:
	_taux_interet = 0.01

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def deposer(self, somme):
		self.balance += somme

	def retirer(self, somme):
		if self.balance - somme < 0 :
			print("le solde doit rester positif")
			return
		self.balance -= somme

	def __str__(self):
		return "owner : {}; balance : {}".format( self.owner, self.balance)

	def calcul_interet(self):
		interet = self.balance * self._taux_interet
		self.balance += interet


class CompteCourant(Compte):
	__frais = 1

	def retirer(self, somme):
		total = somme + self.__frais
		# super().retirer(total)
		self.balance -= total
		if self.balance < 0 :
			print("attention, solde négatif")

	def transferer(self, compteDest, somme ):
		self.retirer(somme)
		compteDest.deposer(somme)


class CompteEpargne(Compte):
	_taux_interet = 0.04


	# def retirer(self, somme):
	# 	if self.balance - somme < 0 :
	# 		print("le solde doit rester positif")
	# 		return
	# 	super().retirer(somme)


# MAIN
tennis_c = Compte("Tennis")
tennis_c.deposer(1000)
tennis_c.retirer(1500)

kim_c = CompteCourant("Kim")
kim_c.deposer(1000)
kim_c.retirer(1500)
# print(kim_c)

clijster_c = CompteEpargne("Clijster")
# print(clijster_c)
clijster_c.deposer(1000)
clijster_c.retirer(1500)

exit()

# kim_c.transferer(clijster_c, 100)
kim_c.retirer(100)
clijster_c.retirer(10)
print(kim_c)
print(clijster_c)

clijster_c.calcul_interet()
clijster_c.retirer(500)
print(clijster_c)

kim_c.calcul_interet()
print(kim_c)
print(clijster_c._taux_interet)
# print(clijster_c.__brol)

