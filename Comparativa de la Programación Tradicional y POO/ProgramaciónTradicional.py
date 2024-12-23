# Primera función del código: obtendrá la información del clima por 7 días
def semanas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Estructuramos una función para realizar el cálculo promedio
def calculo(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Es la funcionalidad principal de este programa
def main():
    print("Promedio de temperatura semanal con programación tradicional")
    temperaturas = semanas()
    promedio = calculo(temperaturas)
    print(f"El promedio de temperaturas de esta semana es: {promedio:.2f}°C")

# Esta linea de comandos ejecuta el programa principal
main()
