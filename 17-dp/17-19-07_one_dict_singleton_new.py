class Storage(object):
	__instance = None
	# None => object not created
	# Smthg => object already created

	def __new__(cls):
		if cls.__instance is None:
			# objet créé uniquement s'il n'existe pas
			cls.__instance = super(Storage, cls).__new__(cls)
			# cls.__instance = Storage()
		return cls.__instance  # objet retourné

	def __init__(self):
		# Data storage as Dictionnary
		if not hasattr(self, "data"):
			# creating dict only once
			self.data = {}

	def __str__(self):
		output = "Storage:\n"
		for k in self.data:
			output += " - clé {} : valeur {}\n".format(k, self.data[k])
		return output

	def append(self, k, v):
		if k in self.data.keys():
			raise Exception("key {} already exists".format(k))
		self.data[k] = v


# Dans un certain module, il se passe ceci :
s = Storage()
s.append( "fname", "Kevin")

# Dans un autre module, il se passe cela :
t = Storage()
t.append( "lname", "Brian")

print("s:", s)
print("t:", t)
print("s == t ?", s == t)
print("s is t ?", s is t)

