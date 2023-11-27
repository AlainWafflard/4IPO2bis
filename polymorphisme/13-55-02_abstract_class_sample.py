# Python program showing how
# abstract base class work
from abc import ABC, abstractmethod

class Polygon(ABC):
	@property
	@abstractmethod
	def name(self):
		return "polygon"

	@abstractmethod
	def number_of_sides(self):
		pass

	# def __str__(self):
	# 	return "blabla"


class Triangle(Polygon):

	@property
	def name(self):
		return "triangle"

	# overriding abstract method
	def number_of_sides(self):
		print(self.name + " : I have 3 sides")


class Pentagon(Polygon):

	@property
	def name(self):
		return "pentagon"

	# overriding abstract method
	def number_of_sides(self):
		print(self.name + " : I have 5 sides")


# Driver code
try:
	R = Triangle()
	R.number_of_sides()

	R = Pentagon()
	R.number_of_sides()

	P = Polygon()
	P.number_of_sides()  # error, why ?

except Exception as err:
	print("ERROR : " + str(err))
