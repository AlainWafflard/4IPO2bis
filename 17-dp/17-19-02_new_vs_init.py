class A():
	def __new__(cls):
		print("In A __new__")
		return B()

	def __init__(self):
		print("In A __init__")


class B():
	def __init__(self):
		print("In B __init__")


a = A()
print()
print(type(a))

# b = B()
# print(type(b))
