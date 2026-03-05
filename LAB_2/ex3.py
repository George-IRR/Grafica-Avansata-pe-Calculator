from graphics import *

def fromPointSquare(win, x_center, y_center,dimension):
    x_half = x_center / 2
    y_half = y_center / 2
    p1 = Point(x_half, y_half)
    p2 = Point(x_half + dimension, y_half + dimension)
    c = Rectangle(p1,p2)
    c.draw(win)


def main():
    win = GraphWin("My Graph", 500, 500)
    fromPointSquare(win, 150, 200, 50)

    fromPointSquare(win, 300, 50, 150)
    win.getMouse()
    win.close()

main()

