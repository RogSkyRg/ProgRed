import requests

def linea(simbolo='*', longitud=10):
    for _ in range(longitud):
        print(simbolo, end=' ')
    print()  

titulo = ""
while not titulo:
    titulo = input("Ingrese el título del libro: ")

def buscar_libro(titulo):
    url = f"https://openlibrary.org/search.json?q={titulo}"  
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        print("Error en la solicitud")
    else:
        libros = respuesta.json().get('docs', [])
        if libros:
            print("Libros encontrados:")
            for libro in libros[:5]:  
                print(f"- {libro.get('title')} por {', '.join(libro.get('author_name', []))}")
        else:
            print("No se encontraron libros.")

linea('#', 20)

buscar_libro(titulo)
