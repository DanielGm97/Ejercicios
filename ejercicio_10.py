#Hacer un programa que determine si un número es par o impar.

num= int(input("Introduce un numero: "))

if num % 2==0:
    print(str(num) + " es par")
else:
    print(str(num) + "es impar")