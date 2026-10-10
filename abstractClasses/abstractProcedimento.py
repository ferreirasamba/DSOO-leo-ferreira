from abc import ABC, abstractmethod
from abstractClasses.pessoa import Pessoa
from utility import ErroDeRegra

class AbstractProcedimento(ABC):
    @abstractmethod
    def __init__(self, descricao:str, custo, profissional:Pessoa):
        if not descricao.strip():
            raise ErroDeRegra("Descrição inválida.")
        if custo < 0:
            raise ErroDeRegra("Custo inválido.")
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    @abstractmethod
    def descricao(self):
        return self.__descricao

    @property
    @abstractmethod
    def custo(self):
        return self.__custo

    @property
    @abstractmethod
    def profissional(self):
        return self.__profissional