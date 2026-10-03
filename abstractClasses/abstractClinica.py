from abc import ABC, abstractmethod

class Clinica(ABC):
    @abstractmethod
    def __init__(self, nome, localizacao, descricao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @property
    @abstractmethod
    def localizacao(self):
        return self.__localizacao

    @property
    @abstractmethod
    def descricao(self):
        return self.__descricao

    