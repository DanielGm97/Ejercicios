#calculadora basica

def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2== 0 or num1== 0:
        print("no se puede dividir entre cero")
    else:
        num1/num2

print("Calculadora basica")

num1= float(input("introduce el primer numero: "))
num2= float(input("introduce el segundo numero: "))

operacion = input("Elige una operación (+, -, *, /): ")

if operacion == "+":
    resultado = suma(num1,num2)
elif operacion =="-":
    resultado = resta(num1,num2)
elif operacion =="*":
    resultado = multiplicacion(num1,num2)
elif operacion == "/":
    resultado = division(num1,num2)

else:
    print("operacion ingresada no es valida!")

print(resultado)