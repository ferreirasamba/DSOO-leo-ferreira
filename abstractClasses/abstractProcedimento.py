from abc import ABC, abstractmethod
from classes.profissional import Profissional

class Procedimento(ABC):
    @abstractmethod
    def __init__(self, descricao:str, custo:float, profissional:Profissional):
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
    

    