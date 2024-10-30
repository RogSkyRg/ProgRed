'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.2.1.11
Fecha: 30/10/2024
'''
word_without_vowels = ""

user_word = input("Introduce una palabra: ").upper()

for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    word_without_vowels += letter

print(word_without_vowels)