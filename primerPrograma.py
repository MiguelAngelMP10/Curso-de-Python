import turtle
lado = 50
numeroLado = 1
angulo = 360/numeroLado
window = turtle.Screen()
tortuga = turtle.Turtle()

for x in range(numeroLado):
    tortuga.forward(lado)
    tortuga.left(angulo)

turtle.mainloop()
