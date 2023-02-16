import turtle


def drawSquare(alex: turtle, x50: int):
    """
    Make turtle t draw a square of width sz
    """
    for i in range(4):
        alex.forward(x50)
        alex.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawSquare(50, alex)
# drawSquare(alex, 10)


wn.exitonclick()
