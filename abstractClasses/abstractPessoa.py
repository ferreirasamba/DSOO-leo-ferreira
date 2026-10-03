from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome, celular, pdf):
        self.__nome = nome
        self.__celular = celular
        self.__pdf = pdf

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
    def pdf(self):
        return self.__pdf

    