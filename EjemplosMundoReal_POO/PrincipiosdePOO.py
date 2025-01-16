# Codigo para agendar citas en un hospital
class Paciente:

    # Son los datos del paciente

    def __init__(self, nombre, edad, ci_paciente):
        self.nombre = nombre
        self.edad = edad
        self.ci_paciente = ci_paciente
        self.historial_medico = []

#Contiene información sobre el estado de los pacientes

    def historial(self, descripcion):
        self.historial_medico.append(descripcion)

# Muestra el historial del paciente

    def mostrar_historial(self):
        print(f"Historial médico de {self.nombre}:")
        for entrada in self.historial_medico:
            print(f"- {entrada}")

#COntiene los datos del especialista

class Doctor:
    def __init__(self, nombre, especialidad, codigo_doctor):
        self.nombre = nombre
        self.especialidad = especialidad
        self.codigo_doctor = codigo_doctor
        self.disponible = True

#La clase cita contiene los datos sobre la fecha en la que sera atendido el paciente

class Cita:
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

#Fecha de la cita

    def fecha_cita(self):
        print(f"Cita programada: \nPaciente: {self.paciente.nombre}\nDoctor: {self.doctor.nombre}\nFecha: {self.fecha} - Hora: {self.hora}")

# Muestra si la cita agendad fue cancelada por el paciente

    def cancelar_cita(self):
        print(f"La cita con el Dr. {self.doctor.nombre} fue cancelada por el paciente {self.paciente.nombre}.")

# Todos los datos que contiene el hospital sobre los paciente, datos básicos de registro

if __name__ == "__main__":
    paciente = Paciente("Fernando Vera", 30, "1735456789")
    paciente1 = Paciente("Elliot Alderson", 27, "1736543211")

    doctor = Doctor("Angela Moss", "Cardiología", "D001")
    doctor1 = Doctor("Tyrell Wellick", "Psicología Clínica", "D002")

    paciente.historial("Consulta inicial - Presión Arterial Alta")
    paciente.historial("Consulta final - Se receta medicamento lisinopril (Prinivil, Zestril)")
    paciente1.historial("Consulta inicial - Trastorno Ansioso/Depresivo")
    paciente1.historial("Consulta final - Se receta medicamento antidepresivo Alprazolam")

# Imprime el historial del paciente

    paciente.mostrar_historial()
    print()
    paciente1.mostrar_historial()
    print()

#Dia, fecha y hora de la cita

    cita = Cita(paciente, doctor, "2025-01-20", "10:00")
    cita1 = Cita(paciente1, doctor1, "2025-01-21", "11:00")


    cita.fecha_cita()
    print()
    cita1.fecha_cita()
    print()

# Una cita fue cancelada por un paciente

    cita1.cancelar_cita()
    print()
