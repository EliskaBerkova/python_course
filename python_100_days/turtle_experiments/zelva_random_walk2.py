import turtle as t
import random

tim = t.Turtle()
#tim.color("DeepPink3")
tim.pensize(7)
tim.speed(10)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.forward(20)
    tim. setheading(random.choice(directions))
    tim.color(random_color())



screen = t.Screen()
screen.exitonclick()