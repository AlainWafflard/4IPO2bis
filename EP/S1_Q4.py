from abc import ABC, abstractmethod


class Project:
	"""
	Gestion des enregistrements du temps d'un employé
	sur un projet pour un client.
	"""

	def __init__(self, project="", client=""):
		self.__client = ""
		self.__project = project
		self.__performance_l = []
		self.__client = client

	def add(self, emp, det, dur):
		self.__performance_l.append({
			"employee": emp,  # object Employee
			"detail":   det,  # performance description
			"duration": float(dur)  # performance duration
		})

	def __str__(self):
		# templates
		header_s = \
			"""
			Client  : {1}
			Projet  : {2}
			
			Détail des prestations (h)
			"""
		prest_str = "{3:16} {2:8} {0:26} {1:>6.2f}h {4:>6.0f}€\n"
		prest_title_str = "{3:^16} {2:^8} {0:^26} {1:^9} {4:^7}\n"
		t_p = 0  # total prestation
		t_i = 0  # total facturation

		# header
		final_fs = header_s.format("", self.__client, self.__project)
		final_fs += prest_title_str.format("TASK", "DUR", "PERSON", "DEPT", "INV")

		# body
		for data in self.__performance_l:
			# appel à la méthode .get_amount_to_invoice() de l'objet Employee
			amount_to_invoice = data["employee"].get_amount_to_invoice(data["duration"])
			final_fs += prest_str.format(
				data["detail"],
				data["duration"],
				data["employee"].name,
				data["employee"].department,
				amount_to_invoice
			)
			t_p += data["duration"]
			t_i += amount_to_invoice

		# footer
		final_fs += "\n" + prest_str.format("Total prestations", t_p, "", "", t_i)
		return final_fs


# MAIN
# Voici la classe Project, un générateur de factures sur base de prestations.
# Elle gère les enregistrements du temps sur un projet pour un client.
# Observez bien le code fourni, le vôtre devra s'y encastrer.
#
# Vous devez écrire les classes représentant les employés.
# Chaque employé est un objet créé à partir d'une des sous-classes de Employee.
#
# Il y a d'abord la classe abstraite Employee,
# ensuite les classes concrètes Geek, HardwareGeek et Manager.
# Construisez la famille polymorphique de classes.
# Geek est enfant de Employee.
# Déterminez où placer les classes Manager et HardwareGeek dans la famille de classes :
# enfant de Employee ? enfant de Geek ? parent de Geek ? frère de Geek ?
#
# Détail de chaque classe concrète :
#
# classe Geek
#  - attribut : name = le nom de l'employé
#  - attribut : department = "deployment"
#  - la facturation du Geek est calculée par la formule :
#    nb heures prestées * 50 €/h
#
# classe HardwareGeek
#  - attribut : name = le nom de l'employé
#  - attribut : department = idem Geek
#  - la facturation du HardwareGeek est calculée par la formule :
#    les 8 premières heures de prestation sont facturées au tarif plein de 60€/h
#    facturation 8 premières heures = nb heures prestées * 60 €/h
#	 pour les heures suivantes, le tarif horaire est 75% du tarif plein
#    facturation heures suivantes = nb heures prestées * 45 €/h
#
# classe Manager
#  - attribut : name = le nom du manager
#  - attribut : department = idem Geek
#  - la facturation du Manager est calculée par la formule :
#    facturation = prestation + déplacement
#    prestation = nb heures prestées * 80 €/h
#    déplacement = forfait de 40 € ; il y a un déplacement par enregistrement, càd
#    par appel à la méthode Project.add()
#
# Tous les attributs et méthodes sont publics.

# Scenario d'utilisation
if __name__ == "__main__":
	# on crée les objets Employee
	kim = Geek("Kim")
	ali = HardwareGeek("Ali")
	caro = HardwareGeek("Caro")
	albert = Manager("Albert")

	# on crée l'objet Project
	# cette classe est prête, elle ne doit pas être modifiée
	project_o = Project("installation de deux PC", "Lehman Brothers Bank")

	# on ajoute des prestations ; détails et durée sont donnés en paramètres
	project_o.add(albert, "réunion avec client", 12)
	project_o.add(kim, "achat matériel", 4)
	project_o.add(ali, "configuration matériel", 20)
	project_o.add(caro, "installation chez client", 30)
	project_o.add(albert, "remise des clés", 4)

	# on génère la facture avec le détail des prestations et de la facturation
	print(project_o)

	# exemple d'output
	"""
	Client  : Lehman Brothers Bank
	Projet  : installation de deux PC

	Détail des prestations (h)
		  DEPT        PERSON             TASK               DUR      INV  
	deployment       Albert   réunion avec client         12.00h   1000€
	deployment       Kim      achat matériel               4.00h    200€
	deployment       Ali      configuration matériel      20.00h   1020€
	deployment       Caro     installation chez client    30.00h   1470€
	deployment       Albert   remise des clés              4.00h    360€

							  Total prestations           70.00h   4050€
	"""

