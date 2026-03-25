import turtle
import time

turtle.bgcolor("white")
turtle.pensize(3)
turtle.speed(0)

def createSquare():
    for _ in range(5):
        for colors in ["red", "blue", "magenta", "green", "yellow", "grey", "black", "pink"]:
            turtle.color(colors)
            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)
            turtle.left(10)
    
    time.sleep(2) 
    turtle.clear()

def createCircle():
    for _ in range(5):
        for colors in ["red", "blue", "magenta", "green", "yellow", "grey", "black", "pink"]:
            turtle.color(colors)
            turtle.circle(50)
            turtle.left(10)
    
    turtle.hideturtle()


createSquare()
createCircle()


turtle.done()