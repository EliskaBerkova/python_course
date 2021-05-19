from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.hideturtle()
    tim.home()
    tim.showturtle()

def turn_left():
    tim.left(10)


def turn_right():
    tim. right(10)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clear_screen, "c")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.exitonclick()