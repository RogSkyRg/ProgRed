"""
def determinar_par_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

numero = int(input())  
determinar_par_impar(numero)

"""

def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return "SI"
    else:
        return "NO"

palabra = input().strip()  

print(es_palindromo(palabra))
