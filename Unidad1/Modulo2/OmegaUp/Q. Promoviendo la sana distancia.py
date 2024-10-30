"""
from collections import Counter

N = int(input())
telefonos = [input().strip() for _ in range(N)]
contador = Counter(telefonos)
max_count = max(contador.values())
primer_telefono = next(num for num in telefonos if contador[num] == max_count)
print(max_count, primer_telefono)
"""

"""
from collections import defaultdict

N = int(input())

frecuencias = defaultdict(int)

orden = []

for _ in range(N):
    telefono = input().strip()
    if frecuencias[telefono] == 0:
        orden.append(telefono)
    frecuencias[telefono] += 1

max_count = max(frecuencias.values())

primer_telefono = next(num for num in orden if frecuencias[num] == max_count)

print(max_count, primer_telefono)
"""

"""

from collections import defaultdict

def encontrar_telefono_mas_llamado():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    
    frecuencias = defaultdict(int)
    
    orden = []
    
    for i in range(1, N + 1):
        telefono = data[i]
        if frecuencias[telefono] == 0:
            orden.append(telefono)
        frecuencias[telefono] += 1
    
    max_count = max(frecuencias.values())
    
    primer_telefono = next(num for num in orden if frecuencias[num] == max_count)
    
    print(max_count, primer_telefono)

encontrar_telefono_mas_llamado()
"""


def telefono_mas_llamado(n, telefonos):
    conteo = {}
    
    for telefono in telefonos:
        if telefono in conteo:
            conteo[telefono] += 1
        else:
            conteo[telefono] = 1
    
    max_llamadas = 0
    telefono_mas_llamadas = None
    
    for telefono in telefonos:
        if conteo[telefono] > max_llamadas:
            max_llamadas = conteo[telefono]
            telefono_mas_llamadas = telefono
    
    return max_llamadas, telefono_mas_llamadas

n = int(input())  
telefonos = [int(input()) for _ in range(n)]  

llamadas, telefono = telefono_mas_llamado(n, telefonos)

print(llamadas, telefono)
