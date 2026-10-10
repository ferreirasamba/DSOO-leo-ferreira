from abstractClasses.pessoa import Pessoa
from datetime import date
from utility import ErroDeRegra

class Profissional(Pessoa):
    def __init__(self, nome:str, celular:str, cpf:str, especialidade:str, registro:str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro = registro

    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def cpf(self):
        return super().cpf

    def especialidade(self):
        return self.__especialidade

    def registro(self):
        return self.__registro

    