import turtle
from random import randint

window = turtle.Screen()
window.bgcolor("black")
turtle.color("yellow")
turtle.speed(0)


def draw_star():
    turns = 5
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(145)
        turns -= 1
    turtle.end_fill()


num_stars = 0
while num_stars < 50:
    x = randint(-300, 300)
    y = randint(-300, 300)
    draw_star()

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Move the star horizontally
    turtle.setx(x + randint(-100, 100))  
    
    num_stars += 1

window.exitonclick()
