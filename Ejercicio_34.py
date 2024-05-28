#Desarrollar un programa que calcule el producto escalar de dos vectores ingresados por el usuario.
def Producto_Escalar():
    vector1=input(("Ingresa los 3 valores del Vector 1 separados por comas:"))
    valor=vector1.split(",")
    a1=int(valor[0])
    a2=int(valor[1])
    a3=int(valor[2])
    
    vector2=input(("Ingresa los 3 valores del Vector 2 separados por comas:"))
    valor2=vector2.split(",")
    b1=int(valor2[0])
    b2=int(valor2[1])
    b3=int(valor2[2])
    
    productoEscalar= (a1*b1)+(a2*b2)+(a3*b3)
    
    print(f"El producto escalar de los dos vectores es: {productoEscalar}")

Producto_Escalar()    