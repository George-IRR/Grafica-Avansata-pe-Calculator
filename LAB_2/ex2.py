from graphics import *

def drawCircle(win, center, radius, color):
    c = Circle(center, radius)
    c.setFill(color)
    c.draw(win)
    
def main():
    win = GraphWin("My Circle", 300, 250)
    drawCircle(win, Point(150, 155), 50, "red")

    drawCircle(win, Point(200, 180), 50, "blue")
    drawCircle(win, Point(230, 50), 50, "green")

    win.getMouse()
    win.close()

main()

