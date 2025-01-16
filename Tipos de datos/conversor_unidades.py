#Este programa convertira distancias entre kilometros y millas


#Esta funcion realiza la operación de kilometros a millas
def km_millas (kilometros):
    millas = kilometros * 0.621371
    return millas

#Esta funcion realiza la operación de millas a kilometros

def millas_km (millas):
    kilometros = millas / 0.621371
    return kilometros

#Menu principal del programa
def convertir_distancias():
    print("Bienvenido al conversor de distancias")
    print("1. Convertir kilometros a millas")
    print("2. Convertir millas a kilometros")

#Menu de opciones, si la opcion elegida no coincide con 1 o 2 lanza un mensaje de error

    menu = input("Elige una opción: ")
    if menu not in ["1", "2"]:
        print("Valor incorrecto, selecciona una opción correcta")
        return

#Esta sección captura y maneja exepciones

    try:
        valor_str = input("Ingresa el valor a convertir: ")
        valor = float(valor_str.replace(",", "."))
        if valor < 0:
            print("Valor incorrecto, no se puede convertir valores negativos")
            return

        if menu == "1":
            resultado = km_millas(valor)
            print(f"El resultado de {valor} kilometros a millas es: {resultado:.2f} millas")

        else:
            resultado = millas_km(valor)
            print(f"El resultado de {valor} millas a kilometros es: {resultado:.2f} kilometros")
    except ValueError:
        print("Valor incorrecto, ingresa un número correcto")

if __name__ == "__main__":
    convertir_distancias()