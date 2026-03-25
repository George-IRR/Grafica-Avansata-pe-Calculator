import turtle as tu


roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern - Fast Animation")


wn.tracer(50, 0) 
roo.hideturtle() 
roo.speed(0)

def draw_fractal(l, ratio, color, pensize):
    """Funcție universală de desenare"""
    if l < 10:
        return
    else:
        roo.pensize(pensize)
        roo.pencolor(color)
        roo.forward(l)
        roo.left(30)
        draw_fractal(ratio * l, ratio, color, pensize)
        roo.right(60)
        draw_fractal(ratio * l, ratio, color, pensize)
        roo.left(30)
        roo.backward(l)


tasks = [
    (20, 3/4, "yellow", 2), (20, 3/4, "magenta", 2), (20, 3/4, "red", 2), (20, 3/4, "#FFF8DC", 2),
    (40, 4/5, "lightgreen", 3), (40, 4/5, "red", 3), (40, 4/5, "yellow", 3), (40, 4/5, "#FFF8DC", 3),
    (60, 6/7, "cyan", 2), (60, 6/7, "yellow", 2), (60, 6/7, "magenta", 2), (60, 6/7, "#FFF8DC", 2)
]

roo.left(90)


for length, ratio, col, size in tasks:
    draw_fractal(length, ratio, col, size)
    roo.right(90)
    
    wn.update() 

print("Desen finalizat!")
wn.exitonclick()