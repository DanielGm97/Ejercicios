#Crear un programa que genere una lista de números pares dentro de un rango dado.
def lista_par():
    num=int(input("ingresa un numero: "))
    lista=[]
    for i in range(num):
        if i %2!=0:
            continue
        else:
            lista.append(i)
        
    print(lista)
            

lista_par()

