class Personaje:
    def __init__(self, nombre, Ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = Ataque
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        print("\nAtributos de", self.nombre)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def atacar(self, enemigo):
        daño = self.ataque - enemigo.defensa
        if daño < 0:
            daño = 0

        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} y le hace {daño} de daño.")

        if enemigo.vida > 0:
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            print(f"{enemigo.nombre} ha sido derrotado.")


class Guerrero(Personaje):
    def __init__(self, nombre, ataque, defensa, vida):
        super().__init__(nombre, ataque, defensa, vida)

    def grito_batalla(self):
        print(f"{self.nombre} grita: ¡Por la victoria!")


class Mago(Personaje):
    def __init__(self, nombre, ataque, defensa, vida, magia):
        super().__init__(nombre, ataque, defensa, vida)
        self.magia = magia

    def lanzar_hechizo(self, enemigo):
        print(f"{self.nombre} lanza un hechizo mágico.")
        daño = self.magia - enemigo.defensa
        if daño < 0:
            daño = 0

        enemigo.vida -= daño
        print(f"El hechizo hace {daño} de daño a {enemigo.nombre}.")
        if enemigo.vida > 0:
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            print(f"{enemigo.nombre} ha sido derrotado.")

guerrero = Guerrero("Leonardo", ataque=15, defensa=5, vida=50)
mago = Mago("Vanessa", ataque=5, defensa=3, vida=40, magia=12)

guerrero.mostrar_atributos()
mago.mostrar_atributos()

print("\n !A Pelear¡ ")
guerrero.grito_batalla()
guerrero.atacar(mago)
mago.lanzar_hechizo(guerrero)

print("\n !Fin del combate¡")
guerrero.mostrar_atributos()
mago.mostrar_atributos()
