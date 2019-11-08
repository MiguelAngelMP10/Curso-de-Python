import math
import turtle


def fractal(n):
    turtle.setup(500, 500)
    turtle.title("copo de nieve :3")
    turtle.left(180)
    z = (360/n)
    turtle.up()
    turtle.fd(10)
    turtle.down()
    for c in range(n):

        turtle.right(90)
# Primero
        turtle.fd(35)
        turtle.left(45)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(20)
        turtle.left(135)
        turtle.fd(30)
# Segundo
        turtle.left(45)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(20)
        turtle.left(135)
        turtle.fd(30)
# Tercero
        turtle.left(45)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(20)
        turtle.left(135)
# Esquina
        turtle.fd(40)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(40)
# Primero2
        turtle.left(135)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(30)
        turtle.left(45)
# Segundo2
        turtle.fd(30)
        turtle.left(135)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(30)
        turtle.left(45)
# Tercero2
        turtle.fd(30)
        turtle.left(135)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(30)
        turtle.left(45)
        turtle.fd(35)

        turtle.left(90)
        turtle.left(z)

 
fractal(8)
turtle.exitonclick()
