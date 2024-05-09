#Desarrollar un programa que calcule la raíz cuadrada de un número ingresado por el usuario.
from math import isqrt as ra

numero=int(input("Ingresa un numero para calcular su raiz cuadrada: "))

raiz = ra(numero)

print("la raiz cuadrada de " + str(numero) + " es: " + str(raiz))
