from abc import ABC, abstractmethod
from datetime import date as Date
from classes.atendimento import Atendimento
from classes.paciente import Paciente

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, data:Date, atendimento:Atendimento, paciente:Paciente, valor:float):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor = valor

    