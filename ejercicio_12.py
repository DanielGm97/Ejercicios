#Desarrollar un programa que calcule el máximo común divisor de dos números

a= float(input("ingresa un numero: "))
b= float(input("ingresa otro numero: "))

def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

mcd= euclides(a,b)
print("el maximo comun divisor es:" + str(mcd))