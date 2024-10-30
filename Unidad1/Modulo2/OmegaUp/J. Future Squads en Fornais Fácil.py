def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinaciones(n, r):
    if n < r:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def calcular_squads(nombres):
    nombres_validos = [nombre for nombre in nombres if nombre != "Ricardo" and nombre != "Mirón"]
    
    n = len(nombres_validos)
    
    if n < 4:
        return 0
    
    return combinaciones(n, 4)

nombres = input().split()

print(calcular_squads(nombres))
