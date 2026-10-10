from abc import ABC, abstractmethod
from abstractClasses.abstractAtendimento import AbstractAtendimento

class AbstractControladorAtendimento(ABC):
    @abstractmethod
    def __init__(self):
        self.__atendimentos = []

    @property
    @abstractmethod
    def atendimentos(self):
        return self.__atendimentos

    @abstractmethod
    def registrar_atendimentos(self, atendimento:AbstractAtendimento):
        pass