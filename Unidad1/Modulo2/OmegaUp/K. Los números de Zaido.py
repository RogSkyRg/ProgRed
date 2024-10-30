def factores_primos(n):
    factores = {}
    divisor = 2
    while n % divisor == 0:
        if divisor in factores:
            factores[divisor] += 1
        else:
            factores[divisor] = 1
        n //= divisor

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            if divisor in factores:
                factores[divisor] += 1
            else:
                factores[divisor] = 1
            n //= divisor
        divisor += 2
    
    if n > 1:
        factores[n] = 1
    
    return factores

def es_numero_de_zaido(n):
    factores = factores_primos(n)
    
    suma_factores = sum(p ** e for p, e in factores.items())
    
    if n % suma_factores == 0:
        return "A wilson Zaido"
    else:
        return "Chaaale"

n = int(input())

print(es_numero_de_zaido(n))
