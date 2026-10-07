from abc import ABC, abstractmethod
from classes.pagamento import Pagamento
from classes.pagamento import pagar


class controladorPagamentos(ABC):
    @abstractmethod
    def __init__(self):
        self.__pagamentos = []

    @property
    @abstractmethod
    def pagamentos(self):
        return self.__pagamentos

    @abstractmethod
    def registrar_pagamento(self, pagamento: Pagamento):
        pass