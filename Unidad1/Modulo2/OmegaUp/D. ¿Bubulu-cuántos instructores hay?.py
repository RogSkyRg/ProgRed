def contar_instructores(nombres):
    return len(nombres.split())

nombres = input()  
cantidad_instructores = contar_instructores(nombres)
print(cantidad_instructores)
