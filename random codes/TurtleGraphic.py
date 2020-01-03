import turtle
import math

keith = turtle.Turtle()

keith.speed(10)

# keith.forward(100)
# keith.left(45)
# keith.forward(100)
# keith.right(90)
# keith.forward(100)

# color(outline, fill)
# keith.color("#3C9118")
# keith.color("cyan", "#3C9118")

# keith.begin_fill()
# for x in range(0, 4):
# 	keith.forward(100)
# 	keith.left(90)
# keith.end_fill()

# keith.penup()
# keith.forward(150)
# keith.pendown()

# keith.begin_fill()
# for x in range(0, 4):
# 	keith.forward(100)
# 	keith.left(90)
# keith.end_fill()

	# keith.penup()
	# keith.setx(300)
	# keith.sety(-200)
	# keith.pendown()

	# original = keith.position()
	# print(original)

	# keith.begin_fill()
	# for x in range(0,1000):
	# 	keith.forward(math.sqrt(10))
	# 	keith.left(math.sin(x/10)*25)
	# 	keith.left(20)
	# keith.end_fill()

keith.penup()
keith.setx(0)
keith.sety(0)
keith.pendown()

keith.getscreen().bgcolor("#994444")

def star(turtle, size):
	if size <= 50:
		return
	else:
		for x in range(5):
			turtle.forward(size)
			star(turtle, size/2.5)
			turtle.right(144)

star(keith, 300)

turtle.done()