from abc import ABC, abstractmethod
from classes.tipoAtendimento import TipoAtendimento
from classes.clinica import Clinica
from classes.paciente import Paciente
from classes.profissional import Profissional
from datetime import date as Date
from typing import List

class Atendimento(ABC):
    @abstractmethod
    def __init__(self, clinica:Clinica, 
                       paciente:Paciente, 
                       profissional:Profissional, 
                       data:Date, 
                       horario_inicio:str,
                       horario_fim:str, 
                       tipo_atendimento: TipoAtendimento,
                       valor: float) -> None:
        
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor
        self.__procedimentos = []

    @property
    @abstractmethod
    def clinica(self) -> Clinica:
        return self.__clinica

    @property
    @abstractmethod
    def paciente(self) -> Paciente:
        return self.__paciente

    @property
    @abstractmethod
    def profissional(self) -> Profissional:
        return self.__profissional

    @property
    @abstractmethod
    def data(self) -> Date:
        return self.__data

    @property
    @abstractmethod
    def horario_inicio(self) -> str:
        return self.__horario_inicio

    @property
    @abstractmethod
    def horario_fim(self) -> str:
        return self.__horario_fim

    @property
    @abstractmethod
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @property
    @abstractmethod
    def valor(self) -> float:
        return self.__valor

    @property
    @abstractmethod
    def procedimentos(self) -> List:
        return self.__procedimentos