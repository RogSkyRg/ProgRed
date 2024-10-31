import requests

def menu():
    print("Seleccione una opción:")
    print("1. Buscar equipo por nombre")
    print("2. Buscar jugador por nombre")
    print("3. Listar ligas")
    print("4. Consultar detalles de una liga")
    print("5. Salir")

    while True:
        opcion = input("Ingrese el número de la opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            return int(opcion)
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def buscar_equipo(nombre_equipo):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={nombre_equipo}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        data = respuesta.json()
        if data['teams']:
            equipo = data['teams'][0]
            print(f"Nombre de la liga: {equipo['strLeague']}")
            print(f"Descripción: {equipo['strDescriptionES']}")
            print(f"Pág. oficial: {equipo['strWebsite']}")
            print(f"Estadio: {equipo['strStadium']}")
        else:
            print("Equipo no encontrado.")
    else:
        print("Error en la solicitud.")

def buscar_jugador(nombre_jugador):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={nombre_jugador}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        if data['player']:
            jugador = data['player'][0]
            print(f"Nombre completo: {jugador['strPlayer']}")
            print(f"Nacionalidad: {jugador['strNationality']}")
            print(f"Equipo: {jugador['strTeam']}")
            print(f"Lugar de nacimiento: {jugador['strBirthLocation']}")
            print(f"Facebook: {jugador['strFacebook']}")
            print(f"Altura: {jugador['strHeight']}")
            print(f"Peso: {jugador['strWeight']}")
        else:
            print("Jugador no encontrado.")
    else:
        print("Error en la solicitud.")

def listar_ligas():
    url = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        for liga in data['leagues']:
            print(f"ID: {liga['idLeague']}, Nombre: {liga['strLeague']}")
    else:
        print("Error en la solicitud.")

def consultar_liga(id_liga):
    url = f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={id_liga}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        if data['leagues']:
            liga = data['leagues'][0]
            print(f"Nombre de la liga: {liga.get('strLeague', 'No disponible')}")
            print(f"Descripción: {liga.get('strDescription', 'No disponible')}")
            print(f"País: {liga.get('strCountry', 'No disponible')}")
        else:
            print("Liga no encontrada.")
    else:
        print("Error en la solicitud.")


def main():
    while True:
        opcion = menu()
        
        if opcion == 1:
            nombre_equipo = input("Ingrese el nombre del equipo: ")
            buscar_equipo(nombre_equipo)
        elif opcion == 2:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            buscar_jugador(nombre_jugador)
        elif opcion == 3:
            listar_ligas()
        elif opcion == 4:
            id_liga = input("Ingrese el ID de la liga: ")
            if id_liga.isdigit():
                consultar_liga(int(id_liga))
            else:
                print("ID no válida. Debe ser un número.")
        elif opcion == 5:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
