'''
def ordenar_concursantes():
    nombres = []
    
    while True:
        nombre = input().strip()
        if nombre == "#":
            break
        nombres.append(nombre)
    
    nombres.reverse()
    
    for nombre in nombres:
        print(nombre)

'''

nombres = []
nombre = input()

while nombre != "#":
    nombres.append(nombre)
    nombre = input()

nombres.reverse()  

for nombre in nombres:
    print(nombre)
