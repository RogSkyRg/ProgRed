'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.2.1.10
Fecha: 30/10/2024
'''

user_word = input("Introduce una palabra: ").upper()

for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    print(letter)