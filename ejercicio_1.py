#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.
valor1=int(input("ingresa el primer numero: "))
valor2=int(input("ingresa el segundo numero: "))

def devuelvemax ():
    if valor1>valor2:
        print("El primer numero es mayor.")
    else: 
        valor1<valor2
        print("El segundo numero es mayor.")

devuelvemax()