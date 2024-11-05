import requests

def obtener_serie_por_nombre(nombre_serie):
    url = f"https://api.tvmaze.com/search/shows?q={nombre_serie}"
    response = requests.get(url)
    return response.json()

def obtener_series_por_genero(genero):
    url = f"https://api.tvmaze.com/shows?genre={genero}"
    response = requests.get(url)
    return response.json()

def mostrar_informacion_serie(serie):
    print(f"Nombre: {serie['name']}")
    print(f"Resumen: {serie['summary']}")
    print(f"Género: {', '.join(serie['genres'])}")
    
    if serie['network'] and serie['network']['country']:
        print(f"País: {serie['network']['country']['name']}")
    else:
        print("País: N/A")
    
    print()

while True:
    print("¡Bienvenido al Cliente de TVMaze!")
    print("Selecciona una opción:")
    print("1. Buscar por nombre de serie")
    print("2. Buscar por género de serie")
    print("3. Salir")

    opcion = input("Ingresa tu opción (1-3): ")

    if opcion == "1":
        nombre_serie = input("Ingresa el nombre de la serie: ")
        if nombre_serie.strip() == "":
            print("El nombre de la serie no puede estar vacío.")
            continue

        datos_serie = obtener_serie_por_nombre(nombre_serie)
        if datos_serie:
            for resultado in datos_serie:
                mostrar_informacion_serie(resultado['show'])
        else:
            print("No se encontraron resultados.")

    elif opcion == "2":
        genero = input("Ingresa el género de la serie: ")
        if genero.strip() == "":
            print("El género no puede estar vacío.")
            continue

        datos_serie = obtener_series_por_genero(genero)
        if datos_serie:
            for serie in datos_serie:
                mostrar_informacion_serie(serie)
        else:
            print("No se encontraron resultados.")

    elif opcion == "3":
        print("¡Adiós!")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")