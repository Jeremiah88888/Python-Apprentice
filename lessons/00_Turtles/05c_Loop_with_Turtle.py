
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

import turtle
tina = turtle.Turtle()
turtle.setup(width=500,height=500)

tina.speed=1

distance = 100
sides = 3
angle = 360/sides

for i in range(sides):
    tina.forward(distance)
    tina.left(angle)

turtle.exitonclick()



