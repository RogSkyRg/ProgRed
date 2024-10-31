'''
n = int(input())
numeros = list(map(int, input().split()))

numeros.sort()

indice_mediana = n // 2

print(numeros[indice_mediana], indice_mediana)
'''
'''
n = int(input())
a = list(map(int, input().split()))

a.sort()

indice_mediana = (n - 1) // 2

print(a[indice_mediana], indice_mediana)
'''
'''
n = int(input())
a = list(map(int, input().split()))

a.sort()

if n % 2 == 0: 
    indice_mediana1 = (n // 2) - 1
    indice_mediana2 = n // 2
    mediana = (a[indice_mediana1] + a[indice_mediana2]) / 2
    print(mediana, indice_mediana1, indice_mediana2)
else: 
    indice_mediana = (n - 1) // 2
    print(a[indice_mediana], indice_mediana)
'''
'''
def mediana(N, A):
    enumerated_A = [(A[i], i) for i in range(N)]
    
    enumerated_A.sort()
    
    mediana_valor, mediana_indice = enumerated_A[N // 2]
    
    print(mediana_valor, mediana_indice)
'''

'''
def median(A):
    A.sort()
    n = len(A)
    mid = n // 2
    if n % 2 == 0:
        median = (A[mid-1] + A[mid]) / 2
    else:
        median = A[mid]
    return median, mid
    '''


'''
def encontrar_mediana(A):
    A.sort()
    n = len(A)
    
    if n == 0:
        return None, None
    
    medio = n // 2
    
    if n % 2 == 0:
        mediana = (A[medio-1] + A[medio]) / 2
        return mediana, medio
    else:
        return A[medio], medio
'''

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
indice_medio = N // 2

mediana = sorted_A[indice_medio]
indice_original = A.index(mediana)

print(mediana)
print(indice_original)