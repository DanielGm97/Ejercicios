#Crear un programa que determine si un número es perfecto (la suma de sus divisores es igual al número original).

def numeroPerfecto():
    Perfecto=0
    num=int(input("ingresa un numero cualquiera: "))
    for i in range(1,num):
        if num % i == 0:
            Perfecto += i
    if Perfecto==num:
        print("el numero es perfecto")
    else:
        return"El Numero no es perfecto"
numeroPerfecto()