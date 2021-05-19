from turtle import Turtle, Screen
import random

tim = Turtle()
#tim.shape("turtle")
tim.color("DeepPink3")
tim.pensize(7)
tim.speed(10)

moves = ["left", "forward", "right"]


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def new_move():
    next = random.choice(moves)
    if next == "left":
        return tim.left(90)
    elif next == "right":
        return tim.right(90)
    elif next == "forward":
        return tim.forward(20)

for _ in range(300):
    new_move()
    change_color()

screen = Screen()
screen.exitonclick()
