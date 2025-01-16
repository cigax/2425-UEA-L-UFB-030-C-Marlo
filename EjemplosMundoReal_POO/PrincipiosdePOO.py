#Codigo para agendar citas en un hospital
class Paciente:

#Son los datos del paciente

    def __init__(self, nombre, edad, ci_paciente):
        self.nombre = nombre
        self.edad = edad
        self.ci_paciente = ci_paciente
        self.historial_medico = []

    def historial(self, descripcion):
        self.historial_medico.append((descripcion, self.edad))

    def mostrar_historial(self):
        print("Historial médico: {self.nombre}")
        for entrada in self.historial_medico:
            print(f"-{entrada}")

class Doctor:
     def __init__(self, nombre, especialidad, codigo_doctor):
            self.nombre = nombre
            self.especialidad = especialidad
            self.codigo_doctor = codigo_doctor
            self.disponible = True

    def estado_disponibilidad(self, estado):
            self.disponible = estado
    def mostrar_disponibilidad(self):
            estado = f"Doctor disponible" if self.disponible else "Doctor no disponible"
            print(f"Dr. {self.nombre} ({self.especialidad}) - {estado})

class Cita:
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def fecha_cita(self):
        print(f"Cita programada: \nPaciente: {self.paciente.nombre}\nDoctor: {self.doctor.nombre}\nFecha: {self.fecha} - Hora: {self.hora}")

    def cancelar_cita(self):
        print(f"La cita con {self.doctor.nombre} fue cancelada por el paciente {self.paciente.nombre}.")

if __name__ == "__main__":
    paciente: Paciente ("Fernando Vera", 30, "123456789" )
    paciente1: Paciente ("Elliot Alderson", 27, "987654321")

    doctor: Doctor("Angela Moss", "Cardiología")
    doctor1: Doctor("Tyrell Wellick", "Psicologia Clinica")

    paciente.historial("Consulta inicial - Presión Arterial Baja")
    paciente.historial("Consulta final - Se receta medicamento lisinopril (Prinivil, Zestril)")
    paciente1.historial("Consulta inicial - Trastorno Ansioso/Depresivo")
    paciente1.historial("Consulta final - Se receta medicamento antidepresivo Alprazolam")

    paciente.historial()
    print()
    paciente1.historial()
    print()

    cita: Cita(paciente, doctor, "2025-01-20", "10:00")
    cita1: Cita(paciente1, doctor1, "2025-01-21", "11:00")

    cita.mostrar_cita()
    print()
    cita1.mostrar_cita()
    print()

    cita1.cancelar_cita()
    print()

    doctor.mostrar_disponibilidad()
    doctor1.mostrar_disponibilidad()