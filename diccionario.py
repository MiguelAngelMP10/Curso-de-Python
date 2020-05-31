# -*- coding: utf-8 -*-

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

for key in calificaciones:
    print(key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():

    print('llave: {}, valor: {}'.format(key, value))

suma_de_calificaciones = 0
for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

promedio_calificaciones = suma_de_calificaciones / len(calificaciones.values())

print(promedio_calificaciones)
