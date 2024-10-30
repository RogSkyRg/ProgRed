'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.6.1.9
Fecha: 30/10/2024
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("La lista con elementos únicos:")
print(unique_list)