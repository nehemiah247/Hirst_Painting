import turtle
import turtle as turtle_module
import random
team = turtle_module.Turtle()
team.speed("fastest")
team.penup()
team.hideturtle()
turtle_module.colormode(255)
color_list = [(216, 154, 113), (131, 172, 196), (215, 130, 150), (223, 70, 91), (236, 211, 104), (25, 121, 157), (124, 178, 152), (36, 125, 89), (28, 169, 197), (235, 163, 178), (221, 85, 73), (142, 82, 59), (156, 63, 84), (239, 167, 154), (172, 151, 69), (56, 163, 133), (163, 208, 181), (27, 54, 75), (150, 208, 218), (175, 185, 218), (7, 88, 106), (26, 92, 64), (235, 214, 9), (102, 122, 173), (51, 58, 91), (24, 72, 39)]

team.setheading(225)
team.forward(300)
team.setheading(0)

number_of_dots = 100

for i in range(1, number_of_dots + 1):
    team.dot(20, random.choice(color_list))
    team.forward(50)

    if i % 10 == 0:
        team.setheading(90)
        team.forward(50)
        team.setheading(180)
        team.forward(500)
        team.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()