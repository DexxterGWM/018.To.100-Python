########### Challenge 5 - Spirograph ########

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

screen = t.Screen()
screen.exitonclick()