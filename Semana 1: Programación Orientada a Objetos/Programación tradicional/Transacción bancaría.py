class CuentaBancaria:
    def __init__(self, numero_de_cuenta, valor_cuenta=0, intereses=0.05 ):
        self.numero_de_cuenta = numero_de_cuenta
        self.valor_cuenta = valor_cuenta
        self.intereses = intereses
        self.transacciones = []

    def deposito (self, cantidad):
        self.valor_cuenta += cantidad
        self. transacciones.append(f"Déposito: +{cantidad}")
        print(f"[{self.numero_de_cuenta}] Deposito de ${cantidad}. Saldo actual: ${self.valor_cuenta}")

    def retiro (self, cantidad):
            if cantidad > self.valor_cuenta:
                print(f"[{self.numero_de_cuenta}] La transacción no pudo realizarse, fondos insuficientes")

            else:
                self.valor_cuenta -= cantidad
                self.transacciones.append(f"Retido de: -${cantidad}")
                print(f"[{self.numero_de_cuenta}] Retiro de ${cantidad}. Saldo actual: ${self.valor_cuenta}")

    def calcular_intereses(self):
                    intereses = self.valor_cuenta * self. intereses
                    self.valor_cuenta += intereses
                    self.transacciones.append(f"Intereses: +{round(intereses, 2)}")
                    print(f"[{self.numero_de_cuenta}] Los interéses calculados fueron: ${round(intereses, 2)}, su saldo actual es: ${self.valor_cuenta}")

    def historial_transacciones(self):
        print(f"\nHistorial de transacciones para la cuenta {self.numero_de_cuenta}")
        for transacciones in self.transacciones:
            print(f"- {transacciones}")
        print(f"Saldo de la cuenta: ${self. valor_cuenta}")

cuenta1 = CuentaBancaria(numero_de_cuenta="663512_GGf", valor_cuenta=820, intereses=0.05)
cuenta2 = CuentaBancaria(numero_de_cuenta="663621_TSy", valor_cuenta=500, intereses=0.05)
cuenta3 = CuentaBancaria(numero_de_cuenta="711224_IAh", valor_cuenta=80, intereses=0.05)

cuenta1.deposito(200)
cuenta1.retiro(50)
cuenta1.calcular_intereses()
cuenta1.historial_transacciones()

cuenta2.deposito(1000)
cuenta2.retiro(540)
cuenta2.calcular_intereses()
cuenta2.historial_transacciones()

cuenta3.deposito(1200)
cuenta3.retiro(20)
cuenta3.calcular_intereses()
cuenta3.historial_transacciones()