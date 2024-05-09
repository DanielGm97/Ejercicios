#. Hacer un programa que calcule el área y el perímetro de un rectángulo con los lados ingresados por el usuario.
print("recuerda! los lados de un rectangulo son pararelos entre si")
lado_izq= float(input("introduce el lado izquierdo: "))
lado_der= float(input("introduce el lado derecho: "))
lado_inf= float(input("introduce el lado inferior: "))
lado_sup= float(input("introduce el lado superior: "))

area = lado_der*lado_inf
perimetro = lado_izq+lado_der+lado_sup+lado_inf

print( f"El area del rectangulo es: {area} y el perimetro es: {perimetro}")