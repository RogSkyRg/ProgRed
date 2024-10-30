from collections import Counter

def contar_edades(edades):
    conteo_edades = Counter(edades)
    
    edades_ordenadas = sorted(conteo_edades.items())
    
    for edad, cantidad in edades_ordenadas:
        print(edad, cantidad)

n = int(input())  
edades = list(map(int, input().split()))  

contar_edades(edades)
