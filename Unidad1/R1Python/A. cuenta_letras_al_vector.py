##cadena = input("Ingresa la cadena: ")
##contador = [0] * 26  
##for letra in cadena:
##    contador[ord(letra) - ord('a')] += 1
##print(*contador)  
##for i in range(26):
##    if contador[i] > 0:
##        print(f"La letra {chr(i + ord('a'))} aparece {contador[i]} veces")



def contar_letras(cadena):
    conteo_letras = {chr(letra): 0 for letra in range(ord('a'), ord('z') + 1)}
    
    for letra in cadena:
        if letra in conteo_letras:
            conteo_letras[letra] += 1
    
    conteo_en_orden = [conteo_letras[chr(letra)] for letra in range(ord('a'), ord('z') + 1)]
    print(" ".join(map(str, conteo_en_orden)))
    
    for letra, conteo in conteo_letras.items():
        if conteo > 0:
            print(f"La letra {letra} aparece {conteo} veces")