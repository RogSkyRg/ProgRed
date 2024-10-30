"""
def es_numero_de_missa(n, k):
    digitos = [int(d) for d in str(n)]
    
    suma = sum(d**k for d in digitos)
    
    return suma == n

n, k = map(int, input().split())

if es_numero_de_missa(n, k):
    print("Simón Missa")
else:
    print("Nelpas mijo")

"""

def es_numero_de_missa(n, k):
    return sum(int(digito) ** k for digito in str(n)) == n

n, k = map(int, input().split())
print("Simón Missa" if es_numero_de_missa(n, k) else "Nelpas mijo")