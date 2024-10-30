import math

def resolver_ecuacion(A, B, C):
    discriminante = B**2 - 4 * A * C
    
    x1 = (-B + math.sqrt(discriminante)) / (2 * A)
    x2 = (-B - math.sqrt(discriminante)) / (2 * A)
    
    return x1, x2

A, B, C = map(int, input().split())
solucion1, solucion2 = resolver_ecuacion(A, B, C)
print(solucion1, solucion2)
