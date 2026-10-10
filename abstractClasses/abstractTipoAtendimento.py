from abc import ABC, abstractmethod

class AbstractTipoAtendimento(ABC):
    @abstractmethod
    def __init__(self, tipo_atendimento:str):
        self.__tipo_atendimento = tipo_atendimento.strip()

    @property
    @abstractmethod
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    