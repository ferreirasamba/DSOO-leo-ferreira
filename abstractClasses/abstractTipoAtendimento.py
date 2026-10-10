from abc import ABC, abstractmethod

class TipoAtendimento(ABC):
    @abstractmethod
    def __init__(self, tipo_atendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    @abstractmethod
    def tipo_atendimento(self):
        return self.__tipo_atendimento