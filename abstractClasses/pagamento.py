from abc import ABC, abstractmethod
from datetime import date as Date
from classes.atendimento import Atendimento
from classes.paciente import Paciente

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, data:Date, campo_monetario:Atendimento, paciente:Paciente, valor:float):
        self.__data = data
        self.__campo_monetario = campo_monetario
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
    def pagar(self) -> float:

        campo_monetario = self.__campo_monetario
        valor_campo = self.__campo_monetario.valor
        divida = 0
        troco = 0
        if isinstance(campo_monetario, Atendimento):
            if self.__valor < valor_campo:
                divida += valor_campo - self.__valor
            elif self.__valor > valor_campo:
                troco += self.__valor - valor_campo
            return self.__valor
