import turtle

turtle.Screen().bgcolor("Green")
pen = turtle.Turtle()

# first triangle of the star
for i in range(3):
    pen.forward(100) # draw base 
    pen.left(120)

pen.penup()
pen.right(30)
pen.forward(50)

# second triangle of the star
pen.pendown()
pen.left(90)
for i in range(3):
    pen.forward(100) # draw base
    pen.left(120)

turtle.done()