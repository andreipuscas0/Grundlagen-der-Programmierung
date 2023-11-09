import turtle

t = turtle.Pen()


def bigrtk():
    t.reset()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.up()


def smallrtk():
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)


def draw():
    bigrtk()
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(30)
    t.down()
    smallrtk()


draw()
