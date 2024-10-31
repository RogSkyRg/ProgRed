'''
N = int(input())  

elementos = list(map(int, input().split()))  

elementos.sort()  

print(*elementos)  


Print( int (input))
'''
'''
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers)
'''
'''
def ordenar_numeros(numeros):
    try:
        numeros.sort()
        return numeros
    except (ValueError, TypeError):
        return None

N = int(input())
numeros = list(map(int, input().split()))
resultado = ordenar_numeros(numeros)
if resultado is not None:
    print(*resultado)
else:
    print("Error en los datos de entrada")
'''
'''
N = int(input().strip())
numeros = list(map(int, input().strip().split()))
numeros_ordenados = sorted(numeros)
print(" ".join(map(str, numeros_ordenados)))
'''

N = int(input().strip())

if N == 0:
    print("")  
else:
    numeros = list(map(int, input().strip().split()))

    numeros_ordenados = sorted(numeros)

    print(" ".join(map(str, numeros_ordenados)))
