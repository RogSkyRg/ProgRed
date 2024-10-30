'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.2.1.15
Fecha: 30/10/2024
'''
c0 = int(input("Ingresa un número natural: "))

pasos = 0

while c0 != 1:
    if c0 % 2 == 0:  
        c0 = c0 // 2
    else:  
        c0 = 3 * c0 + 1
    print(c0)  
    pasos += 1 

print("pasos =", pasos)