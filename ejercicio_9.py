#. Desarrollar un programa que calcule el área de un círculo con un radio dado por el usuario
#Área de un círculo = π r² 
import math
radio=float(input("Introduce el radio del circulo:"))

area= math.pi*radio**2

print("el area del circulo es: " + str(area))

