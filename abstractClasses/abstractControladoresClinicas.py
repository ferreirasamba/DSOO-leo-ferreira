from abc import ABC, abstractmethod

class AbstractControladorClinicas(ABC):
    @abstractmethod
    def __init__(self):
        self.__clinicas = []

    @property
    @abstractmethod
    def clinicas(self):
        return self.__clinicas    

    @abstractmethod
    def registrar_clinica(self):
        pass
