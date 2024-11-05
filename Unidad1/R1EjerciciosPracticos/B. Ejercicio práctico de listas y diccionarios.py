escuela =[]

def agregar_estudiantes(nombre, carrera, edad, numero_control):

    if not nombre or not carrera or not edad or not numero_control:
        return "Error: El estudiante ya existe en la base de datos"
    
    try:
        edad = int(edad)
        if edad < 0 or edad > 120:
            return "Error: La edad debe ser un numero valido entre 0 y 120"
    except ValueError:
        return "Error: La edad debe ser un numero valido"
    
    estudiante = {
        'nombre': nombre,
        'carrera': carrera,
        'edad': edad,
        'numero_control': numero_control
    }

    escuela.append(estudiante)
    return "Estudiante agregado"
    
def mostrar_estudiantes():

    if not escuela:
        return "no hay estudiantes registrados"
    
    resultado = "\nEstudiantes registrados:\n"
    for estudiante in escuela:
        resultado += f"Nombre: {estudiante['nombre']}\n"
        resultado += f"Carrera: {estudiante['carrera']}\n"
        resultado += f"Edad: {estudiante['edad']}\n"
        resultado += f"Numero de control:: {estudiante['numero_control']}\n"
        resultado += "-" * 30 + "\n"
    return resultado

def buscar_estudiante(nombre):

    if not nombre:
        return "Error: debe ingresar un nombre para buscar"
    
    for estudiante in escuela:
        if estudiante['nombre'].lower() == nombre.lower():
            return f"""
Estudiante encontrado:
Nombre: {estudiante['nombre']}
Carrera: {estudiante['carrera']}
Edad: {estudiante['edad']}
Numero de Control: {estudiante['numero_control']}"""
        
        return "Estudiante no encontrado "
    
def eliminar_estudiante(nombre):

    if not nombre:
        return "Error: Debe ingresar un nombre para eliminar"
    
    for i, estudiante in enumerate(escuela):
        if estudiante['nombre'].lower() == nombre.lower():
            escuela.pop(i)
            return "Estudiante eliminado exitosamente"
        
    return "Error: Estudiante no encontrado en la base de datos"

def menu_principal():

    while True:
        print("\n== Gestion de estudiantes==")
        print("1. Agregar estudiantes")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar Estudiante")
        print("5 Salir")

        opcion = input("\nSeleccione una opcion del 1 al 5")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            numero_control = input("Ingrese el numero de control: ")
            print(agregar_estudiantes(nombre, carrera, edad, numero_control))

        elif opcion == "2":
            print(mostrar_estudiantes())

        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante: ")
            print(buscar_estudiante(nombre))

        elif opcion == "4":
            nombre = input("Ingrese el nombre a eliminar: ")
            print(eliminar_estudiante(nombre))

        elif opcion == "5":
            print("Gracias por usar")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu_principal()