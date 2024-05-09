# Hacer un programa que cuente cuántas veces aparece una letra en un texto ingresado por el usuario.

texto= input("introduce una palabra o texto: ")
contador = 0 
letra = input("que letra desea contar? ")

for i in range(len(texto)):
    if texto[i] == letra:
        contador+=1
    elif [i]== " ":
        continue
    
print(f"la letra {letra} se repite:  {contador}")
#print("la letra " + letra + " se repite: " + str(contador))
