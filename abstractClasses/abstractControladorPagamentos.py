from abc import ABC, abstractmethod
from utility import ErroDeRegra

class AbstractControladorPagamentos(ABC):
    @abstractmethod
    def __init__(self):
        self.__pagamentos = []

    @property
    @abstractmethod
    def pagamentos(self):
        return self.__pagamentos

    @abstractmethod
    def registrar_pagamento(self):
        pass