from collections import Counter

def contar_y_ordenar(cadena):
    contador = Counter(cadena)
    
    caracteres_ordenados = sorted(contador.keys())
    
    resultado = ""
    for caracter in caracteres_ordenados:
        resultado += f"{contador[caracter]}{caracter}"
    
    print(resultado)