#Crear un programa que cuente cuántas palabras hay en un texto ingresado por el usuario.

#Esta línea solicita al usuario que ingrese un texto y lo almacena en la variable texto.
texto = input("Ingresa un texto: ")
#Se inicializa una variable contador en 0, la cual se utilizará para contar las palabras en el texto.
contador=0
#Se inicia un bucle for que recorre cada posición del texto ingresado por el usuario, haciendo uso de range(len(texto)).
for i in range(len(texto)):
    #: Dentro del bucle, se verifica si el carácter en la posición actual texto[i] es un espacio (" "). Si es así, el programa continúa con la siguiente iteración del bucle (con continue).
    if texto[i] == " ":
        continue
    # Se evalúa si el carácter actual está al principio de la cadena (i == 0) o si el carácter anterior era un espacio (texto[i-1] == " "). En caso de cumplirse alguna de estas condiciones, significa que se está en el inicio de una palabra.
    elif i == 0 or texto[i-1] == " ":
        #contador += 1: Si se cumple lo anterior, se incrementa en 1 el contador (que indica el inicio de una palabra).
        contador += 1

print(f"hay {contador} palabras ")


