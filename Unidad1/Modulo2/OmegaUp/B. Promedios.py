def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) // len(calificaciones)
    return promedio

calificaciones = list(map(int, input().split()))
promedio = calcular_promedio(calificaciones)
print(promedio)
