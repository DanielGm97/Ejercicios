# Desarrollar un programa que sume los dígitos de un número ingresado por el usuario.

def ingresa_digitos():
    calculo = (input("introduce digitos: "))
    suma=0
   
    for i in calculo:
        suma+=int(i)
    return suma

resultado=ingresa_digitos()

print(f"El resultado de la suma es: {resultado}")