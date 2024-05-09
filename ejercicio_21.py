#Desarrollar un programa que calcule el promedio de una lista de números.

lista=[]

num= int(input("agrega la cantidad de numero que desees sacar el promedio: "))

for i in range (num):
    lista.append(int(input("introduce un numero: ")))

promedio = sum(lista)/ num

print(f"el promedio es: {promedio}")
    