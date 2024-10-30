'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.4.1.13
Fecha: 30/10/2024
'''
beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for miembro in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(miembro)
print("Paso 3:", beatles)

del beatles[-1]  
del beatles[-1]  
print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

print("Los Beatles favoritos:", len(beatles))