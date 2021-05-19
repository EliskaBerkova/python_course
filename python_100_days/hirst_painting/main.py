import colorgram

rgb_colors = []
colors = colorgram.extract("damien-hirst-the-complete-spot-paintings-1986-2011-39.jpg", 25)

# vypsani seznamu barev - moje varianta
# for color in colors:
#     rgb = color.rgb
#     barvy = tuple(rgb)
#     rgb_colors.append(barvy)
# print(rgb_colors)

# vypsani seznamu barev - dalsi moznost
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

color_list = [(221, 231, 236), (235, 36, 109), (144, 29, 66), (238, 75, 36), (8, 147, 94), (230, 167, 43), (184, 158, 48), (45, 191, 231), (29, 127, 193), (126, 192, 75), (253, 223, 0), (85, 29, 92), (247, 220, 40), (171, 41, 97), (31, 168, 120), (208, 133, 166), (201, 59, 39), (146, 28, 27), (242, 164, 198), (243, 167, 155), (26, 185, 225), (158, 213, 179)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

for row in range(10):
    tim.hideturtle()
    tim.penup()
    tim.goto(-230, -230 + row * 50)
    tim.pendown()

    for dots in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()

