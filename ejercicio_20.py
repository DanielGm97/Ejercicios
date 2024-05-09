#Hacer un programa que encuentre el mayor y el menor número de una lista dada.

milist=[]
n= int(input("cuantos numeros desea agregar a la lista: "))

for i in range(n):
     milist.append(int(input(print("Agrega numeros a la lista: "))))
     
print(f"el numero mayor es {max(milist)}")
print(f"el numero menor es {min(milist)}")

