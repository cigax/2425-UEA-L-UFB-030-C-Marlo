# Se crea la clase Archivo
class Archivo:

    # Implementa en metodo constructor
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo

        # El metodo try funciona para tratar excepciones, en este caso, si o no existe archivo
        try:
            self.archivo = open(self.nombre, self.modo)
            print(f"Se ha creado o abierto el archivo '{self.nombre}' con el modo '{self.modo}'")
        except FileNotFoundError:
            self.archivo = None
            print(f"Error: El archivo '{self.nombre}' no existe.")
        except Exception as e:
            self.archivo = None
            print(f"Error inesperado al intentar abrir el archivo '{self.nombre}': {e}")

    # Metodo para escribir en un archivo
    def escribir(self, texto):
        if self.archivo and ('w' in self.modo or 'a' in self.modo or '+' in self.modo):
            try:
                self.archivo.write(texto)
                print(f"Se ha escrito '{texto}' en el archivo '{self.nombre}'")
            except Exception as e:
                print(f"Error al escribir en el archivo '{self.nombre}': {e}")
        else:
            print(f"No se puede escribir en el archivo '{self.nombre}', el modo seleccionado es incompatible.")

    # Metodo para revisar el contenido del archivo
    def revisar(self):
        if self.archivo and ('r' in self.modo or '+' in self.modo):
            try:
                self.archivo.seek(0)  # Mueve el cursor al inicio del archivo
                contenido = self.archivo.read()
                print(f"El archivo '{self.nombre}' tiene el siguiente contenido:\n{contenido}")
            except Exception as e:
                print(f"Error al leer el archivo '{self.nombre}': {e}")
        else:
            print(
                f"No se puede revisar el contenido del archivo '{self.nombre}', el modo seleccionado es incompatible.")

    # Metodo para cerrar el archivo
    def cerrar(self):
        if self.archivo:
            try:
                self.archivo.close()
                self.archivo = None
                print(f"Se ha cerrado el archivo: '{self.nombre}'")
            except Exception as e:
                print(f"Error al cerrar el archivo '{self.nombre}': {e}")
        else:
            print(f"El archivo '{self.nombre}' ya está cerrado o no fue abierto correctamente.")

    # Metodo destructor para asegurar que los archivos se cierran
    def __del__(self):
        if self.archivo:
            try:
                self.archivo.close()
                print(f"Se cerró el archivo '{self.nombre}' desde el destructor.")
            except Exception as e:
                print(f"Error al cerrar el archivo desde el destructor: {e}")


# Ejecución del programa
# Cambia el modo según lo que quieras hacer (r, w, a, r+)
objeto = Archivo("archivo.txt", "w")  # Abre el archivo en modo escritura ("w")

# Escribir texto en el archivo
objeto.escribir("Hola mundo\n")

# Cerrar y reabrir para poder leerlo (necesario si se usó modo "w" antes)
objeto.cerrar()
objeto = Archivo("archivo.txt", "r")  # Reabrimos en modo lectura

# Revisar el contenido del archivo
objeto.revisar()

# Cerrar el archivo
objeto.cerrar()

# Eliminar la instancia
del objeto
