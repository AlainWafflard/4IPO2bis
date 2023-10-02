import turtle


class MyKoch(turtle.Turtle):

	def __init__(self):
		# Of course, to actually run the code we still need to
		# add the necessary instructions to set up the turtle graphics:
		window = turtle.Screen()
		# au lieu de window.mainloop() destiné à de la progra événementielle
		# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
		window.update()
		# faire exécuter le constructor de la classe parent
		super().__init__()
		# initialisation tortue
		self.speed(0)
		self.penup()
		self.forward(-200)
		self.pendown()

	def koch(self, order, size):
		"""
		   Makes turtle 't' draw a Koch fractal of 'order' and 'size'.
		   pre:  't' is a Turtle object, ready to draw on some Screen
		   post: A Koch fractal of given 'order' and 'size' has been
				 drawn by turtle 't' on the screen, and the turtle 't'
				 is left facing the same direction.
		"""
		if order == 0:  # The base case is just a straight line
			self.forward(size)
		else:
			self.koch(order - 1, size / 3)  # Go 1/3 of the way
			self.color("red")
			self.left(60)
			self.koch(order - 1, size / 3)
			self.color("blue")
			self.right(120)
			self.koch(order - 1, size / 3)
			self.color("green")
			self.left(60)
			self.koch(order - 1, size / 3)


# MAIN
# the purpose of this code is to draw Koch fractals
if __name__ == '__main__':
	k = MyKoch()
	k.koch(3, 500)  # <- Here is the actual call to the koch function !
	input("press 'return' to exit")
