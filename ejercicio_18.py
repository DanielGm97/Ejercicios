#. Desarrollar un programa que calcule el área de un triángulo con los lados ingresados por el usuario.
#formula usada: Formula de Herón
from math import sqrt
lado1= int(input("Ingresa lado 1: "))
lado2= int(input("Ingresa lado 2: "))
lado3= int(input("Ingresa lado 3: "))

p= (lado1+lado2+lado3)/2

Area= sqrt(p*(p-lado1)*(p-lado2)*(p-lado3))

print(f"el area del Triangulo es: {Area}")