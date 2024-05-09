#Crear un programa que genere la sucesión de Fibonacci hasta un número dado.
num=int(input("ingresa un numero "))
a=0
b=1
fibo=[]

for i in range(num):
    fibo.append(a)
    a,b = b,a+b
    
print(f"la sucecion es {fibo}")