from abc import ABC, abstractmethod
from pessoa import Pessoa

class AbstractControladorPacientes(ABC):
    @abstractmethod
    def __init__(self):
        self.__pacientes = []

    @property
    @abstractmethod
    def pacientes(self):
        return self.__pacientes

    @abstractmethod
    def registrar_paciente(self, paciente:Pessoa):
        pass