objetos_recogidos = []

try:
    objeto = input("Ingresa el nombre del objeto que quieres recoger: ")
    if objeto in objetos_recogidos:
        raise ValueError("Ya has recogido este objeto.")
    objetos_recogidos.append(objeto)
    print("¡Has recogido", objeto, "!")
except ValueError as error:
    print("Error:", error)
