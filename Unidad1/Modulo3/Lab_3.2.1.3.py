'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 3.2.1.3
Fecha: 30/10/2024
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while True:
    user_number = int(input("Introduce un número: "))  
    if user_number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break 
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")  