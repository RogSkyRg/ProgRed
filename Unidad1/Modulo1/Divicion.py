#Nombre: Méndez fernandez Alan Eusebio
#Descripcion: Suma simple
#fecha: 11 de Septiembre 2024


data = input("")
x, y = data.split()
x = int(x)
y = int(y)

coc = x // y
res = x %  y

if res == 0:
    print(coc)
else:
    print(f"{coc} {res}/{y}")
