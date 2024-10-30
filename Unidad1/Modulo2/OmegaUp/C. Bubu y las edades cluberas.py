def edades_ordenadas(lista_edades):
    edades_distintas = sorted(set(map(str, lista_edades)), reverse=True)
    return edades_distintas

edades = list(map(int, input().split()))
resultado = edades_ordenadas(edades)
print(resultado)
