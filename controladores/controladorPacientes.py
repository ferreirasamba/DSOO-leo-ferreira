from abstractClasses.abstractControladorPacientes import AbstractControladorPacientes
from model.paciente import Paciente

class controladorPacientes(AbstractControladorPacientes):
    def __init__(self):
        super().__init__()

    @property
    def pacientes(self):
        return super().pacientes

    def registrar_paciente(self, paciente:Paciente):
        self.pacientes.append(paciente)