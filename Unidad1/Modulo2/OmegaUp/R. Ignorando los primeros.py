

N = int(input())

arreglo = list(map(int, input().split()))

K = int(input())

subarreglo = arreglo[K:]

print(' '.join(map(str, subarreglo)))