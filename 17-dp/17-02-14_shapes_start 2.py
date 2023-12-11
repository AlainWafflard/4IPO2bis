# Exo 13-11-03 : les quadrilatères
# from pprint import pprint
from inspect import getmembers
from types import FunctionType
import abc
import math



class Shape(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def __init__(self):
		pass

	@abc.abstractmethod
	def calculate_area(self):
		pass

	@abc.abstractmethod
	def calculate_perimeter(self):
		pass

	@classmethod
	def factory(cls, name):
		match name:
			case "circle":
				radius = float(input("radius ? "))
				return Circle(radius)
			case "square":
				width = float(input(" width ? "))
				return Square(width)
			case "rectangle":
				width = float(input(" width ? "))
				height = float(input(" height ? "))
				return Rectangle(height, width)
			case _:
				raise Exception("Shape unknown")




class Rectangle(Shape):
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def calculate_area(self):
		return self.width * self.height

	def calculate_perimeter(self):
		return 2 * ( self.height + self.width )


class Square(Shape):
	def __init__(self, width):
		self.width = width

	def calculate_area(self):
		return self.width * self.width

	def calculate_perimeter(self):
		return 4 * self.width


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		return math.pi	* self.radius * self.radius

	def calculate_perimeter(self):
		return 2 * math.pi * self.radius


# MAIN
shape_name = input("Enter the name of the shape: ")
shape = factory(shape_name)

print("The type of object created: {}".format(type(shape)))
print("The area of the {} is {}:".format(shape_name, shape.calculate_area()))
print("The perimeter of the {} is: {}".format(shape_name, shape.calculate_perimeter()))
