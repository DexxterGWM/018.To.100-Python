######## Challenge 1 - Draw a Square ############

from turtle import Turtle, Screen

# tim = Turtle()
timmy_the_turtle = Turtle()

# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()