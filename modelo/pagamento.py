from abc import ABC, abstractmethod
from datetime import date
from modelo.paciente import Paciente
from modelo.atendimento import Atendimento
from utilidades import ErroDeRegra, dinheiro

class Pagamento(ABC):
    def __init__(self, data:date,
                       atendimento:Atendimento,
                       paciente:Paciente,
                       valor):
        valor = dinheiro(valor)
        if valor <= 0:
            raise ErroDeRegra("Valor do pagamento deve ser positivo.")
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @property
    def atendimento(self):
        return self.__atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def modalidade(self) -> str:
        pass

    def __str__(self):
        return f"{self.data:%d/%m/%Y} | R$ {self.valor} | {self.modalidade}"
    