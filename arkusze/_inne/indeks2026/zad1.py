import turtle

t = turtle.Turtle()
t.speed(2000)

def fig(odc):
    if  odc != 0:
        for i in range(4):
            t.forward(odc)
            t.left(90)
            fig(odc//3)

fig(90)
