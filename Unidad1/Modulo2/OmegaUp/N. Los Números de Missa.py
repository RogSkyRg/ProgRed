def es_numero_de_missa(n, k):
    digitos = [int(d) for d in str(n)]  
    suma = sum(d**k for d in digitos)   
    return suma == n                    

def encontrar_grado_de_missa(n):
    k = 1  
    while True:
        digitos = [int(d) for d in str(n)]
        suma = sum(d**k for d in digitos)
        
        if suma == n:
            return k  
        elif suma > n:
            return -1  
        
        k += 1 

n = int(input())

print(encontrar_grado_de_missa(n))
