from graphics import *

def main():
    win = GraphWin("My Circle", 300, 250)
    g = Point(150, 150)
    g.draw(win)
    win.getMouse()
    win.close()

main()