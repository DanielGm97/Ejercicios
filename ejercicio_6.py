#. Crear un programa que calcule la factorial de un número ingresado por el usuario
from math import factorial

num= int(input("ingresa un numero: "))
fact= factorial(num)

print("EL factorial de " + str(num) + " es: " + str(fact)) 
