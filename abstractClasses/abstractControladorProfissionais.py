from abc import ABC, abstractmethod
from abstractClasses.pessoa import Pessoa

class AbstractControladorProfissionais(ABC):
    @abstractmethod
    def __init__(self):
        self.__profissionais = []

    @property
    @abstractmethod
    def profissionais(self):
        return self.__profissionais

    @abstractmethod
    def registrar_profissional(self, profissional:Pessoa):
        pass