from abc import ABC, abstractmethod
from datetime import time
from utility import ErroDeRegra
class AbstractClinica(ABC):
    @abstractmethod
    def __init__(self, nome:str, cidade:str, descricao:str, abre:time, fecha:time):
        if not nome.strip():
            raise ErroDeRegra("Nome inválido.")
        if not cidade.strip():
            raise ErroDeRegra("Cidade inválida.")
        if not descricao.strip():
            raise ErroDeRegra("Descrição inválida.")
        if abre > fecha:
            raise ErroDeRegra("Funcionamento inválido.")
        self.__nome = nome.strip()
        self.__cidade = cidade.strip()
        self.__descricao = descricao.strip()
        self.__abre = abre
        self.__fecha = fecha

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @property
    @abstractmethod
    def cidade(self):
        return self.__cidade

    @property
    @abstractmethod
    def descricao(self):
        return self.__descricao

    @property
    @abstractmethod
    def abre(self):
        return self.__abre

    @property
    @abstractmethod
    def fecha(self):
        return self.__fecha

    @abstractmethod
    def funciona_em(self, abertura:time, fechamento:time) -> bool:
        return abertura > self.abre and fechamento < self.fecha