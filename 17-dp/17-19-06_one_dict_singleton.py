class Storage:
	__instance = None
	# None => object not created
	# Smthg => object already created

	@classmethod
	def singleton(cls):
		""" Static access method.
		 	Used to :
		 	 - create the object, only once
		 	 - initialize the object (constructor)
		 	 - return the object
		"""
		if cls.__instance is None:
			# l'objet est créé, uniquement s'il n'existe pas
			cls.__instance = cls()
		# l'objet est retourné
		return cls.__instance

	def __init__(self):
		""" private constructor
			If the instance already exists, it will raise an exception.
			After this, the usual constructor commands are run.
		"""
		if self.__instance is not None:
			raise Exception("This class is a singleton! Use Storage.singleton()")

		# Data storage as Dictionnary
		self.__data = {}

	def __str__(self):
		output = "Storage:\n"
		for k in self.__data:
			output += " - clé {} : valeur {}\n".format(k, self.__data[k])
		return output

	def append(self, k, v):
		if k in self.__data.keys():
			raise Exception("key {} already exists".format(k))
		self.__data[k] = v


# Dans un certain module, il se passe ceci :
s = Storage.singleton()
s.append( "fname", "Kevin")

# Dans un autre module, il se passe cela :
t = Storage.singleton()
t.append( "lname", "Costner")

# Encore dans un autre, il se passe cela :
u = Storage.singleton()
u.append("mail", "kevin@costner.world")

print("s : " + str(s))
print("t : " + str(t))
print("u : " + str(u))
print("s is t ?", s is t)
print("s is u ?", s is u)
print("t is u ?", t is u)

# Try this, it will give an error !
# "Exception: This class is a singleton!"
# You must call this class via the singleton static method
# v = Storage()

