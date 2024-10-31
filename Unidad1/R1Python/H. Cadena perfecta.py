'''
from collections import Counter

def contar_y_ordenar(cadena):
    contador = Counter(cadena)
    
    caracteres_ordenados = sorted(contador.keys())
    
    resultado = ""
    for caracter in caracteres_ordenados:
        resultado += f"{contador[caracter]}{caracter}"
    
    print(resultado)
    '''

palabra = input()
frecuencias = {}
for caracter in palabra:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

caracteres_ordenados = sorted(frecuencias.keys())
salida = ""
for caracter in caracteres_ordenados:
    salida += f"{frecuencias[caracter]}{caracter}"

print(salida)
