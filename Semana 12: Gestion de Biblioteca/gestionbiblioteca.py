class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} / Categoría: {self.categoria} / ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_adquiridos = []

    def __str__(self):
        return f"Usuario: {self.id_usuario} / Nombre: {self.nombre}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  #Diccionario para ISBN
        self.usuarios = {}  #Diccionario para usuarios

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"El libro ha sido agregado a la lista")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"El libro ha sido eliminado de la lista")
        else:
            print("El libro no existe en la lista")

    def nuevo_registro(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("Usuario registrado, inicie sesión")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print("Registro completado, ¡Bienvenido!")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario {id_usuario} eliminado")
        else:
            print("Usuario no existe en la lista")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usted no está registrado, no puede adquirir ningún libro")
            return
        if isbn not in self.libros:
            print("El libro no está disponible por el momento")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_adquiridos.append(libro)
        print(f"Libro prestado: {libro}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no está registrado")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_adquiridos:
            if libro.isbn == isbn:
                usuario.libros_adquiridos.remove(libro)
                self.libros[isbn] = libro
                print(f"{libro} ha sido devuelto a la biblioteca")
                return
        print("El libro no está en la lista de préstamos del usuario")

    def buscar_libro(self, criterio):
        encontrado = False
        for libro in self.libros.values():
            if criterio.lower() in libro.datos[0].lower() or criterio.lower() in libro.datos[1].lower():
                print(f"Se ha encontrado: {libro}")
                encontrado = True
        if not encontrado:
            print("No hay resultados para su búsqueda")


def menu():
    bib = Biblioteca()
    while True:
        print("\nMenú de Opciones:")
        print("1. Registrar nuevo usuario")
        print("2. Eliminar usuario")
        print("3. Préstamo de libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            id_usuario = input("Ingrese ID de usuario: ")
            bib.nuevo_registro(Usuario(nombre, id_usuario))
        elif opcion == "2":
            id_usuario = input("Ingrese ID de usuario: ")
            bib.eliminar_usuario(id_usuario)
        elif opcion == "3":
            id_usuario = input("Ingrese ID de usuario: ")
            isbn = input("Ingrese ISBN: ")
            bib.prestar_libro(id_usuario, isbn)
        elif opcion == "4":
            id_usuario = input("Ingrese ID de usuario: ")
            isbn = input("Ingrese ISBN: ")
            bib.devolver_libro(id_usuario, isbn)
        elif opcion == "5":
            criterio = input("Ingrese el título o autor del libro: ")
            bib.buscar_libro(criterio)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Ingrese una opción válida")


if __name__ == "__main__":
    menu()
