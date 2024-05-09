#	Hacer un programa que calcule el área y el volumen de una esfera con el radio ingresado por el usuario.
import math


radio= float(input("introduce el radio de la esfera: "))

volumen= 4/3*math.pi * radio**3
area= 4*math.pi * radio**2

print(f"el volumen es: {volumen} y el area es: {area}")