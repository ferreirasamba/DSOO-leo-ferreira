from abc import ABC, abstractmethod
from utility import ErroDeRegra
from abstractClasses.abstractAtendimento import AbstractAtendimento
from abstractClasses.pessoa import Pessoa
from datetime import date

class AbstractPagamento(ABC):
    @abstractmethod
    def __init__(self, data:date, atendimento:AbstractAtendimento, paciente:Pessoa, valor_pago) -> None:
        if valor_pago <= 0:
            raise ErroDeRegra("Valor inválido.")
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

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
    def valor_pago(self):
        return self.__valor_pago
        