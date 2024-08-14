#Hacer un programa que calcule el área y el perímetro de un cuadrado con el lado ingresado por el usuario.

lado=float(input("Introduce el lado del cuadrado: "))

area = lado*lado
perimetro= lado *4 

print(f"dado el lado ingresado por el usuario{lado}\n\
El area es: {area}\nY el Perimetro es: {perimetro}")