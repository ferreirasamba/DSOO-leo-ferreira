from abc import ABC, abstractmethod
from datetime import date
from modelo.paciente import Paciente
from util import ErroDeRegra, dinheiro

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, data:date, atendimento, paciente:Paciente, valor):
        valor = dinheiro(valor)
        if valor <= 0:
            raise ErroDeRegra("Valor inválido.")
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente  
        self.__valor = valor

    @property
    @abstractmethod
    def data(self):
        return self.__data

    @property
    @abstractmethod
    def atendimento(self):
        return self.__atendimento

    @property
    @abstractmethod
    def paciente(self):
        return self.__paciente

    @property
    @abstractmethod
    def valor(self):
        return self.__valor

    @abstractmethod
    def modalidade(self) -> str:
        pass

    def __str__(self):
        return f"{self.data:%d/%m/%Y} | R${self.valor} | {self.modalidade()}"