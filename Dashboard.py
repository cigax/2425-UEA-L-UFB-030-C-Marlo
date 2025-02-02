import os
import subprocess


def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n -- Código de {ruta_script} --\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("No se encontró ningún archivo con ese nombre.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == "posix":  # Linux
            subprocess.run(['kitty', 'python3', ruta_script])
        else:  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    semanas = {
        '1': 'Semana 1: Programación Orientada a Objetos',
        '2': 'Semana 2: Técnicas de Programación',
        '3': 'Semana 3: Comparativa de la Programación Tradicional y POO',
        '4': 'Semana 4: EjemplosMundoReal_POO',
        '5': 'Semana 5: Tipos de datos',
        '6': 'Semana 6: Conceptos de POO',
        '7': 'Semana 7: Metodo constructor y destructor'
    }

    while True:
        print(f"\nMenu Principal - Dashboard")
        for key in semanas:
            print(f"{key} - {semanas[key]}")
        print("0 - Salir")

        eleccion_semana = input("Elija una semana para revisión o '0' para salir: ")
        if eleccion_semana == '0':
            print("Saliendo del programa...")
            break
        elif eleccion_semana in semanas:
            mostrar_sub_menu(os.path.join(ruta_base, semanas[eleccion_semana]))
        else:
            print("Opción inválida, intente de nuevo.")


def mostrar_sub_menu(ruta_semana):
    sub_carpetas = [f.name for f in os.scandir(ruta_semana) if f.is_dir()]


    while True:
        print("\nSeleccione una carpeta:")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i}. {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elija una subcarpeta o '0' para regresar al menú principal: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_semana, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción inválida. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida, intente de nuevo.")


def mostrar_scripts(ruta_sub_carpetas):
    try:
        scripts = [f.name for f in os.scandir(ruta_sub_carpetas) if f.is_file() and f.name.endswith('.py')]
    except FileNotFoundError:
        print("La ruta especificada no existe.")
        return

    while True:
        print("\nSeleccione un script para ejecutar:")
        for i, script in enumerate(scripts, start=1):
            print(f"{i}. {script}")
        print("0 - Regresar al menú anterior.")
        print("9 - Regresar al menú principal.")

        eleccion_script = input("Elija un script o '0' para regresar al menú anterior: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpetas, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Ejecutar script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó ningún programa.")
                        else:
                            print("Opción inválida. Regresando al menú anterior...")
                        input("Presione ENTER para continuar...")
                else:
                    print("Opción inválida, intente de nuevo.")
            except ValueError:
                print("Entrada inválida, intente de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
