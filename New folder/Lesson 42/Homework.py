import turtle 

turtle.Screen().bgcolor("Green")
pen=turtle.Turtle()

pen.penup()
pen.left(180)
pen.forward(200)
pen.left(180)
pen.pendown()

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.penup()
pen.forward(200)
pen.pendown()

for i in range(6):
    pen.forward(50)
    pen.left(60)

pen.penup()
pen.forward(150)
pen.pendown()

for i in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)

turtle.done()