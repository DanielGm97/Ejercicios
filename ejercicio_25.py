#Hacer un programa que genere una lista de números primos dentro de un rango dado.

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def listar_primos(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

primos_en_rango = listar_primos(inicio, fin)
print("Números primos en el rango de", inicio, "a", fin, "son:", primos_en_rango)
