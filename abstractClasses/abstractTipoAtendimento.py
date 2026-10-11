from abc import ABC, abstractmethod
from utility import ErroDeRegra
class AbstractTipoAtendimento(ABC):
    @abstractmethod
    def __init__(self, tipo_atendimento:str):
        if not tipo_atendimento.strip():
            raise ErroDeRegra("Tipo de atendimento inválido.")
        self.__tipo_atendimento = tipo_atendimento.strip()

    @property
    @abstractmethod
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    