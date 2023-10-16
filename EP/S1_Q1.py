
class CalculatorToolBox:
	"""
	Class Calculator_ToolBox : c'est une classe utilisée comme boîte à outils
	Fonctionnalités :
	- elle simule le comportement d'une petite calculatrice
	- elle effectue l'addition, la soustraction, la multiplication, la division
	- elle gère une valeur "mémoire" avec les fonctionnalités : ajouter, soustraire, effacer, récupérer la valeur
	!! Remarque : Cette classe ne peut pas être modifiée. !!
	"""
	def __init__(self):
		self.memoire = 0

	def plus(self, x, y ):
		""" addition des deux nombres x et y """
		return x + y

	def moins(self, x, y ):
		""" soustraction de deux nombres x et y """
		return x - y

	def fois(self, x, y ):
		""" multiplication des deux nombres x et y """
		return x * y

	def diviser(self, x, y ):
		""" division de deux nombres x et y """
		return x / y

	def memoire_plus(self, x ):
		self.memoire += x

	def memoire_moins(self, x ):
		self.memoire -= x

	def memoire_effacer(self):
		self.memoire = 0

	def memoire_recuperer(self):
		return self.memoire


if __name__ == "__main__":
	#
	# Ecrivez le code POO en utilisant la classe Calculator_ToolBox
	# afin de calculer les expressions suivantes.
	# !! Ne répondre qu'aux sous-questions assignées (cf Moodle) !!
	#
	# SQ 1 :    ( 3 + 4 ) * ( 3 + 2 )
	# SQ 2 :    ( 3 + ( 5 - 2 ) ) * 2
	# SQ 3 :    ( 5 * 3 ) + ( 4 * 2 )
	# SQ 4 :    ( 24 / 8 ) * ( 33 / ( 3 + 4 + 4 ) )
	# SQ 5 :    ( ( 12 + 8 + 4 ) * 4 ) / ( 3 * 16 )
	# SQ 6 :    ( 25 * 2 ) / ( 6 + 2 + 2 )
	# SQ 7 :	( ( 125 / 5 ) / 5 ) / ( ( 2 / 2 ) - 1 )
	# SQ 8 : 	( 3 + 1 + 1 ) / ( 12 - ( ( 2 + 2 ) * 3 )
	# SQ 9 :    ( 4 * 6 * 4 ) / ( ( 6 - 3 ) - ( 2 + 1 ) )
	#
	# Remarques :
	# - Un seul objet Calculator_ToolBox est créé.
	# - Ne pas utiliser les symbôles arithmétiques +, -, *, etc.
	# - En cas d'addition de trois nombres, utiliser la mémoire de l'objet.
	# - En cas de problème de calcul, enclencher une exception
	#   cf https://www.w3schools.com/python/python_try_except.asp
	#   Exemple:
	# 		try:
	# 			x = 5 / 0
	# 		except:
	# 			print("division par zéro impossible")
	#
	calc = CalculatorToolBox()
	print( calc.plus( 1, 2 ))

