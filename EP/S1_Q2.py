class CalculatorSingleton:
	"""
	classe CalculatorSingleton
	- à la construction, elle reçoit les valeurs de x et y
	- via les méthodes appropriées, elle effectue l'addition, la soustraction ou la multiplication de x et y
	- x et y sont des attributs privés, leur setter valide leur valeur
	"""
	def __init__():
		pass

	def plus():
		""" addition des deux nombres x et y préalablement définis """
		pass

	def moins():
		""" soustraction des deux nombres x et y préalablement définis """
		pass

	def fois():
		""" multiplication des deux nombres x et y préalablement définis """
		pass


# MAIN
if __name__ == '__main__':
	#
	# Modifiez la classe CalculatorSingleton suivant les consignes suivantes :
	# - x et y privés, munis d'accesseurs
	# - x doit être positif, sinon une exception est générée et le programme s'arrête (cf remarque)
	# - y doit être positif et inférieur ou égal à 10, sinon sa valeur est ramenée à 0 ou à 10
	#   (selon qu'elle est inférieure à 0 ou supérieure à 10)
	# 
	# Implantez la procédure de test, càd trois calculs.
	# !! N'implanter que les calculs assignés (cf Moodle) !!
	#
	# SQ 1 :    ( 3 + 4 ) * ( 3 + 2 )
	# SQ 2 :    ( 3 + ( 5 - 2 ) ) * 2
	# SQ 3 :    ( 5 * 3 ) + ( 4 * 2 )
	# SQ 4 :    ( 24 * 18 ) * ( 3 + 4 )
	# SQ 5 :    ( 12 + 14 ) * ( 3 - 16 )
	# SQ 6 :    ( 25 * 2 ) * ( 6 - 12 )
	# SQ 7 :	( ( -125 * 5 ) * 5 ) * ( ( 2 * 2 ) - 1 )
	# SQ 8 : 	( -3 + 1 ) * ( 12 - ( ( 2 + 2 ) * -3 )
	# SQ 9 :    ( -4 * 6 ) * ( ( 6 - 3 ) - ( 2 + 1 ) )
	#
	# Remarques :
	# - En cas de problème avec les valeurs de test, enclencher une exception
	#   cf https://www.w3schools.com/python/python_try_except.asp
	#   Exemple:
	# 		if x == "bad value" :
	#			raise Exception("x must be a good value")
	#

	# Exemple d'implantation
	try:
		#    ( 3 + 4 ) * ( 3 + 2 ) 		=> 35
		print( CalculatorSingleton( CalculatorSingleton( 3, 4 ).plus(), CalculatorSingleton( 3, 2 ).plus() ).fois() )
		#    ( 3 + 4 ) * ( 20 - 12 ) 	=> 70 (car y (12) est devenu 10)
		print( CalculatorSingleton( CalculatorSingleton( 3, 4 ).plus(), CalculatorSingleton( 20, 12 ).moins() ).fois() )
		#    ( 3 + 4 ) * ( -3 + 2 ) 	=> exception : "x (-3) ne peut pas être négatif"
		print( CalculatorSingleton( CalculatorSingleton( 3, 4 ).plus(), CalculatorSingleton( -3, 2 ).plus() ).fois() )
	except Exception as e :
		print("! Exception:", e, "!")


