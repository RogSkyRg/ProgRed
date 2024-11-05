
biblioteca = []

def agregar_libro(titulo,autor,año):

    if not titulo or not autor or not año:
        return "Error: Todos los campos son necesarios"
    
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            return "Error: El libro ya existe en la biblioteca"
    
    try:
        año = int(año)
    except ValueError:
        return "Error: el año debe ser un numero valido"

    libro = {
        'titulo': titulo,
        'autor': autor,
        'año': año
}
    biblioteca.append(libro)
    return "Libro agregado exitosamente"

def mostrar_libros():
    if not biblioteca:
        return "La biblioteca esta vacia"
    
    resultado = "\nLibros en la biblioteca:\n"
    for libro in biblioteca:
        resultado += f"Titulo: {libro['titulo']}\n"
        resultado += f"Autor: {libro['autor']}\n"
        resultado += f"Año: {libro['año']}\n"
        resultado += "-" * 30 + "\n"
    return resultado

def buscar_libro(titulo):

    if not titulo:
        return "Error: Debe ingresar un titulo"
    
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            return f"""
Libro encontrado:
Titulo: {libro['titulo']}
Autor: {libro['autor']}
Año: {libro['año']}"""
        
        return "Error: Libro no encontrado en la biblioteca"
    
def eliminar_libro(titulo):

    if not titulo:
        return "Error: Debe ingresr un titulo para eliminar"
    
    for i, libro in enumerate(biblioteca):
        if libro['titulo'].lower() == titulo.lower():
            biblioteca.pop(i)
            return "Error: Libro no encontrado"
        
    return "Error: Libro no encontrado en la biblioteca"

def menu_principal():

    while True:
        print("\n== GESTION DE LA BILIOTECA ==")
        print("1. Agrregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Salir")

        opcion = input("\nSeleccione una opcion del 1 al 5: ")

        if opcion == "1":
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingresa el autor del libro: ")
            año = input("Ingrese el año de la publicacion: ")
            print(agregar_libro(titulo, autor, año))

        elif opcion == "2":
            print(mostrar_libros())

        elif opcion == "3":
            titulo = input("Ingrese el titulo del libro: ")
            print(buscar_libro(titulo))

        elif opcion == "4":
            titulo = input("Ingrese el titulo del libro a eliminar: ")
            print(eliminar_libro(titulo))

        elif opcion == "5":
            print("Biblioteca de Alan Mendez")
            break

        else:
            print("Opcion no valida. Por favor, selecciona una opcion del 1 al 5")

if __name__== "__main__":
    menu_principal()

            