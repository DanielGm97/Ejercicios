from math import pi
#Desarrollar un programa que calcule el área y el perímetro de un círculo con el radio ingresado por el usuario.

radio=float(input("Introduce el radio del circulo: "))

area= pi* radio**2

perimetro= 2* pi * radio

print(f"De acuerdo al radio ingresado por el usuario {radio}\n\
El area del circulo es: {area:.2f}\nY el perimetro es: {perimetro:.2f}")


