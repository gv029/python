import turtle

WIDTH = 1000
HEIGHT = 600
window = turtle.Screen()
window.bgcolor("red")
window.setup(WIDTH,HEIGHT)

alex = turtle.Turtle()
alex.color("yellow")
alex.speed(100)


def draw_square():
    alex.forward(120)
    alex.rt(90)
    alex.forward(120)
    alex.rt(90)
    alex.forward(120)
    alex.rt(90)
    alex.forward(120)
    alex.rt(90)

for i in range(36):
    draw_square()
    alex.right(10)
alex.backward(300)

for i in range(36):
    draw_square()
    alex.right(10)
alex.forward(600)

for i in range(36):
    draw_square()
    alex.right(10)


window.exitonclick()
