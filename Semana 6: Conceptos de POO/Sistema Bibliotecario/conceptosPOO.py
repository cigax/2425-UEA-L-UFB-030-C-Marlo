#Ejemplo practico de conceptos de POO

#Progrma para gestionar el sistema de una biblioteca

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []
        self.libros_reservador = []
        self.reservas = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def reservar_libro(self, titulo, tipo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.tipo == tipo:
                self.libros_reservador.append(libro)
                self.libros_disponibles.remove(libro)
                self.reservas.append(f"Libro '{titulo}' ({tipo}) reservado")
                return
        self.reservas.append(f"Libro '{titulo}' ({tipo}) no disponible")

    def historial_reservas (self):
        if not self.libros_reservador:
            print("No hay reservas")
        else:
            print("\nReservas:")
            for libro in self.libros_reservador:
                print(f"- {libro.descripcion()}")

class Libro:
    def __init__(self, genero, titulo, autor, editorial, fecha_lanzamiento, tipo):
        self.genero = genero
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_lanzamiento = fecha_lanzamiento
        self.tipo = tipo

    def descripcion(self):
        return f"Genero: {self.genero}, Titulo: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Año: {self.fecha_lanzamiento}, Tipo: {self.tipo}"

if __name__ == "__main__":
    biblioteca = Biblioteca()

    biblioteca.agregar_libro(Libro("Novela","1984", "George Orwell", "Editorial El Libro", "1949", "Libro"))
    biblioteca.agregar_libro(Libro("Novela", "1984", "George Orwell", "Editorial El Libro", "1949", "Libro Digital"))
    biblioteca.agregar_libro(Libro("Ciencia Ficcón", "El Juego de Ender", "Orson Scott Card", "Editorial Ficción", "1985", "Libro Digital"))
    biblioteca.agregar_libro(Libro("Novela/Misrerio/Aventura", "La Sombra del Viento", "Carlos Ruiz Safón", "Editorial mágica", "2001", "Libro"))
    biblioteca.agregar_libro(Libro("Novela/Misterio/Aventura", "La Sombra del Viento", "Carlos Ruiz Safón", "Editorial mágica", "2001", "Libro Digital"))
    biblioteca.agregar_libro(Libro("Novela clásica/Aventura", "Moby Dick", "Herman Melville", "Editorial El Libro", "1851", "Libro"))
    biblioteca.agregar_libro(Libro("Novela Histórica/Misterio", "El nombre de la Rosa", "Umberto Eco", "Editorial mágica", "1980", "Libro"))

    while True:
        print("\n -- Tienda Virtual -- ")
        print("1. Constultar Libro")
        print("2. Reservar libro")
        print("3. Ver historial de reservas")
        print("4. Salir")

        opciones = input("Que deseas hacer? ")

        if opciones == "1":
            print("\nLibros Disponibles")
            for libro in biblioteca.libros_disponibles:
                print(f"- {libro.descripcion()}")

        elif opciones == "2":
            titulo = input("Ingresa el titulo del libro que desea reservar: ")
            tipo = input("Ingresa el tipo del libro (Libro/Libro Digital): ")
            biblioteca.reservar_libro(titulo, tipo)

        elif opciones == "3":
            biblioteca.historial_reservas()


        elif opciones == "4":
            print("Saliendo del programa")
            break


