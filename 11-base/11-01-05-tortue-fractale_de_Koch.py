import turtle


def koch(t, order, size):
	"""
       Makes turtle 't' draw a Koch fractal of 'order' and 'size'.
       pre:  't' is a Turtle object, ready to draw on some Screen
       post: A Koch fractal of given 'order' and 'size' has been
             drawn by turtle 't' on the screen, and the turtle 't'
             is left facing the same direction.
    """
	if order == 0:  # The base case is just a straight line
		t.forward(size)
	else:
		koch(t, order - 1, size / 3)  # Go 1/3 of the way
		t.color("red")
		t.left(60)
		koch(t, order - 1, size / 3)
		t.color("blue")
		t.right(120)
		koch(t, order - 1, size / 3)
		t.color("green")
		t.left(60)
		koch(t, order - 1, size / 3)


# Of course, to actually run the code above we still need to
# add the necessary instructions to set up the turtle graphics: 
def run_koch(order=3, size=500):
	"""
	Use : run_koch( order=3, size=500 )
	:param order: eg 3
	:param size: eg 500
	:return: none
	"""
	t = turtle.Turtle()
	t.speed(0)
	t.penup()
	t.forward(-200)
	t.pendown()
	koch(t, order, size)  # <- Here is the actual call to the koch function !


window = turtle.Screen()
# au lieu de window.mainloop() destiné à de la progra événementielle
# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
window.update()

run_koch(order=5, size=500)

input("press 'return' to exit")