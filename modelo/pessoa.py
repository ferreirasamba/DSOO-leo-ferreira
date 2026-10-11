from abc import ABC, abstractmethod
from datetime import date
from utilidades import ErroDeRegra, so_digitos

class Pessoa(ABC):
    def __init__(self, nome:str, 
                       celular:str, 
                       cpf:str, 
                       data_nascimento:date):
        cpf = so_digitos(cpf)
        if len(cpf) != 11:
            raise ErroDeRegra("CPF deve ter 11 dígitos.")
        if not nome.strip():
            raise ErroDeRegra("Nome não pode ser vazio.")
        if data_nascimento > date.today():
            raise ErroDeRegra("Data de nascimento no futuro.")
        self.__nome = nome.strip()
        self.__celular = celular
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @property
    def celular(self):
        return self.__celular

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def idade_em(self, data:date) -> int:
        n = self.__data_nascimento
        aniversario_ja_passou = (data.month, data.day) >= (n.month, n.day)
        return data.year - n.year - (0 if aniversario_ja_passou else 1)

    @abstractmethod
    def descricao(self) -> str:
        pass

    def __str__(self):
        return self.descricao()