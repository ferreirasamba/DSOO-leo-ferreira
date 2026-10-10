from abc import ABC, abstractmethod
from classes.pagamento import Pagamento

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
        self.__pagamentos.append(pagamento)
        return 0