# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones

def mostrar_libros(biblioteca):
    # Recorre la lista y muestra la información de cada libro
    
    for l in biblioteca:
        print("Título: ", l["titulo"])
        print("Autor: ", l["autor"])
        print("Año: ", l["anio"])
        print("Genero: ", l["genero"])
        print("Prestamos del libro: ", l["prestamos"])




def buscar_por_autor(biblioteca, autor):
    # Devuelve una lista con los títulos de un autor dado
    for l in biblioteca:
        if l["autor"].lower() == autor.lower():
            print("Libros del autor", autor, ": ", l["titulo"])


def prestamo(biblioteca, titulo, usuario):
    # Registra un préstamo de un libro por un usuario
    for l in biblioteca:
        if l["titulo"].lower() == titulo.lower():
            if usuario in l["prestamos"] :
                l["prestamos"][usuario] += 1
            else:
                l["prestamos"][usuario] = 1
                

def libro_mas_popular(biblioteca):
    # Devuelve el libro con más préstamos totales
    masprestramos = 0
    for l in biblioteca:
        #Prestamo de cada libro
        suma = list(l["prestamos"].values())
        print("El libro", l["titulo"], " tiene", sum(suma), " prestamos")
        
        #El mas popular
        totalprestamos = sum(l["prestamos"].values())
        if totalprestamos > masprestramos:
            masprestamos = totalprestamos
            maspopular = l["titulo"]
    return maspopular

def estadisticas_usuarios(biblioteca):
    # Devuelve un diccionario con total de préstamos por usuario
    usuarios = {}
    for l in biblioteca:
        for usuario, cantidad in l["prestamos"].items():
            if usuario in usuarios:
                usuarios[usuario] += cantidad
            else:
                usuarios[usuario] = cantidad

# Programa principal
def main():
    # 1. Crear biblioteca con al menos 5 libros
    biblioteca = [
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "anio": 1967,
            "genero": "Novela",
            "prestamos": {"Alba":2, "Irene":4}
        },
        {
            "titulo": "El Quijote",
            "autor": "Miguel de Cervantes",
            "anio": 1605,
            "genero": "Novela",
            "prestamos": {"Andrea":7}
        },
        # Añadir más libros aquí...
        {
            "titulo": "La Fabrica de Chocolate",
            "autor": "Julio Jimenez",
            "anio": 1956,
            "genero": "Novela",
            "prestamos": {"Ramon":3, "Irene":3}
        },
        {
            "titulo": "No sin mi hija",
            "autor": "La",
            "anio": 1998,
            "genero": "Novela",
            "prestamos": {"Julia":2, "Seba":1}
        },
        {
            "titulo": "Cumbres Borrascosas",
            "autor": "La",
            "anio": 1605,
            "genero": "Novela",
            "prestamos": {"Loli":2}
        }
    ]

    # 2. Mostrar todos los libros
    mostrar_libros(biblioteca)
    
    # 3. Buscar por autor (pedir al usuario un nombre)
    autorbuscar=(input("¿Que autor quieres buscar?: "))
    buscar_por_autor(biblioteca,autorbuscar)
    
    # 4. Simular préstamos
    tituloalquila=(input("¿Que libro quieres alquilar?: "))
    nombrealquila=(input("Introduzca su nombre: "))
    prestamo(biblioteca,tituloalquila,nombrealquila)
    
    # 5. Mostrar el libro más popular
    libroMasPopular = libro_mas_popular(biblioteca)
    print(libroMasPopular)
    # 6. Mostrar estadísticas de usuarios
    estadisticas_usuarios(biblioteca)

# Ejecutar programa
if __name__ == "__main__":
    main()
