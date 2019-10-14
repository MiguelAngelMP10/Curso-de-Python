import math
import turtle as t


def fractal(n):
    t.setup(500, 500)
    t.title("copo de nieve :3")
    t.left(180)
    z = (360/n)
    t.up()
    t.fd(10)
    t.down()
    for c in range(n):

        t.right(90)
# Primero
        t.fd(35)
        t.left(45)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(20)
        t.left(135)
        t.fd(30)
# Segundo
        t.left(45)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(20)
        t.left(135)
        t.fd(30)
# Tercero
        t.left(45)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(20)
        t.left(135)
# Esquina
        t.fd(40)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(40)
# Primero2
        t.left(135)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(30)
        t.left(45)
# Segundo2
        t.fd(30)
        t.left(135)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(30)
        t.left(45)
# Tercero2
        t.fd(30)
        t.left(135)
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)
        t.fd(30)
        t.left(45)
        t.fd(35)

        t.left(90)
        t.left(z)


fractal(8)
t.exitonclick()
