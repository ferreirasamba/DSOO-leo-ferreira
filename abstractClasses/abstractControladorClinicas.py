from abc import ABC, abstractmethod
from abstractClasses.abstractClinica import AbstractClinica

class AbstractControladorClinicas(ABC):
    @abstractmethod
    def __init__(self):
        self.__clinicas = []

    @property
    @abstractmethod
    def clinicas(self):
        return self.__clinicas    

    @abstractmethod
    def registrar_clinica(self, clinica:AbstractClinica):
        pass
