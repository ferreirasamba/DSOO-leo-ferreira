from abc import ABC, abstractmethod
from datetime import date
from util import so_digito, ErroDeRegra
class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome:str, celular:str, cpf:str, data_nascimento:date):
        cpf = so_digito(cpf)
        if len(cpf) != 11:
            raise ErroDeRegra("CPF deve conter 11 dígitos.")
        if not nome.strip():
            raise ErroDeRegra("Nome não pode ser vazio.")
        if data_nascimento > date.today():
            raise ErroDeRegra("Data de nascimento inválida.")
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

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

    @property
    @abstractmethod
    def data_nascimento(self):
        return self.__data_nascimento

    def idade(self, data:date) -> int:
        n = self.__data_nascimento
        aniversario_passou = (data.month, data.day) >= (n.month, n.day)

        return data.year - n.year - (0 if aniversario_passou else 1)

    @abstractmethod
    def descricao(self) -> str:
        pass

    def __str__(self):
        return self.descricao()