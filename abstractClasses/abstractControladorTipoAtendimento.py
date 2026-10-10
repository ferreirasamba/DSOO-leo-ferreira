from abc import ABC, abstractmethod
from abstractClasses.abstractTipoAtendimento import AbstractTipoAtendimento

class AbstractControladorTipoAtendimento(ABC):
    @abstractmethod
    def __init__(self):
        self.__tipo_atendimentos_registrados = []

    @property
    @abstractmethod
    def tipo_atendimentos_registrados(self):
        return self.__tipo_atendimentos_registrados

    @abstractmethod
    def registrar_tipo_atendimento(self, tipo_atendimento:AbstractTipoAtendimento):
        pass

    