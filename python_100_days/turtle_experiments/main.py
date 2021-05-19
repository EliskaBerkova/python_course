from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.color("DeepPink3")
import random
#ctverec
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#prerusovana cara
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

for num_sides in range(3,11):
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)
    change_color()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     change_color()
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()

