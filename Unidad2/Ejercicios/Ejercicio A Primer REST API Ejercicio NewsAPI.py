import requests

API_KEY = "6ee26208e57b4377994e8ce46e48a3bc"

def obtener_noticias_por_fecha(fecha):
    url = f"https://newsapi.org/v2/everything?publishedAt={fecha}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()

while True:
    print("¡Bienvenido al Cliente de NewsAPI!")
    print("Selecciona una opción:")
    print("1. Buscar noticias por autor")
    print("2. Buscar noticias por fuente")
    print("3. Listar noticias por autor y título")
    print("4. Salir")

    opcion = input("Ingresa tu opción (1-4): ")

    if opcion == "1":
        autor = input("Ingresa el nombre del autor: ")
        if autor.strip() == "":
            print("El nombre del autor no puede estar vacío.")
            continue

        response = requests.get(f"https://newsapi.org/v2/everything?author={autor}&apiKey={API_KEY}")
        data = response.json()
        print(f"Código de estado: {response.status_code}")
        print(f"Total de resultados: {data['totalResults']}")

        for articulo in data['articles']:
            print(f"Autor: {articulo['author']}")
            print(f"Título: {articulo['title']}")
            print(f"Descripción: {articulo['description']}")
            print()

    elif opcion == "2":
        fuente = input("Ingresa el nombre de la fuente: ")
        if fuente.strip() == "":
            print("El nombre de la fuente no puede estar vacío.")
            continue

        response = requests.get(f"https://newsapi.org/v2/everything?sources={fuente}&apiKey={API_KEY}")
        data = response.json()
        print(f"Código de estado: {response.status_code}")
        print(f"Total de resultados: {data['totalResults']}")

        for articulo in data['articles']:
            print(f"Autor: {articulo['author']}")
            print(f"Título: {articulo['title']}")
            print(f"Descripción: {articulo['description']}")
            print()

    elif opcion == "3":
        fecha = input("Ingresa la fecha (AAAA-MM-DD): ")
        data = obtener_noticias_por_fecha(fecha)

        for articulo in data['articles']:
            print(f"Autor: {articulo['author']}")
            print(f"Título: {articulo['title']}")
            print()

    elif opcion == "4":
        print("¡Adiós!")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")