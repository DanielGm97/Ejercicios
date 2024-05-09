#Crear un programa que convierta grados Celsius a Fahrenheit y viceversa.

#Grados centígrados = (grados Fahrenheit − 32) × 5/9. Grados Fahrenheit = (grados centígrados × 9/5) +32.



grados= float(input("Introduce los grados que desea convertir: "))

Celcius= (grados - 32) * 5/9

Fahrenheit= (grados*9/5) +32

print("¿que operacion desea realizar? \n 1-Convertir grados Celsius a fahrenheit 2-Convertir grados fahrenheit a Celsius  ")
operacion = int(input())
if operacion == 1:
  print("Los grados Celcius " + str(grados) +  " a Farenheit son : " + str(Fahrenheit))
elif operacion == 2:
    print("Los grados Farenheit " + str(grados) +  " a Celsius son : " + str(Celcius))
else:
    print("operacion no contemplada")