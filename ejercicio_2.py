#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
# Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje:
# “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por telado
nombre = input("Introduce tu nombre: ")
direccion = input("Introduce tu direccion: ")
telefono = int(input("Introduce tu telefono: "))

Datos_personales = [nombre,direccion,telefono]

print("los datos personales son: ", Datos_personales)