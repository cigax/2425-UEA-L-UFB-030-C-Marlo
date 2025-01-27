
#Se crea la clase Archivo

class Archivo:

    # Implementa en método constructor

    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo

        #El método tray funciona para tratar excepciones, en este caso, si o no existe archivo
        try:
            self.archivo = open(self.nombre, self.modo)
            print(f"Se ha creado el archivo '{self.nombre}' con el modo '{self.modo}'")
        except FileNotFoundError:
            self.archivo = None
            print(f"Error: EL archivo '{self.nombre}' no existe")

    #Funcion escribir para definir los atributos que tomanar de las instancias

    def escribir(self, texto):
        if self.archivo and ('w' in self.modo or 'a' in self.modo or '+' in self.modo) :
            self.archivo.write(texto)
            print(f"Se ha escrito '{texto}' en el archivo '{self.nombre}'")
        else:
            print(f"No se puede escribir en el archivo '{self.nombre}'")

    #Funcion revisar, revisara el contenido escrito en el .txt creado

    def revisar(self):
        if self.archivo and ('r' in self.modo or '+' in self.modo):
            self.archivo.seek(0)
            contenido = self.archivo.read()
            print(f"El archivo '{self.nombre}' tiene el siguiente contenido:\n{contenido}")
        else:
            print(f"No se puede revisar el contenido del archivo '{self.nombre}'")

    #Cierra el archivo de modificaciones o escrituras

    def cerrar(self):
        if self.archivo:
            self.archivo.close()
            self.archivo = None
            print(f"Se ha cerrado el archivo: '{self.nombre}'")
        else:
            print(f"El archivo '{self.nombre}' ya se ha cerrado")

    # Metodo destructor acaba con la instancia de la clase creada

    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Se cerro el archivo: '{self.nombre}'")

#objeto = Archivo("archivo.txt", "r")
objeto = Archivo("archivo2.txt", "w")

objeto.escribir("Hola mundo")

objeto.revisar()

objeto.cerrar()

del objeto

