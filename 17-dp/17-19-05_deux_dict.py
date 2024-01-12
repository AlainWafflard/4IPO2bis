class Storage:
	__singleton_o = None

	@classmethod
	def singleton(cls):
		if cls.__singleton_o is None:
			cls.__singleton_o = cls()
		return cls.__singleton_o

	def __init__(self):
		self.__data = {}  # Data storage as Dictionnary

	def __str__(self):
		output = "Storage:\n"
		for k in self.__data:
			output += " - clé {} : valeur {}\n".format(k, self.__data[k])
		return output

	def append(self, k, v):
		if k in self.__data.keys():
			raise Exception("key {} already exists".format(k))
		self.__data[k] = v
		return self.__singleton_o


# Dans un certain module, il se passe ceci :
Storage.singleton().append( "fname", "Prénom")

# Dans un autre module, il se passe cela :
Storage.singleton().append( "lname", "Nom de famille")

v = Storage()
v.append("brol", 'gnagna')

# print("s:", s)
# print("t:", t)
# print("s == t ?", s == t)
# print("s is t ?", s is t)
print(v)

