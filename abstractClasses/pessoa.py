from abc import ABC, abstractmethod
from utility import cpf_valido, ErroDeRegra

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome:str, celular:str, cpf:str) -> None:
        cpf = cpf_valido(cpf)
        if len(cpf) != 11:
            raise ErroDeRegra("Cpf inválido.")
        if not nome.strip():
            raise ErroDeRegra("Nome inválido.")
        self.__nome = nome.strip()
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

    