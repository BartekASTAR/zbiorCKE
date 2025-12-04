import turtle

t = turtle.Turtle()
t.speed(0)

def sierpinski(odcinek):
    if odcinek < 10:
        return
    for _ in range(3):
        t.forward(odcinek)
        t.left(120)
        sierpinski(odcinek // 2)


sierpinski(300)

turtle.exitonclick()