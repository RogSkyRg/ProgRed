'''
N = int(input())

numeros = list(map(int, input().split()))

K = int(input())

numeros.sort()

posicion = 0
for numero in numeros:
    if numero == K:
        break
    posicion += 1

print(posicion)
'''
'''
def encontrar_posicion(numeros, k):
    numeros.sort()
    return numeros.index(k)

N = int(input())
numeros = list(map(int, input().split()))
k = int(input())
print(encontrar_posicion(numeros, k))
'''
'''
def encontrar_posicion(numeros, k):
    try:
        numeros.sort()
        return numeros.index(k)
    except ValueError:
        return -1

N = int(input())
numeros = list(map(int, input().split()))
k = int(input())
posicion = encontrar_posicion(numeros, k)
if posicion >= 0:
    print(posicion)
else:
    print("El elemento no está en la lista")
    '''


'''
N = int(input().strip())
conjunto = list(map(int, input().strip().split()))
K = int(input().strip())
conjunto_ordenado = sorted(conjunto)
posicion = conjunto_ordenado.index(K)
print(posicion)
'''
'''
try:
    N = int(input().strip())
    
    conjunto = list(map(int, input().strip().split()))
    
    K = int(input().strip())
    
    if len(conjunto) != N:
        raise ValueError("La cantidad de números en el conjunto no coincide con N.")
    
    if K not in conjunto:
        raise ValueError("El valor de K no está presente en el conjunto.")
    
    conjunto_ordenado = sorted(conjunto)
    
    posicion = conjunto_ordenado.index(K)
    
    print(posicion)

except ValueError as e:
    print(f"Error en los datos de entrada: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
'''

'''
def encontrar_posicion(n, conjunto, k):
  
  conjunto_ordenado = sorted(conjunto)
  for i in range(n):
    if conjunto_ordenado[i] == k:
      return i
  return -1

n = int(input())
conjunto = list(map(int, input().split()))
k = int(input())

posicion = encontrar_posicion(n, conjunto, k)

if posicion != -1:
  print(posicion)
else:
  print("El número K no se encuentra en el conjunto.")
'''
'''
def encontrar_posicion(n, conjunto, k):

  conjunto_ordenado = sorted(conjunto)
  for i in range(n):
    if conjunto_ordenado[i] == k:
      return i
  return -1  

n = int(input())
conjunto = list(map(int, input().split()))
k = int(input())

posicion = encontrar_posicion(n, conjunto, k)

if posicion != -1:
  print(posicion)
else:
  print("El número K no se encuentra en el conjunto.")
'''

def encontrar_posicion(n, conjunto, k):

  conjunto_ordenado = sorted(conjunto)
  for i in range(len(conjunto_ordenado)): 
    if conjunto_ordenado[i] == k:
      return i
  return -1  

n = int(input())
conjunto = list(map(int, input().split()))
k = int(input())

posicion = encontrar_posicion(n, conjunto, k)

if posicion != -1:
  print(posicion)
else:
  print("El número K no se encuentra en el conjunto.")
