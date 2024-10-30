def es_permutacion(n, conjunto_a, conjunto_b):
    conjunto_a.sort()
    conjunto_b.sort()
    
    if conjunto_a == conjunto_b:
        print("SI")
    else:
        print("NO")

n = int(input().strip())
conjunto_a = list(map(int, input().strip().split()))
conjunto_b = list(map(int, input().strip().split()))

es_permutacion(n, conjunto_a, conjunto_b)
