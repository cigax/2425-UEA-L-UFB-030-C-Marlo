#Se crea la clase semana
class semanas:
    def __init__(self):
        self.temperaturas = []
# La clase semana almacenara las temperaturas
    def temperaturas_semana(self):
        for i in range(7):
            temp = float(input(f"Temperatura del día {i+1}: "))
            self.temperaturas.append(temp)
# Realiza el calculo del promedio de las temperaturas
    def calculo(self):
        if len(self.temperaturas) == 0:
            return 0
        promedio = sum(self.temperaturas) /len(self.temperaturas)
        return promedio
# Función principal del programa
def main():
        print("Promedio de temperatura semanal con la POO")
        semana= semanas ()
        semana.temperaturas_semana()
        promedio = semana.calculo()
        print(f"El promedio de temperatura es: {promedio:.2f}°C")
main()