from abc import ABC, abstractmethod
from abstractClasses.abstractClinica import AbstractClinica
from abstractClasses.pessoa import Pessoa
from abstractClasses.abstractTipoAtendimento import AbstractTipoAtendimento
from datetime import date, time
from utility import ErroDeRegra

class AbstractAtendimento(ABC):
    @abstractmethod
    def __init__(self, clinica:AbstractClinica, 
                       paciente:Pessoa, 
                       profissional:Pessoa, 
                       data:date, 
                       horario_inicio:time, 
                       horario_fim:time, 
                       tipo_atendimento:AbstractTipoAtendimento, 
                       valor):
        if valor < 0:
            raise ErroDeRegra("Valor inválido.")
        if data < date.today():
            raise ErroDeRegra("Data inválida.")
        tempo_valido_inicio = AbstractClinica.abre
        tempo_valido_final = AbstractClinica.fecha
        if horario_inicio < tempo_valido_inicio:
            raise ErroDeRegra("Horário inicial inválido.")
        if horario_fim > tempo_valido_final:
            raise ErroDeRegra("Horário final inválido.")
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor

    @property
    @abstractmethod
    def clinica(self):
        return self.__clinica

    @property
    @abstractmethod
    def paciente(self):
        return self.__paciente

    @property
    @abstractmethod
    def profissional(self):
        return self.__profissional

    @property
    @abstractmethod
    def data(self):
        return self.__data

    @property
    @abstractmethod
    def horario_inicio(self):
        return self.__horario_inicio

    @property
    @abstractmethod
    def horario_fim(self):
        return self.__horario_fim

    @property
    @abstractmethod
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @property
    @abstractmethod
    def valor(self):
        return self.__valor