import requests

def menu():
    print("Seleccione una opción:")
    print("1. Buscar Pokémon por nombre")
    print("2. Listar generaciones de Pokémon")
    print("3. Consultar detalles de una generación")
    print("4. Salir")

    while True:
        opcion = input("Ingrese el número de la opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 4:
            return int(opcion)
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        print(f"Nombre: {data['name'].capitalize()}")
        print(f"Tipo(s): {', '.join(type['type']['name'].capitalize() for type in data['types'])}")
        print(f"Estadísticas:")
        for stat in data['stats']:
            print(f"- {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
    else:
        print("Pokémon no encontrado.")

def listar_generaciones():
    url = "https://pokeapi.co/api/v2/generation/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        for generation in data['results']:
            print(f"ID: {generation['url'].split('/')[-2]}, Nombre: {generation['name'].capitalize()}")
    else:
        print("Error al obtener las generaciones.")

def consultar_generacion(id_generacion):
    url = f"https://pokeapi.co/api/v2/generation/{id_generacion}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        print(f"Nombre: {data['name'].capitalize()}")
        print(f"Número de Pokémon: {len(data['pokemon_species'])}")
        print("Pokémon de esta generación:")
        for pokemon in data['pokemon_species']:
            print(f"- {pokemon['name'].capitalize()}")
    else:
        print("Generación no encontrada.")

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
            buscar_pokemon(nombre_pokemon)
        elif opcion == 2:
            listar_generaciones()
        elif opcion == 3:
            id_generacion = input("Ingrese el ID de la generación: ")
            if id_generacion.isdigit():
                consultar_generacion(int(id_generacion))
            else:
                print("ID no válida. Debe ser un número.")
        elif opcion == 4:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()