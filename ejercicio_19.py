#Crear un programa que determine si una palabra es un anagrama de otra.

palabra1= input("Introduce una palabra: ")
palabra2= input("Introduce otra palabra: ")

palabra1 = sorted(palabra1)
palabra2 = sorted(palabra2)

if palabra1==palabra2:
    print("es anagrama")
else:
    print("no es anagrama")
