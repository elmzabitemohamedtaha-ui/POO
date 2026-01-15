import turtle
import math


t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

screen = turtle.Screen()
screen.bgcolor("black")
t.color("#FF2D75")  


def heart_x(k):
    return 16 * math.sin(k)**3

def heart_y(k):
    return (13 * math.cos(k)
            - 5 * math.cos(2*k)
            - 2 * math.cos(3*k)
            - math.cos(4*k))

for i in range(0, 628):   
    k = i / 100
    x = heart_x(k) * 12
    y = heart_y(k) * 12

    t.penup()
    t.goto(0, 0)       
    t.pendown()
    t.goto(x, y)        

turtle.done()