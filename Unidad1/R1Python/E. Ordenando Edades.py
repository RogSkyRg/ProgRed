'''
N = int(input())  

edades = []  
for i in range(N):
    edad = int(input())
    edades.append(edad)

edades.sort()

for edad in edades:
    print(edad, end=" ")
'''

'''
n = int(input())  
edades = []  

for i in range(n):
    edad = int(input())
    edades.append(edad)

edades.sort()

for edad in edades:
    print(edad)
'''
'''
n = int(input())  
edades = []  

for i in range(n):
    edad = int(input())  
    edades.append(edad)  

edades_ordenadas = sorted(edades)  

for edad in edades_ordenadas:
    print(edad)  
'''

'''
def ordenar_edades(N, edades):
    frecuencia = [0] * 101
    
    for edad in edades:
        frecuencia[edad] += 1
    
    resultado = []
    for edad in range(1, 101):
        if frecuencia[edad] > 0:
            resultado.extend([edad] * frecuencia[edad])
    
    print(" ".join(map(str, resultado)))
'''

'''
def ordenar_edades(N, edades):
    frecuencia = [0] * 101  
    
    for edad in edades:
        if 1 <= edad <= 100:
            frecuencia[edad] += 1
        else:
            raise ValueError("La edad debe estar entre 1 y 100.")
    
    resultado = []
    for edad in range(1, 101):  
        resultado.extend([edad] * frecuencia[edad])
    
    print(" ".join(map(str, resultado)))
'''

'''
def sort_ages(ages):
    ages.sort()
    return ages

N = int(input())
ages = [int(input()) for _ in range(N)]
print(*sort_ages(ages))
'''
'''
N = int(input())
ages = []

for _ in range(N):
    age = int(input())
    if 1 <= age <= 100:
        ages.append(age)

ages.sort()
print(*ages)
'''
'''
N = int(input())
edades = list(map(int, input().split()))
if len(edades) != N:
    print("Error: se esperaban", N, "edades.")
else:
    edades.sort()
    print(" ".join(map(str, edades)))
'''

'''
N = int(input())
edades = list(map(int, input().split()))

if len(edades) != N:
    print(f"Error: se esperaban {N} edades, pero se recibieron {len(edades)}")
else:
    edades.sort()
    print(" ".join(map(str, edades)))
'''

'''
N = int(input())
edades = list(map(int, input().split()))

if len(edades) != N:
    print(f"Error: se esperaban {N} edades, pero se recibieron {len(edades)}")
else:
    edades.sort()
    print(*edades)
'''


'''
N = int(input().strip())

edades = list(map(int, input().strip().split()))

if len(edades) != N:
    print(f"Error: se esperaban {N} edades, pero se recibieron {len(edades)}")
else:
    edades.sort()
    
    print(" ".join(map(str, edades)))
'''

'''
##Progama al 93%
import sys
input = sys.stdin.read

datos = input().split()
N = int(datos[0])  
edades = map(int, datos[1:]) 

conteo_edades = [0] * 101

for edad in edades:
    conteo_edades[edad] += 1

resultado = []
for edad in range(1, 101):
    if conteo_edades[edad] > 0:
        resultado.extend([str(edad)] * conteo_edades[edad])

sys.stdout.write(" ".join(resultado) + "\n")
'''
'''
import sys
input = sys.stdin.read

datos = input().split()
N = int(datos[0])  
edades = map(int, datos[1:])  

conteo_edades = [0] * 101

for edad in edades:
    conteo_edades[edad] += 1

for edad in range(1, 101):
    if conteo_edades[edad] > 0:
        sys.stdout.write((f"{edad} " * conteo_edades[edad]).strip() + " ")
'''
'''
import sys
input = sys.stdin.read

datos = input().split()
N = int(datos[0])  
edades = map(int, datos[1:])  

conteo_edades = [0] * 101

for edad in edades:
    conteo_edades[edad] += 1

output = sys.stdout.write
for edad in range(1, 101):
    if conteo_edades[edad] > 0:
        output((f"{edad} " * conteo_edades[edad]).strip() + "\n")
'''

import sys

input = sys.stdin.read

datos = input().split()
N = int(datos[0])  
edades = map(int, datos[1:])  

conteo_edades = {}

for edad in edades:
    if edad in conteo_edades:
        conteo_edades[edad] += 1
    else:
        conteo_edades[edad] = 1

output = sys.stdout.write
for edad in range(1, 101):
    if edad in conteo_edades:
        output((f"{edad} " * conteo_edades[edad]).strip() + "\n")
