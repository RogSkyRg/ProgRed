def es_capicua(n):
    return str(n) == str(n)[::-1]

def inverso(n):
    return int(str(n)[::-1])

def encontrar_capicua(n):
    while not es_capicua(n):
        n = n + inverso(n)
    return n

n = int(input())

print(encontrar_capicua(n))
