n = int(input())
numeros = list(map(int, input().split()))

numeros.sort()

indice_mediana = n // 2

print(numeros[indice_mediana], indice_mediana)
