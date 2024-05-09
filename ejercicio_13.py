# Hacer un programa que determine si una palabra es un palíndromo o no.
palabra = input("ingresa una palabra: ")

if palabra == palabra[::-1]:
     print("es un palindromo")
else:
    print("no es un palindromo")