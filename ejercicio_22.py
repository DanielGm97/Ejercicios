#Crear un programa que determine si un año es bisiesto o no.

año= int(input("introduce el año: "))

if (año%4==0 and año%100 !=0) or (año%400==0):
    print("es año bisiesto")
else:
    print("no es bisiesto")