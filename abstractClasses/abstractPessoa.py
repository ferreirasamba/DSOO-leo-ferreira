from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome, celular, cpf):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @property
    @abstractmethod
    def celular(self):
        return self.__celular

    @property
    @abstractmethod
    def cpf(self):
        return self.__cpf

    