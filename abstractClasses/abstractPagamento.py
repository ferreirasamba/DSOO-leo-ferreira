from abc import ABC, abstractmethod
from datetime import date as Date
from classes.atendimento import Atendimento
from classes.paciente import Paciente

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, data:Date, atendimento:Atendimento, paciente:Paciente, valor:float):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor = valor

    @property
    @abstractmethod
    def data(self) -> Date:
        return self.__data

    @property
    @abstractmethod
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @property
    @abstractmethod
    def paciente(self) -> Paciente:
        return self.__paciente

    @property
    @abstractmethod
    def valor(self) -> float:
        return self.__valor

    @abstractmethod
    def pagar(self, total) -> float:

        valor_restante = 0

        if self.__valor < total:
            valor_restante = total - self.__valor
            return valor_restante        
        return 0
